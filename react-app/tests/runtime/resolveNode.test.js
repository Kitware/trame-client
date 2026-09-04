import { describe, expect, it, vi } from "vitest";
import { makeCallbackHandler } from "../../src/runtime/resolveNode";
import { createFakeTrame } from "../helpers/fakeTrame";

function fakeEvent(value) {
  return {
    target: { value },
    preventDefault: vi.fn(),
    stopPropagation: vi.fn(),
  };
}

describe("makeCallbackHandler", () => {
  it("calls trame.trigger with correctly-evaluated args/kwargs", () => {
    const { trame } = createFakeTrame();
    const handler = makeCallbackHandler(
      { callback: { trigger: "foo", args: { js: "[$event.target.value]" } } },
      undefined,
      trame,
    );

    handler(fakeEvent("hello"));

    expect(trame.trigger).toHaveBeenCalledWith("foo", ["hello"], {});
  });

  it("evaluates a plain js callback expression against the merged scope", () => {
    const { trame, setState } = createFakeTrame({ count: 1 });
    const handler = makeCallbackHandler(
      { callback: { js: "count = Number($event.target.value)" } },
      undefined,
      trame,
    );

    handler(fakeEvent("7"));

    expect(trame.state.get("count")).toBe(7);
    // sanity: setState helper still works independently of the handler
    setState({ count: 9 });
    expect(trame.state.get("count")).toBe(9);
  });

  it("modifiers:['prevent'] calls event.preventDefault()", () => {
    const { trame } = createFakeTrame();
    const handler = makeCallbackHandler(
      { callback: { trigger: "foo" }, modifiers: ["prevent"] },
      undefined,
      trame,
    );
    const event = fakeEvent();

    handler(event);

    expect(event.preventDefault).toHaveBeenCalled();
  });

  it("modifiers:['stop'] calls event.stopPropagation()", () => {
    const { trame } = createFakeTrame();
    const handler = makeCallbackHandler(
      { callback: { trigger: "foo" }, modifiers: ["stop"] },
      undefined,
      trame,
    );
    const event = fakeEvent();

    handler(event);

    expect(event.stopPropagation).toHaveBeenCalled();
  });
});
