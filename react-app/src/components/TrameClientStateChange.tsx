import { useEffect, useRef } from "react";

import type { SlotFn } from "../types";

export default function TrameClientStateChange({
  value,
  immediate = false,
  triggerChangeOnCreate = false,
  onChange,
  slot,
}: {
  value?: unknown;
  immediate?: boolean;
  triggerChangeOnCreate?: boolean;
  onChange?: (value: unknown) => void;
  slot?: SlotFn;
}) {
  const first = useRef(true);

  useEffect(() => {
    if (first.current) {
      first.current = false;
      if (triggerChangeOnCreate) {
        onChange?.(value);
      }
      return;
    }
    if (immediate) {
      onChange?.(value);
    } else {
      const id = setTimeout(() => onChange?.(value), 0);
      return () => clearTimeout(id);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [value]);

  return slot ? slot() : null;
}
