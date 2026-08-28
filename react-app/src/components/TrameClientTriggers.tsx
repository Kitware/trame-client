import { useEffect, useImperativeHandle, useRef, forwardRef } from "react";

// Server can call `emit(topic, event)` on this component through js_call/refs.
import type { SlotFn } from "../types";

type Props = { slot?: SlotFn } & Record<string, any>;

const TrameClientTriggers = forwardRef<any, Props>(function TrameClientTriggers(
  { slot, ...props },
  ref,
) {
  const propsRef = useRef(props);
  propsRef.current = props;

  function emitTopic(topic: string, event?: unknown) {
    const handler = propsRef.current[`on${topic[0].toUpperCase()}${topic.slice(1)}`];
    handler?.(event);
  }

  useImperativeHandle(ref, () => ({ emit: emitTopic }));

  useEffect(() => {
    emitTopic("created");
    emitTopic("mounted");
    const onExit = () => emitTopic("exit");
    window.addEventListener("beforeunload", onExit);
    return () => {
      emitTopic("beforeDestroy");
      emitTopic("beforeUnmount");
      window.removeEventListener("beforeunload", onExit);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return slot ? slot() : null;
});

export default TrameClientTriggers;
