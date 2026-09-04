import { useImperativeHandle } from "react";

// Port of vue3-app/src/components/TrameExec.js: exposes an imperative
// `exec(arg)` method (invoked server-side via `server.js_call(ref, "exec",
// ...)`, dispatched client-side through the generic ref-action mechanism in
// js-lib's Trame class) - calling it with no argument fires `onExec` with
// the bound `event` prop's current value, calling it with an argument fires
// `onExec` with that argument instead.
export default function TrameJSEval({ event, onExec, ref, children }) {
  useImperativeHandle(
    ref,
    () => ({
      exec: (arg) => onExec?.(arg === undefined ? event : arg),
    }),
    [event, onExec],
  );

  return children ?? null;
}
