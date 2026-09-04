import { useEffect, useRef } from "react";
import { useTrame } from "../runtime/trameContext";

// Port of vue3-app/src/components/TrameSizeObserver.js: wraps children in a
// full-size container, observes its own size via ResizeObserver, and writes
// {x, y, width, height, pixelRatio, dpi} directly into trame state under the
// bound `name` on every resize (no need to also wire a change-event prop -
// callers just watch the resulting state key, matching the python side,
// which never registers a "change" event for this widget either).
export default function TrameSizeObserver({ name, children }) {
  const { trame } = useTrame();
  const elRef = useRef(null);

  useEffect(() => {
    if (!elRef.current) return undefined;

    const resize = () => {
      const { x, y, width, height } = elRef.current.getBoundingClientRect();
      const pixelRatio = window.devicePixelRatio;
      const dpi = 96 * pixelRatio;
      const event = { size: { x, y, width, height }, pixelRatio, dpi };
      if (name) event.name = name;
      trame.state.set(name, event);
    };

    const observer = new ResizeObserver(resize);
    observer.observe(elRef.current);
    return () => observer.disconnect();
  }, [name, trame]);

  return (
    <div
      ref={elRef}
      style={{
        overflow: "hidden",
        position: "relative",
        width: "100%",
        height: "100%",
        margin: 0,
        padding: 0,
      }}
    >
      {children}
    </div>
  );
}
