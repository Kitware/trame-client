import { useEffect, useRef } from "react";
import { useTrame } from "../renderer/hooks";

import type { SlotFn } from "../types";

export default function TrameSizeObserver({
  name,
  onChange,
  slot,
}: {
  name?: string;
  onChange?: (event: unknown) => void;
  slot?: SlotFn;
}) {
  const trame = useTrame();
  const elem = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    function resize() {
      if (!elem.current) return;
      const { x, y, width, height } = elem.current.getBoundingClientRect();
      const size = { x, y, width, height };
      const pixelRatio = window.devicePixelRatio;
      const dpi = 96 * pixelRatio;
      const event: Record<string, unknown> = { size, pixelRatio, dpi };
      if (name) {
        event.name = name;
      }
      if (trame && name) {
        trame.state.set(name, event);
      }
      onChange?.(event);
    }

    const sizeObserver = new ResizeObserver(resize);
    sizeObserver.observe(elem.current as Element);
    return () => sizeObserver.disconnect();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [name]);

  return (
    <div
      ref={elem}
      style={{
        overflow: "hidden",
        position: "relative",
        width: "100%",
        height: "100%",
        margin: 0,
        padding: 0,
      }}
    >
      {slot ? slot() : null}
    </div>
  );
}
