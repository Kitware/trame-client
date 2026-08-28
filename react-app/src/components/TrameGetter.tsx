import { useTrame, useTrameState } from "../renderer/hooks";

import type { SlotFn } from "../types";

export default function TrameGetter({
  name,
  slot,
}: {
  name: string;
  slot?: SlotFn;
}) {
  const trame = useTrame();
  useTrameState(); // `name` can be an expression over arbitrary state

  const value = trame.state.get(name);

  function update(newValue: unknown) {
    trame.state.set(name, newValue);
  }

  function updateNested(key: string, newValue: unknown) {
    const newData = JSON.parse(JSON.stringify(trame.state.get(name)));
    let current = newData;
    const steps = String(key).split(".");
    for (let i = 0; i < steps.length - 1; i++) {
      current = current[steps[i]];
    }
    current[steps.at(-1) as string] = newValue;
    trame.state.set(name, newData);
  }

  return slot
    ? slot({ keyName: name, value, update, updateNested })
    : null;
}
