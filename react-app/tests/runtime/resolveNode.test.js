import { describe, expect, it, vi } from "vitest";
import {
  classifyProps,
  makeCallbackHandler,
} from "../../src/runtime/resolveNode";
import { createFakeTrame } from "../helpers/fakeTrame";

describe("classifyProps", () => {
  it("splits a dict-valued prop mixing static entries with {js: ...} leaves into `composites`, leaving other props alone", () => {
    const { reactive, composites, static_ } = classifyProps({
      style: { fontWeight: "bold", color: { js: "color" } },
      title: "hi",
      value: { js: "count" },
    });

    expect(reactive).toEqual([["value", "count"]]);
    expect(static_).toEqual([["title", "hi"]]);
    expect(composites).toEqual([
      [
        "style",
        {
          static: { fontWeight: "bold" },
          reactiveEntries: [["color", { js: "color" }]],
        },
      ],
    ]);
  });

  it("treats a fully-static dict-valued prop as static, not a composite", () => {
    const { composites, static_ } = classifyProps({
      style: { fontWeight: "bold", color: "red" },
    });

    expect(composites).toEqual([]);
    expect(static_).toEqual([["style", { fontWeight: "bold", color: "red" }]]);
  });
});

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
