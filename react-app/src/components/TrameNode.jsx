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

function TrameNodeOne({ node, scope }) {
  if (typeof node === "string") return node;
  if (isBindLeaf(node)) return <ExprLeaf jsExpression={node.js} scope={scope} />;
  if (!node || node.tag === undefined) return null;

  const Component = resolveTag(node.tag);
  const { props } = useResolvedNode(node, scope);

  if (isStructuralTag(node.tag)) {
    // Structural tags (ReactIf/ReactFor) get their raw, unresolved children +
    // the current scope as ordinary props - they control WHETHER and with
    // WHAT EXTENDED SCOPE their children render, which a pre-resolved child
    // element can't express.
    return createElement(Component, { ...props, rawChildren: node.children, scope });
  }

  // node.literalChildren (react.py's `literal_children` widget flag) is
  // static per tree position - like node.tag, it never toggles across
  // re-renders of the same node - so this conditional hook call is safe,
  // the same assumption the early returns above already make about a node's
  // shape being stable (see resolveLiteralChildren.js for why this exists).
  if (node.literalChildren) {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const literalChildren = useLiteralChildren(node.children, scope);
    return createElement(Component, props, literalChildren);
  }

  const children = node.children?.length
    ? createElement(TrameNode, { nodes: node.children, scope })
    : undefined;
  return createElement(Component, props, children);
}

export default function TrameNode({ nodes, scope }) {
  const { trame } = useTrame();
  if (nodes == null) return null;
  const list = Array.isArray(nodes) ? nodes : [nodes];
  return list.map((node, i) => (
    <TrameNodeOne key={computeNodeKey(node, scope, trame, i)} node={node} scope={scope} />
  ));
}
