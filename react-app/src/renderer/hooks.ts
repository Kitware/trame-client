// React hooks bridging the trame shared state to component re-renders.

import {
  createContext,
  useCallback,
  useContext,
  useRef,
  useSyncExternalStore,
} from "react";

import type { TrameInstance, TrameStateEvent } from "../types";

export const TrameContext = createContext<TrameInstance | null>(null);

export function useTrame(): TrameInstance {
  const trame = useContext(TrameContext);
  if (!trame) {
    throw new Error("useTrame must be used inside <TrameContext.Provider>");
  }
  return trame;
}

// Re-render when any watched state key becomes dirty.
// keys === null -> re-render on every dirty-state event (template-level).
export function useTrameState(keys: string[] | null = null): number {
  const trame = useTrame();
  const versionRef = useRef(0);
  const keyList = keys ? keys.join(",") : null;

  const subscribe = useCallback(
    (onStoreChange: () => void) => {
      const keySet = keyList !== null ? new Set(keyList.split(",")) : null;
      const listener = ({ type, keys: dirtyKeys }: TrameStateEvent) => {
        if (type !== "dirty-state" && type !== "new-keys") return;
        if (!keySet || dirtyKeys?.some((k) => keySet.has(k))) {
          versionRef.current += 1;
          onStoreChange();
        }
      };
      trame.state.addListener(listener);
      return () => trame.state.removeListener(listener);
    },
    [trame, keyList],
  );

  return useSyncExternalStore(subscribe, () => versionRef.current);
}

// Subscribe to a single state value.
export function useTrameValue(name: string): unknown {
  const trame = useTrame();
  useTrameState([name]);
  return trame.state.get(name);
}
