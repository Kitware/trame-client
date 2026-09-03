import { hasOwnLocal } from "./scope";

// expression string -> Function, never evicted (finite, server-authored set)
const compiledCache = new Map();

export function compile(jsExpression) {
  let fn = compiledCache.get(jsExpression);
  if (!fn) {
    // eslint-disable-next-line no-new-func -- same trust model Vue's compiled
    // templates already accept: expression strings are server/app-author-controlled.
    fn = new Function("scope", `with (scope) { return (${jsExpression}); }`);
    compiledCache.set(jsExpression, fn);
  }
  return fn;
}

// Valtio-style dependency tracking via a Proxy: forces every free identifier
// referenced by the expression through `get`, recording it unless it resolves
// to a local (For/Slot-introduced) scope variable rather than trame state.
export function evalTracked(jsExpression, mergedScope) {
  const tracked = new Set();
  const proxy = new Proxy(mergedScope, {
    // Only claims identifiers actually resolvable in mergedScope (a local
    // frame binding, or an existing trame state key) - anything else (a
    // real global like `Math`) must fall through to the outer/global scope,
    // which only happens if `has` says "no" for it.
    has(target, prop) {
      return (
        typeof prop === "string" &&
        (hasOwnLocal(target, prop) || target[prop] !== undefined)
      );
    },
    get(target, prop) {
      if (typeof prop === "string" && !hasOwnLocal(target, prop)) {
        tracked.add(prop);
      }
      return target[prop];
    },
  });
  const value = compile(jsExpression)(proxy);
  return { value, keys: [...tracked] };
}

// useSyncExternalStore requires getSnapshot() to return a referentially
// stable value when nothing actually changed (React compares snapshots via
// Object.is and re-renders - and re-invokes getSnapshot - whenever they
// differ) - a fresh `Object.fromEntries(...)` on every call would never be
// Object.is-equal to the previous one, causing an infinite render loop. This
// caches the last snapshot and reuses its reference whenever every field is
// still Object.is-equal to what it held before (primitives compare by value
// so pass through unchanged; object/array-valued fields compare by
// reference, which is stable as long as the underlying state value wasn't
// reassigned).
export function createSnapshotCache() {
  let cached;
  return (next) => {
    if (
      cached !== undefined &&
      typeof next === "object" &&
      next !== null &&
      typeof cached === "object" &&
      cached !== null &&
      Object.keys(cached).length === Object.keys(next).length &&
      Object.keys(next).every((k) => Object.is(cached[k], next[k]))
    ) {
      return cached;
    }
    cached = next;
    return cached;
  };
}
