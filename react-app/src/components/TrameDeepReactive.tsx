import { useRef } from "react";
import { useTrame, useTrameState } from "../renderer/hooks";

// Two-way binding of a nested state structure. The slot receives a proxied
// `value`: reading is live, and any nested mutation is pushed to the server.
import type { SlotFn } from "../types";

export default function TrameDeepReactive({
  name,
  slot,
}: {
  name: string;
  slot?: SlotFn;
}) {
  const trame = useTrame();
  useTrameState([name]);
  const pending = useRef<ReturnType<typeof setTimeout> | null>(null);

  function makeProxy(target: any, root: any): any {
    if (target === null || typeof target !== "object") return target;
    return new Proxy(target, {
      get(obj: any, key: string) {
        return makeProxy(obj[key], root);
      },
      set(obj: any, key: string, newValue: unknown) {
        obj[key] = newValue;
        // push a deep copy of the whole structure
        if (!pending.current) {
          pending.current = setTimeout(() => {
            pending.current = null;
            trame.state.set(name, JSON.parse(JSON.stringify(root)));
          }, 0);
        }
        return true;
      },
    });
  }

  const raw = JSON.parse(JSON.stringify(trame.state.get(name) ?? {}));
  const value = makeProxy(raw, raw);

  return slot ? slot({ value }) : null;
}
