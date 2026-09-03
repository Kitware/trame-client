import { createElement, useMemo, useRef, useSyncExternalStore } from "react";
import { useTrame } from "./trameContext";
import { buildMergedScope, extendScope } from "./scope";
import { compile, createSnapshotCache, evalTracked } from "./expr";
import TrameNode from "../components/TrameNode.jsx";

// Pure, non-hook classification of node.props - cheap object walk. Ordered
// by prop KEY first ("ref" is always a plain string, never wrapped), then by
// VALUE SHAPE (matching react-refs.md §5 / react-scoped-slots.md §4).
function classifyProps(props) {
  const reactive = [];
  const callbacks = [];
  const slots = [];
  const static_ = [];
  let ref;

  Object.entries(props ?? {}).forEach(([key, value]) => {
    if (key === "ref") {
      ref = value;
      return;
    }
    if (value !== null && typeof value === "object") {
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
    }
    static_.push([key, value]);
  });

  return { reactive, callbacks, slots, ref, static_ };
}

const MODIFIER_HANDLERS = {
  prevent: (e) => e.preventDefault(),
  stop: (e) => e.stopPropagation(),
};

export function makeCallbackHandler({ callback, modifiers }, scope, trame) {
  return (event) => {
    modifiers?.forEach((m) => MODIFIER_HANDLERS[m]?.(event));
    const merged = buildMergedScope(
      extendScope(scope, ["e"], [event]),
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

  const { reactive, callbacks, slots, ref, static_ } = classifyProps(
    node.props,
  );

  const trackedKeys = useMemo(() => {
    const merged = buildMergedScope(scope, trame.state);
    const keys = new Set();
    reactive.forEach(([, expr]) =>
      evalTracked(expr, merged).keys.forEach((k) => keys.add(k)),
    );
    return [...keys];
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [reactive, scope, trame.state]);

  const snapshotCacheRef = useRef(null);
  if (snapshotCacheRef.current === null)
    snapshotCacheRef.current = createSnapshotCache();

  const reactiveValues = useSyncExternalStore(
    (onChange) => trame.state.watch(trackedKeys, onChange),
    () =>
      snapshotCacheRef.current(
        Object.fromEntries(
          reactive.map(([key, expr]) => [
            key,
            evalTracked(expr, buildMergedScope(scope, trame.state)).value,
          ]),
        ),
      ),
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
