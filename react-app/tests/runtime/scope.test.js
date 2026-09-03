import { describe, expect, it } from "vitest";
import {
  extendScope,
  buildMergedScope,
  hasOwnLocal,
} from "../../src/runtime/scope";
import { createFakeTrame } from "../helpers/fakeTrame";

describe("scope", () => {
  it("extendScope nesting (For inside For) preserves shadowing", () => {
    const outer = extendScope(undefined, ["item"], ["outer-item"]);
    const inner = extendScope(outer, ["item"], ["inner-item"]);

    expect(inner.item).toBe("inner-item");
    expect(outer.item).toBe("outer-item");
  });

  it("extendScope nesting (Slot inside For) preserves shadowing", () => {
    const forScope = extendScope(undefined, ["row"], [{ id: 1 }]);
    const slotScope = extendScope(forScope, ["cell"], ["cell-value"]);

    expect(slotScope.cell).toBe("cell-value");
    expect(slotScope.row).toEqual({ id: 1 });
  });

  it("hasOwnLocal finds a local scope variable and stops at the state facade sentinel", () => {
    const { trame } = createFakeTrame({ count: 1 });
    const scope = extendScope(undefined, ["count"], ["shadowed"]);
    const merged = buildMergedScope(scope, trame.state);

    expect(hasOwnLocal(merged, "count")).toBe(true);
    expect(hasOwnLocal(merged, "somethingElse")).toBe(false);
  });

  it("buildMergedScope falls back to trame state for names not in the local chain", () => {
    const { trame } = createFakeTrame({ count: 42 });
    const merged = buildMergedScope(undefined, trame.state);

    expect(merged.count).toBe(42);
  });

  it("a scope-chain local shadowing a same-named state key wins over state", () => {
    const { trame } = createFakeTrame({ count: 1 });
    const scope = extendScope(undefined, ["count"], ["shadowed"]);
    const merged = buildMergedScope(scope, trame.state);

    expect(merged.count).toBe("shadowed");
  });

  it("buildMergedScope preserves an outer For's loop variable through a nested Slot frame", () => {
    const { trame } = createFakeTrame({ count: 1 });
    const forScope = extendScope(undefined, ["row"], [{ id: 7 }]);
    const slotScope = extendScope(forScope, ["cell"], ["cell-value"]);
    const merged = buildMergedScope(slotScope, trame.state);

    expect(merged.cell).toBe("cell-value");
    expect(merged.row).toEqual({ id: 7 });
    expect(merged.count).toBe(1);
  });

  it("hasOwnLocal detects an outer For's loop variable through a nested Slot frame", () => {
    const { trame } = createFakeTrame({ count: 1 });
    const forScope = extendScope(undefined, ["row"], [{ id: 7 }]);
    const slotScope = extendScope(forScope, ["cell"], ["cell-value"]);
    const merged = buildMergedScope(slotScope, trame.state);

    expect(hasOwnLocal(merged, "row")).toBe(true);
    expect(hasOwnLocal(merged, "cell")).toBe(true);
    expect(hasOwnLocal(merged, "count")).toBe(false);
  });
});
