import { useEffect, useRef } from "react";

// Port of vue3-app/src/components/TrameClientStateChange.js. `value` arrives
// already resolved (react.Bind, evaluated reactively by useResolvedNode), so
// this only needs to notice when it changes. `immediate` (sync vs. Vue's
// nextTick emission) has no meaningful react equivalent - useEffect already
// defers to after commit either way - so it's accepted but unused here;
// `triggerChangeOnCreate` fires `onChange` once on mount, before any change.
export default function TrameClientStateChange({
  value,
  triggerChangeOnCreate,
  onChange,
  children,
}) {
  const isFirst = useRef(true);

  useEffect(() => {
    if (isFirst.current) {
      isFirst.current = false;
      if (triggerChangeOnCreate) onChange?.(value);
      return;
    }
    onChange?.(value);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [value]);

  return children ?? null;
}
