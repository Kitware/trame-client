import { createElement, useMemo, useRef, useSyncExternalStore } from "react";
import { useTrame } from "./trameContext";
import { buildMergedScope } from "./scope";
import { compile, createSnapshotCache, evalTracked } from "./expr";
import { resolveTag, isStructuralTag } from "./tags";
import { classifyProps, makeCallbackHandler } from "./resolveNode";
// Same TrameNode.jsx <-> runtime cycle resolveNode.js already has for Slot
// rendering; safe because neither side is touched until render time, well
// after module evaluation.
import TrameNode from "../components/TrameNode.jsx";

/*
 * Support for `node.literalChildren` (set by react.py's `literal_children`
 * widget flag - trame-mui sets it on Select/Tabs/RadioGroup/...): those
 * components read `child.props.value` / `child.props.children` straight off
 * their `children` array via `React.Children`, synchronously, before
 * anything renders. The usual per-node <TrameNodeOne> wrapper (TrameNode.jsx)
 * defeats that, since those props would live on the wrapper instead of on a
 * real `<MenuItem>` element.
 *
 * This resolves a node's DIRECT children eagerly into literal elements of
 * their real component type instead - only one level deep. Each resolved
 * child's own GRANDchildren still render through the normal <TrameNode>
 * wrapper and keep their own fine-grained reactivity (see
 * react-fine-grained-reactivity.md); only the direct children's own props
 * become one shared subscription (watching the union of every key they
 * read), since the library only ever inspects that one level.
 *
 * react.For/react.If aren't supported as a direct child here - a
 * dynamically-sized/conditional list of real elements can't come out of a
 * single eager walk - such a node is skipped with a warning.
 */

function isBindLeaf(node) {
  return (
    node !== null &&
    typeof node === "object" &&
    !Array.isArray(node) &&
    "js" in node
  );
}

function walkTrackedKeys(node, mergedScope, keys) {
  if (!node || typeof node !== "object" || node.tag === undefined) return;
  if (isStructuralTag(node.tag)) return;

  Object.values(node.props ?? {}).forEach((value) => {
    if (isBindLeaf(value)) {
      evalTracked(value.js, mergedScope).keys.forEach((k) => keys.add(k));
    }
  });
}

function shallowEqual(a, b) {
  if (a === b) return true;
  const aKeys = Object.keys(a);
  const bKeys = Object.keys(b);
  if (aKeys.length !== bKeys.length) return false;
  return aKeys.every((k) => Object.is(a[k], b[k]));
}

// ctx.elementCache/ctx.callbackCache persist (via useRef) across
// getSnapshot() calls so an unchanged child keeps returning the SAME element
// reference - required for useSyncExternalStore's "cached snapshot"
// contract, not just an optimization: a fresh element every call reads as
// "the store changed" on every render, forcing React into a synchronous
// re-render loop.
function resolveLiteralChild(node, ctx, path) {
  if (typeof node === "string") return node;
  if (node === null || node === undefined) return null;
  if (isBindLeaf(node)) return compile(node.js)(ctx.mergedScope);
  if (node.tag === undefined) return null;
  if (isStructuralTag(node.tag)) {
    console.warn(
      `TrameNode: "${node.tag}" isn't supported as a direct child of a literalChildren node, skipping`,
    );
    return null;
  }

  const Component = resolveTag(node.tag);
  const { reactive, callbacks, ref, static_ } = classifyProps(node.props);

  const props = Object.fromEntries(static_);
  reactive.forEach(([key, expr]) => {
    props[key] = compile(expr)(ctx.mergedScope);
  });
  callbacks.forEach(([key, spec]) => {
    const cacheKey = `${path}#${key}`;
    const depKey = JSON.stringify(spec);
    const cached = ctx.callbackCache.get(cacheKey);
    const handler =
      cached && cached.depKey === depKey
        ? cached.handler
        : makeCallbackHandler(spec, ctx.scope, ctx.trame);
    ctx.callbackCache.set(cacheKey, { depKey, handler });
    props[key] = handler;
  });
  if (ref) props.ref = ctx.getRefCallback(ref);

  const cached = ctx.elementCache.get(path);
  if (
    cached &&
    cached.type === Component &&
    shallowEqual(cached.props, props)
  ) {
    return cached.element;
  }

  const children = node.children?.length
    ? createElement(TrameNode, { nodes: node.children, scope: ctx.scope })
    : undefined;

  const element = createElement(Component, { ...props, key: path }, children);
  ctx.elementCache.set(path, { type: Component, props, element });
  return element;
}

export function useLiteralChildren(nodes, scope) {
  const { trame, getRefCallback } = useTrame();
  const list = Array.isArray(nodes) ? nodes : nodes ? [nodes] : [];

  const trackedKeys = useMemo(() => {
    const merged = buildMergedScope(scope, trame.state);
    const keys = new Set();
    list.forEach((node) => walkTrackedKeys(node, merged, keys));
    return [...keys];
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [list, scope, trame.state]);

  const elementCacheRef = useRef(null);
  if (elementCacheRef.current === null) elementCacheRef.current = new Map();
  const callbackCacheRef = useRef(null);
  if (callbackCacheRef.current === null) callbackCacheRef.current = new Map();
  const snapshotCacheRef = useRef(null);
  if (snapshotCacheRef.current === null)
    snapshotCacheRef.current = createSnapshotCache();

  return useSyncExternalStore(
    (onChange) => trame.state.watch(trackedKeys, onChange),
    () => {
      const ctx = {
        scope,
        trame,
        getRefCallback,
        mergedScope: buildMergedScope(scope, trame.state),
        elementCache: elementCacheRef.current,
        callbackCache: callbackCacheRef.current,
      };
      return snapshotCacheRef.current(
        list.map((node, i) => resolveLiteralChild(node, ctx, String(i))),
      );
    },
  );
}
