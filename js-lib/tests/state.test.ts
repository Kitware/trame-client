import { describe, expect, it, vi } from "vitest";
import { State } from "../src/state";
import { createFakeClient } from "./helpers/fakeClient";

async function makeState(initialServerState: Record<string, any> = {}) {
  const fake = createFakeClient(initialServerState);
  // Mirrors real usage: Trame always connects the client before creating State.
  await fake.client.connect({});
  const state = new State(fake.client as any);
  return { state, fake };
}

describe("State", () => {
  it("loads its initial content from the server", async () => {
    const { state } = await makeState({ a: 1, b: 2 });
    await state.loadState();

    expect(state.get("a")).toBe(1);
    expect(state.get("b")).toBe(2);
    expect(state.getAllKeys().sort()).toEqual(["a", "b"]);
  });

  it("set() updates locally and pushes to the server (README: state.set)", async () => {
    const { state, fake } = await makeState();
    await state.loadState();

    await state.set("a", 5);

    expect(state.get("a")).toBe(5);
    expect(fake.getServerState().a).toBe(5);
  });

  it("get() returns undefined for keys that were never set (README: state.get('b'))", async () => {
    const { state } = await makeState();
    await state.loadState();

    expect(state.get("b")).toBeUndefined();
  });

  it("get() with no key returns the full state object", async () => {
    const { state } = await makeState({ a: 1 });
    await state.loadState();

    expect(state.get()).toMatchObject({ a: 1 });
  });

  it("update() applies several key/value pairs at once (README: state.update)", async () => {
    const { state, fake } = await makeState();
    await state.loadState();

    await state.update({ a: 1, b: 2 });

    expect(state.get("a")).toBe(1);
    expect(state.get("b")).toBe(2);
    expect(fake.getServerState()).toMatchObject({ a: 1, b: 2 });
  });

  it("watch() calls back immediately and on every dependency change (README: state.watch)", async () => {
    const { state } = await makeState({ a: 1 });
    await state.loadState();

    const values: any[] = [];
    state.watch(["a"], (a) => values.push(a));

    // called right away with the current value
    expect(values).toEqual([1]);

    await state.set("a", 42);
    expect(values).toEqual([1, 42]);
  });

  it("watch() unsubscribe stops future notifications", async () => {
    const { state } = await makeState({ a: 1 });
    await state.loadState();

    const callback = vi.fn();
    const unsubscribe = state.watch(["a"], callback);
    callback.mockClear();

    unsubscribe();
    await state.set("a", 2);

    expect(callback).not.toHaveBeenCalled();
  });

  it("onChange() reports dirty-state and new-keys events", async () => {
    const { state, fake } = await makeState({ a: 1 });
    await state.loadState();

    const events: any[] = [];
    state.onChange((event) => events.push(event));

    await state.set("a", 2);
    expect(events).toContainEqual({ type: "dirty-state", keys: ["a"] });

    // "new-keys" fires when the server introduces a key the client didn't
    // already know about, e.g. another client/the server adding one.
    fake.pushServerState({ brandNewKey: "hello" });
    expect(
      events.some(
        (e) => e.type === "new-keys" && e.keys.includes("brandNewKey"),
      ),
    ).toBe(true);
  });

  it("flush() forces the given keys to be pushed even without a prior set() (README: state.flush)", async () => {
    const { state, fake } = await makeState({ a: 1, b: 2 });
    await state.loadState();

    // Mutate state directly, bypassing set(), then force a flush.
    (state as any)._state.a = 99;
    await state.flush("a");

    expect(fake.getServerState().a).toBe(99);
  });

  it("canDirty() respects the server-provided trame__client_only list", async () => {
    const { state } = await makeState({ trame__client_only: ["locked"] });
    await state.loadState();

    expect(state.canDirty("locked")).toBe(false);
    expect(state.canDirty("free")).toBe(true);
  });

  it("delete() unsubscribes from the wslink client without throwing", async () => {
    const { state, fake } = await makeState({ a: 1 });
    await state.loadState();

    expect(() => state.delete()).not.toThrow();
    expect(fake.remote.Trame.unsubscribe).toHaveBeenCalled();
  });
});
