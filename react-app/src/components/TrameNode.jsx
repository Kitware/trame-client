import { createElement, useMemo, useRef, useSyncExternalStore } from "react";
import { useTrame } from "../runtime/trameContext";
import { useResolvedNode } from "../runtime/resolveNode";
import { createSnapshotCache, evalTracked } from "../runtime/expr";
import { buildMergedScope } from "../runtime/scope";
import { resolveTag, isStructuralTag } from "../runtime/tags";
import { useLiteralChildren } from "../runtime/resolveLiteralChildren";

function isBindLeaf(node) {
  return node !== null && typeof node === "object" && !Array.isArray(node) && "js" in node;
}

// A `{js: "..."}` leaf found directly in a `children` array (text
// interpolation, react-text-interpolation.md) rather than as a node prop:
// its own small subscription, isolated from whatever sibling nodes surround
// it, so a change to the expression's inputs re-renders only this leaf.
function ExprLeaf({ jsExpression, scope }) {
  const { trame } = useTrame();

  const trackedKeys = useMemo(() => {
    const merged = buildMergedScope(scope, trame.state);
    return evalTracked(jsExpression, merged).keys;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [jsExpression, scope, trame.state]);

  const snapshotCacheRef = useRef(null);
  if (snapshotCacheRef.current === null) snapshotCacheRef.current = createSnapshotCache();

  const value = useSyncExternalStore(
    (onChange) => trame.state.watch(trackedKeys, onChange),
    () =>
      snapshotCacheRef.current(
        evalTracked(jsExpression, buildMergedScope(scope, trame.state)).value,
      ),
  );

  return value;
}

// Plain function (no hooks): has to run at the PARENT's .map() step, not
// inside TrameNodeOne, because React needs an element's `key` before that
// element is even created/mounted.
function computeNodeKey(node, scope, trame, i) {
  const keyProp = node?.props?.key;
  if (keyProp !== null && typeof keyProp === "object" && "js" in keyProp) {
    return evalTracked(keyProp.js, buildMergedScope(scope, trame.state)).value;
  }
  if (keyProp !== undefined) {
    return keyProp;
  }
  return i;
}

// Builds one <TrameNodeOne> element PER node directly, rather than a single
// <TrameNode> element wrapping the whole list - used both by the top-level
// TrameNode component and inline inside TrameNodeOne (below) for a node's
// own children. Passing the array itself as `children` (instead of one
// nested <TrameNode>) matters for a parent Component that inspects its own
// `children` via `React.Children.map`/`toArray` (e.g. MUI's
// Tabs/RadioGroup/ButtonGroup, which clone each item to inject per-item
// props like `onClick`/`selected`): with a single wrapper element in the
// way, React.Children only ever sees that one opaque wrapper, not one
// element per actual child, so there's nothing distinct to clone.
function renderNodeList(nodes, scope, trame) {
  if (nodes == null) return undefined;
  const list = Array.isArray(nodes) ? nodes : [nodes];
  return list.map((node, i) => (
    <TrameNodeOne key={computeNodeKey(node, scope, trame, i)} node={node} scope={scope} />
  ));
}

// `createElement(Component, props, childrenArray)` sets `props.children` to
// that ARRAY even when it holds exactly one element - fine for a host that
// reads React.Children as a list (the multi-child case renderNodeList's own
// comment above is about), but not for one that requires its single child to
// BE an element so it can React.cloneElement/isValidElement it directly (MUI
// Snackbar/Tooltip wrap their one child this way to attach a transition
// ref). A real single child stays a real single child; an empty or
// multi-item list is untouched.
function unwrapSingle(children) {
  return Array.isArray(children) && children.length === 1 ? children[0] : children;
}

function TrameNodeOne({ node, scope, ...extraProps }) {
  if (typeof node === "string") return node;
  if (isBindLeaf(node)) return <ExprLeaf jsExpression={node.js} scope={scope} />;
  if (!node || node.tag === undefined) return null;

  const { trame } = useTrame();
  const Component = resolveTag(node.tag);
  const { props } = useResolvedNode(node, scope);

  // A parent may have cloned this very element (React.cloneElement) to graft
  // its own props onto it - the pattern MUI's Tabs/RadioGroup/ButtonGroup
  // use on each of their `children` to inject `onClick`/`selected`/`checked`/
  // etc. React strips `key`/`ref` out before they ever reach here, so
  // `extraProps` only ever holds genuine DOM/component props, which take
  // precedence over this node's own resolved ones - matching cloneElement's
  // own "new props win" semantics. Note this only forwards props FORWARD
  // (into what actually renders); `child.props.*` read back by the parent
  // BEFORE cloning still sees this node's `{node, scope}`, not real ones -
  // components needing that instead (Select's synchronous `child.props.value`
  // reads) still need `literal_children` (resolveLiteralChildren.js).
  const mergedProps = { ...props, ...extraProps };

  if (isStructuralTag(node.tag)) {
    // Structural tags (ReactIf/ReactFor) get their raw, unresolved children +
    // the current scope as ordinary props - they control WHETHER and with
    // WHAT EXTENDED SCOPE their children render, which a pre-resolved child
    // element can't express.
    return createElement(Component, { ...mergedProps, rawChildren: node.children, scope });
  }

  // node.literalChildren (react.py's `literal_children` widget flag) is
  // static per tree position - like node.tag, it never toggles across
  // re-renders of the same node - so this conditional hook call is safe,
  // the same assumption the early returns above already make about a node's
  // shape being stable (see resolveLiteralChildren.js for why this exists).
  if (node.literalChildren) {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const literalChildren = useLiteralChildren(node.children, scope);
    return createElement(Component, mergedProps, unwrapSingle(literalChildren));
  }

  const children = node.children?.length
    ? unwrapSingle(renderNodeList(node.children, scope, trame))
    : undefined;
  return createElement(Component, mergedProps, children);
}

export default function TrameNode({ nodes, scope }) {
  const { trame } = useTrame();
  return renderNodeList(nodes, scope, trame) ?? null;
}
