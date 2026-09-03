import { vi } from "vitest";

/**
 * Minimal fake `trame` object exposing only what react-app's runtime touches
 * (`trame.state.get`/`.watch`, `trame.refs`, `trame.trigger`) - mirrors real
 * `State.watch` behavior (js-lib/src/state.ts): calling the watcher
 * immediately with current values on subscribe, and again whenever one of
 * its watched keys changes.
 */
export function createFakeTrame(initialState = {}) {
  const state = { ...initialState };
  const watchers = [];

  function notify(changedKeys) {
    watchers.forEach(({ keys, fn }) => {
      if (changedKeys.some((k) => keys.has(k))) fn();
    });
  }

  const trameState = {
    get: (key) => (key === undefined ? state : state[key]),
    set: (key, value) => {
      state[key] = value;
      notify([key]);
    },
    watch: (keys, fn) => {
      const entry = { keys: new Set(keys), fn };
      watchers.push(entry);
      fn(...keys.map((k) => state[k]));
      return () => {
        const idx = watchers.indexOf(entry);
        if (idx >= 0) watchers.splice(idx, 1);
      };
    },
  };

  const trame = {
    state: trameState,
    refs: {},
    trigger: vi.fn(),
  };

  return {
    trame,
    setState(partial) {
      Object.assign(state, partial);
      notify(Object.keys(partial));
    },
  };
}
