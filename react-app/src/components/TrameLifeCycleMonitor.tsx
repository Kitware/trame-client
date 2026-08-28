import { useEffect, useRef } from "react";

const DEFAULT_EVENTS = [
  "created",
  "beforeMount",
  "mounted",
  "beforeUpdate",
  "updated",
  "beforeDestroy",
  "destroyed",
];

import type { SlotFn } from "../types";

export default function TrameLifeCycleMonitor({
  name = "LifeCycleMonitor",
  type = "log",
  value = "value",
  events = DEFAULT_EVENTS,
  slot,
  ...handlers
}: {
  name?: string;
  type?: string;
  value?: string;
  events?: string[];
  slot?: SlotFn;
} & Record<string, any>) {
  const mounted = useRef(false);

  function notify(eventName: string) {
    if (!events.includes(eventName)) return;
    if (type === "emit") {
      const handler =
        handlers[`on${eventName[0].toUpperCase()}${eventName.slice(1)}`];
      handler?.({ name, value });
    } else {
      (console as any)[type](name, eventName, value);
    }
  }

  // created / beforeMount happen before the first paint in React terms
  if (!mounted.current) {
    notify("created");
    notify("beforeMount");
  }

  useEffect(() => {
    mounted.current = true;
    notify("mounted");
    return () => {
      notify("beforeDestroy");
      notify("destroyed");
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (mounted.current) {
      notify("updated");
    }
  });

  return slot ? slot() : null;
}
