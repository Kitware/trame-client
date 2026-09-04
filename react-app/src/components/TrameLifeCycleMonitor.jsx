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

// Port of vue3-app/src/components/TrameLifeCycleMonitor.js. React function
// components have no separate before/after hook for mount or destroy (only
// one commit point each), so - matching how TrameClientTriggers already
// conflates beforeDestroy/beforeUnmount at its single unmount point -
// created/beforeMount fire together (synchronously, during first render) and
// beforeDestroy/destroyed fire together (at unmount cleanup). beforeUpdate/
// updated fire together on every re-render after the first.
export default function TrameLifeCycleMonitor({
  name = "LifeCycleMonitor",
  type = "log",
  value = "value",
  events = DEFAULT_EVENTS,
  children,
  ...topicHandlers
}) {
  const fire = (topicName) => {
    if (!events.includes(topicName)) return;
    if (type === "emit") {
      topicHandlers[topicName]?.({ name, value });
    } else {
      // eslint-disable-next-line no-console
      console[type]?.(name, topicName, value);
    }
  };

  const isFirstRenderRef = useRef(true);
  if (isFirstRenderRef.current) {
    isFirstRenderRef.current = false;
    fire("created");
    fire("beforeMount");
  } else {
    fire("beforeUpdate");
  }

  // Runs once per actual mount/unmount (never re-runs on prop changes).
  useEffect(() => {
    fire("mounted");
    return () => {
      fire("beforeDestroy");
      fire("destroyed");
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Runs after every commit; the first commit is "mounted" (already fired
  // above), so only count "updated" from the second commit onward.
  const commitCount = useRef(0);
  useEffect(() => {
    commitCount.current += 1;
    if (commitCount.current > 1) fire("updated");
  });

  return children ?? null;
}
