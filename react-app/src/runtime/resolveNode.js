import { createElement, useMemo, useRef, useSyncExternalStore } from "react";
import { useTrame } from "./trameContext";
import { buildMergedScope, extendScope } from "./scope";
import { compile, createSnapshotCache, evalTracked } from "./expr";
import TrameNode from "../components/TrameNode.jsx";

// A dict-valued prop (e.g. `style={"color": react.Bind(...)}`, see
// react.py's HtmlElement._serialize_value) that mixes static entries with
// nested `{"js": ...}` markers - resolved as a unit below (one composite
// object per prop) rather than flattened into `reactive`, so its static
// entries survive untouched alongside the per-key reactive ones.
function isReactiveLeaf(value) {
  return value !== null && typeof value === "object" && "js" in value;
}

// Pure, non-hook classification of node.props - cheap object walk. Ordered
// by prop KEY first ("ref" is always a plain string, never wrapped), then by
// VALUE SHAPE (matching react-refs.md §5 / react-scoped-slots.md §4).
export function classifyProps(props) {
  const reactive = [];
  const callbacks = [];
  const slots = [];
  const composites = [];
  const static_ = [];
  let ref;

  Object.entries(props ?? {}).forEach(([key, value]) => {
    if (key === "ref") {
      ref = value;
      return;
    }
    if (value !== null && typeof value === "object" && !Array.isArray(value)) {
      if ("js" in value) {
        reactive.push([key, value.js]);
        return;
      }
      if ("callback" in value) {
        callbacks.push([key, value]);
        return;
      }
      if ("slot" in value) {
        slots.push([key, value.slot]);
        return;
      }
      const reactiveEntries = Object.entries(value).filter(([, v]) =>
        isReactiveLeaf(v),
      );
      if (reactiveEntries.length) {
        const staticEntries = Object.fromEntries(
          Object.entries(value).filter(([, v]) => !isReactiveLeaf(v)),
        );
        composites.push([key, { static: staticEntries, reactiveEntries }]);
        return;
      }
    }
    static_.push([key, value]);
  });

  return { reactive, callbacks, slots, composites, ref, static_ };
}

const MODIFIER_HANDLERS = {
  prevent: (e) => e.preventDefault(),
  stop: (e) => e.stopPropagation(),
};

export function makeCallbackHandler({ callback, modifiers }, scope, trame) {
  return (event) => {
    modifiers?.forEach((m) => MODIFIER_HANDLERS[m]?.(event));
    const merged = buildMergedScope(
      extendScope(scope, ["$event"], [event]),
      trame.state,
    );
    if ("js" in callback) {
      compile(callback.js)(merged);
      return;
    }
    const args = callback.args ? compile(callback.args.js)(merged) : [];
    const kwargs = callback.kwargs ? compile(callback.kwargs.js)(merged) : {};
    trame.trigger(callback.trigger, args, kwargs);
  };
}

function makeSlotRenderProp({ params, children }, scope) {
  return (...args) =>
    createElement(TrameNode, {
      nodes: children,
      scope: extendScope(scope, params, args),
    });
}

// The ONE hook-call-site per TrameNodeOne instance: always called the same
// way regardless of node shape (fixed sequence useTrame -> useMemo ->
// useSyncExternalStore -> useMemo), so it's safe under the Rules of Hooks
// and batches every reactive prop of a node into a single subscription
// instead of one per prop.
export function useResolvedNode(node, scope) {
  const { trame, getRefCallback } = useTrame();

  const { reactive, callbacks, slots, composites, ref, static_ } =
    classifyProps(node.props);

  const trackedKeys = useMemo(() => {
    const merged = buildMergedScope(scope, trame.state);
    const keys = new Set();
    reactive.forEach(([, expr]) =>
      evalTracked(expr, merged).keys.forEach((k) => keys.add(k)),
    );
    composites.forEach(([, { reactiveEntries }]) =>
      reactiveEntries.forEach(([, v]) =>
        evalTracked(v.js, merged).keys.forEach((k) => keys.add(k)),
      ),
    );
    return [...keys];
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [reactive, composites, scope, trame.state]);

  const snapshotCacheRef = useRef(null);
  if (snapshotCacheRef.current === null)
    snapshotCacheRef.current = createSnapshotCache();

  // One nested cache per composite prop key (e.g. "style"), reused across
  // calls - a bare `{...staticProps, ...evaluated}` object literal would be a
  // fresh reference on every getSnapshot() call even when nothing in it
  // changed, defeating snapshotCacheRef's own Object.is check on that key and
  // recreating exactly the infinite-render-loop risk createSnapshotCache
  // above exists to prevent.
  const compositeCachesRef = useRef(null);
  if (compositeCachesRef.current === null)
    compositeCachesRef.current = new Map();

  const reactiveValues = useSyncExternalStore(
    (onChange) => trame.state.watch(trackedKeys, onChange),
    () => {
      const merged = buildMergedScope(scope, trame.state);
      return snapshotCacheRef.current({
        ...Object.fromEntries(
          reactive.map(([key, expr]) => [key, evalTracked(expr, merged).value]),
        ),
        ...Object.fromEntries(
          composites.map(([key, { static: staticProps, reactiveEntries }]) => {
            let cache = compositeCachesRef.current.get(key);
            if (!cache) {
              cache = createSnapshotCache();
              compositeCachesRef.current.set(key, cache);
            }
            return [
              key,
              cache({
                ...staticProps,
                ...Object.fromEntries(
                  reactiveEntries.map(([subKey, v]) => [
                    subKey,
                    evalTracked(v.js, merged).value,
                  ]),
                ),
              }),
            ];
          }),
        ),
      });
    },
  );

  const callbackDepKey = callbacks
    .map(([k, v]) => k + JSON.stringify(v))
    .join("|");
  const callbackValues = useMemo(
    () =>
      Object.fromEntries(
        callbacks.map(([key, spec]) => [
          key,
          makeCallbackHandler(spec, scope, trame),
        ]),
      ),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [callbackDepKey, scope, trame],
  );

  const slotValues = Object.fromEntries(
    slots.map(([key, spec]) => [key, makeSlotRenderProp(spec, scope)]),
  );

  const props = {
    ...Object.fromEntries(static_),
    ...reactiveValues,
    ...callbackValues,
    ...slotValues,
  };
  if (ref) props.ref = getRefCallback(ref);
  return { props };
}
