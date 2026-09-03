import { describe, expect, it, vi } from "vitest";
import { compile, evalTracked } from "../../src/runtime/expr";
import { extendScope, buildMergedScope } from "../../src/runtime/scope";
import { createFakeTrame } from "../helpers/fakeTrame";

describe("compile", () => {
  it("reuses the cached Function for the same expression string", () => {
    const fn1 = compile("1 + 1");
    const fn2 = compile("1 + 1");
    expect(fn1).toBe(fn2);
  });

  it("compiles distinct expression strings to distinct functions", () => {
    const fn1 = compile("1 + 1");
    const fn2 = compile("2 + 2");
    expect(fn1).not.toBe(fn2);
  });
});

describe("evalTracked", () => {
  it("evaluates the expression against the merged scope", () => {
    const { trame } = createFakeTrame({ count: 5 });
    const merged = buildMergedScope(undefined, trame.state);
    const { value } = evalTracked("count + 1", merged);
    expect(value).toBe(6);
  });

  it("records only identifiers actually read", () => {
    const { trame } = createFakeTrame({ a: 1, b: 2, c: 3 });
    const merged = buildMergedScope(undefined, trame.state);
    const { keys } = evalTracked("a + b", merged);
    expect(keys.sort()).toEqual(["a", "b"]);
  });

  it("a ternary only tracks its taken branch", () => {
    const { trame } = createFakeTrame({ mode: "a", x: 1, y: 2 });
    const merged = buildMergedScope(undefined, trame.state);
    const { keys } = evalTracked('mode === "a" ? x : y', merged);
    expect(keys.sort()).toEqual(["mode", "x"]);
  });

  it("a scope-chain local shadowing a same-named state key is never tracked as a state dependency", () => {
    const { trame } = createFakeTrame({ count: 100 });
    const scope = extendScope(undefined, ["count"], ["local-value"]);
    const merged = buildMergedScope(scope, trame.state);
    const { value, keys } = evalTracked("count", merged);

    expect(value).toBe("local-value");
    expect(keys).toEqual([]);
  });

  it("state.watch only fires for keys the expression actually reads", () => {
    const { trame, setState } = createFakeTrame({ a: 1, b: 2 });
    const merged = buildMergedScope(undefined, trame.state);
    const { keys } = evalTracked("a", merged);

    const onChange = vi.fn();
    trame.state.watch(keys, onChange);
    onChange.mockClear();

    setState({ b: 20 });
    expect(onChange).not.toHaveBeenCalled();

    setState({ a: 10 });
    expect(onChange).toHaveBeenCalledTimes(1);
  });
});
