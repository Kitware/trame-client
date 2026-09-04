import { useEffect, useImperativeHandle } from "react";

// Port of vue3-app/src/components/TrameClientTriggers.js. `events` collects
// every non-ref prop by name - both the "built-in" ones (mounted, created,
// beforeDestroy, beforeUnmount, exit) and any arbitrary custom topic name a
// caller declared - so a single generic `emit(topic, event)` (exposed for
// server-triggered `.call(method, *args)` dispatch via js-lib's ref-action
// mechanism) can fire either kind the same way vue's `emit()` does.
export default function TrameClientTriggers({ ref, children, ...events }) {
  useImperativeHandle(
    ref,
    () => ({
      emit: (topic, event) => events[topic]?.(event),
    }),
    [events],
  );

  useEffect(() => {
    events.created?.();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    events.mounted?.();
    return () => {
      events.beforeDestroy?.();
      events.beforeUnmount?.();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    function onExit() {
      events.exit?.();
    }
    window.addEventListener("beforeunload", onExit);
    return () => window.removeEventListener("beforeunload", onExit);
  }, [events.exit]);

  return children ?? null;
}
