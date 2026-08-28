import { useImperativeHandle, forwardRef } from "react";

// Exposes an imperative `exec` method (used by the server via js_call/refs).
import type { SlotFn } from "../types";

const TrameExec = forwardRef<
  any,
  { event?: unknown; onExec?: (arg: unknown) => void; slot?: SlotFn }
>(function TrameExec({ event, onExec, slot }, ref) {
  useImperativeHandle(ref, () => ({
    exec(arg?: unknown) {
      onExec?.(arg === undefined ? event : arg);
    },
  }));

  return slot ? slot() : null;
});

export default TrameExec;
