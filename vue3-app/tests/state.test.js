import { describe, expect, it, vi } from "vitest";
import { SharedState } from "../src/core/trame/state";
import { createFakeClient } from "./helpers/fakeClient";

async function makeState(initialServerState = {}, oldState = null) {
  // trame_server always ships trame__client_only, so every test but the one
  // about an unloaded state gets it.
  const fake = createFakeClient({
    trame__client_only: [],
    ...initialServerState,
  });
  const state = new SharedState(fake.client, oldState);
  await state.loadState();
  return { state, fake };
}

describe("SharedState", () => {
  it("loads its initial content from the server", async () => {
    const { state } = await makeState({ a: 1, b: 2 });

    expect(state.get("a")).toBe(1);
    expect(state.getAllKeys()).toEqual(
      expect.arrayContaining(["a", "b", "trame__client_only"]),
    );
  });

  it("set() updates locally and pushes to the server", async () => {
    const { state, fake } = await makeState();

    await state.set("a", 5);

    expect(state.get("a")).toBe(5);
    expect(fake.getServerState().a).toBe(5);
  });

  it("addListener() returns a working unsubscribe function", async () => {
    const { state } = await makeState({ a: 1 });
    const listener = vi.fn();

    const unsubscribe = state.addListener(listener);
    expect(unsubscribe).toBeTypeOf("function");

    await state.set("a", 2);
    expect(listener).toHaveBeenCalled();

    listener.mockClear();
    unsubscribe();
    await state.set("a", 3);
    expect(listener).not.toHaveBeenCalled();
  });

  it("delete() only hands wslink subscriptions to Trame.unsubscribe", async () => {
    const { state, fake } = await makeState({ a: 1 });

    // wslink throws on an undefined subscription, so a local listener handed to
    // it takes the whole teardown - and the reconnect it belongs to - down.
    expect(() => state.delete()).not.toThrow();
    expect(fake.remote.Trame.unsubscribe).toHaveBeenCalledTimes(1);
    expect(fake.remote.Trame.unsubscribe).toHaveBeenCalledWith(
      expect.objectContaining({ topic: "trame.state.topic" }),
    );
  });

  it("delete() releases the rest when one subscription cannot be released", async () => {
    const { state, fake } = await makeState({ a: 1 });
    const released = vi.fn();
    state.subscriptions.push(undefined);
    state.unsubscribes.push(released);

    expect(() => state.delete()).not.toThrow();
    expect(released).toHaveBeenCalled();
    expect(state.subscriptions).toHaveLength(0);
    expect(fake.remote.Trame.unsubscribe).toHaveBeenCalledWith(
      expect.objectContaining({ topic: "trame.state.topic" }),
    );
  });

  it("delete() consumes an unsubscribe that rejects asynchronously", async () => {
    // wslink's unsubscribe REJECTS for a subscription the session does not hold,
    // which is normal during teardown and lands as an unhandled rejection in the
    // middle of a reconnect. Asserted by watching the returned promise get a
    // rejection handler, not by listening for `unhandledRejection`: that fires
    // too late and under vitest's own handler to fail this test on the code
    // without the fix -- measured, it passed either way.
    const { state, fake } = await makeState({ a: 1 });
    const rejected = Promise.reject({
      code: -32099,
      message: "not subscribed",
    });
    const handled = vi.spyOn(rejected, "catch");
    fake.remote.Trame.unsubscribe = vi.fn(() => rejected);

    expect(() => state.delete()).not.toThrow();
    expect(handled).toHaveBeenCalled();

    await rejected.catch(() => {});
  });

  it("a key created on the client is announced as a new key", async () => {
    const { state } = await makeState({ a: 1 });
    const events = [];
    state.addListener((event) => events.push(event));

    await state.set("brand_new", "value");

    expect(events).toEqual([
      { type: "new-keys", keys: ["brand_new"] },
      { type: "dirty-state", keys: ["brand_new"] },
    ]);
  });

  it("a key that already exists is not announced as new again", async () => {
    const { state } = await makeState({ a: 1 });
    const events = [];
    state.addListener((event) => events.push(event));

    await state.set("a", 2);
    await state.set("a", 3);

    expect(events.filter((e) => e.type === "new-keys")).toEqual([]);
  });

  it("update() announces every key it creates", async () => {
    const { state } = await makeState({ a: 1 });
    const events = [];
    state.addListener((event) => events.push(event));

    await state.update({ a: 2, b: 3, c: 4 });

    const announced = events
      .filter((e) => e.type === "new-keys")
      .flatMap((e) => e.keys);
    expect(announced.sort()).toEqual(["b", "c"]);
  });

  it("keeps the listeners and watchers of the state it replaces", async () => {
    const { state: oldState } = await makeState({ a: 1 });
    const listener = vi.fn();
    const watcher = vi.fn();
    oldState.addListener(listener);
    oldState.watch(["a"], watcher);
    listener.mockClear();
    watcher.mockClear();

    // what a reconnect does: release the old state, build one on a new client
    oldState.delete();
    const { state } = await makeState({ a: 9 }, oldState);

    expect(listener).toHaveBeenCalled();
    expect(watcher).toHaveBeenCalledWith(9);
    expect(state.listeners).toContain(listener);
  });

  it("a listener removed on one state is removed on the state that inherits it", async () => {
    const { state: oldState } = await makeState({ a: 1 });
    const listener = vi.fn();
    oldState.addListener(listener);

    const { state } = await makeState({ a: 1 }, oldState);
    state.removeListener(listener);
    listener.mockClear();

    await state.set("a", 2);
    expect(listener).not.toHaveBeenCalled();
    expect(oldState.listeners).not.toContain(listener);
  });

  it("a failed push keeps its keys dirty instead of rejecting", async () => {
    const { state, fake } = await makeState({ a: 1 });
    fake.setPushFails(true);

    await expect(state.set("a", 2)).resolves.toBeUndefined();
    expect(state.dirtyKeys.has("a")).toBe(true);

    fake.setPushFails(false);
    await state.flush();
    expect(fake.getServerState().a).toBe(2);
    expect(state.dirtyKeys.size).toBe(0);
  });

  it("dirty() works before the first server state arrives", () => {
    const fake = createFakeClient();
    const state = new SharedState(fake.client);

    expect(() => state.dirty("whatever")).not.toThrow();
  });
});
