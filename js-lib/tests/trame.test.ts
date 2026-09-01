import { beforeEach, describe, expect, it, vi } from "vitest";
import { Trame } from "../src/trame";
import { createFakeClient, type FakeClient } from "./helpers/fakeClient";

// `Trame.connect()` builds its client via `wslink.createClient()`. We swap
// that factory for one that hands back our in-memory fake so tests never
// need a real server. vitest hoists `vi.mock` above the imports above, so
// "../src/wslink" is already mocked by the time "../src/trame" loads it.
let fake: FakeClient;
vi.mock("../src/wslink", () => ({
  default: {
    createClient: () => fake.client,
  },
}));

beforeEach(() => {
  fake = createFakeClient({ a: 0, b: 0 });
});

describe("Trame (README: basic usage)", () => {
  it("connect() returns the resolved configuration", async () => {
    const trame = new Trame();
    const config = await trame.connect({ application: "trame" });

    expect(trame.isConnected()).toBe(true);
    expect(config).toEqual({ application: "trame" });
    expect(trame.client).toBe(fake.client);
  });

  it("state.set()/state.get() round-trip through the server (README: state.set/get)", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    await trame.state!.set("a", 5);

    expect(trame.state!.get("a")).toBe(5);
    expect(fake.getServerState().a).toBe(5);
  });

  it("state.update() applies multiple keys at once (README: state.update)", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    await trame.state!.update({ a: 1, b: 2 });

    expect(trame.state!.get("a")).toBe(1);
    expect(trame.state!.get("b")).toBe(2);
  });

  it("state.watch() reports changes for the watched keys (README: state.watch)", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    const seen: any[] = [];
    trame.state!.watch(["a"], (a) => seen.push(a));

    await trame.state!.set("a", 7);
    expect(seen).toEqual([0, 7]);
  });

  it("trigger() calls the named server method and returns its result (README: trame.trigger)", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    fake.registerTrigger("name", (arg0, arg1, kwargs) => ({
      arg0,
      arg1,
      kwargs,
    }));

    const result = await trame.trigger("name", ["arg_0", "arg_1"], {
      kwarg_0: 1,
      kwarg_1: 2,
    });

    expect(result).toEqual({
      arg0: "arg_0",
      arg1: "arg_1",
      kwargs: { kwarg_0: 1, kwarg_1: 2 },
    });
  });

  it("refs[name] lets the server invoke a method on a registered JS object (README: trame.refs)", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    const jsObject = { method: vi.fn() };
    trame.refs["name"] = jsObject;

    fake.emitAction({
      ref: "name",
      type: "method",
      method: "method",
      args: ["arg_0", "arg_1"],
    });

    expect(jsObject.method).toHaveBeenCalledWith("arg_0", "arg_1");
  });
});

describe("Trame (README: more API examples)", () => {
  it("registerDecorator() customizes trigger() argument serialization", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    // `registerDecorator` mutates a module-wide registry (like the README's
    // built-in File handling), so this uses a value shape (a tagged marker
    // object) that no other test in this file could ever produce, keeping
    // the registration side effect from leaking into unrelated assertions.
    class TestMarker {
      constructor(public payload: string) {}
    }
    trame.registerDecorator({
      priority: 1000,
      async decorate(value) {
        return value instanceof TestMarker ? { encoded: value.payload } : value;
      },
    });

    fake.registerTrigger("encode", (value) => value);
    const result = await trame.trigger("encode", [new TestMarker("hello")]);
    expect(result).toEqual({ encoded: "hello" });
  });

  it("onClose() is notified when the connection closes, and can unsubscribe", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    const onClose = vi.fn();
    const unsubscribe = trame.onClose(onClose);

    trame.disconnect();
    expect(onClose).toHaveBeenCalledWith("Connection closed");

    unsubscribe();
    fake.emitClose("closed again");
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it("onError() is notified on connection errors, and can unsubscribe", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    const onError = vi.fn();
    const unsubscribe = trame.onError(onError);

    fake.emitError("boom");
    expect(onError).toHaveBeenCalledWith("boom");

    unsubscribe();
    fake.emitError("boom again");
    expect(onError).toHaveBeenCalledTimes(1);
  });

  it("disconnect() notifies the server lifecycle and closes the connection", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    trame.disconnect();

    expect(fake.remote.Trame.lifeCycleUpdate).toHaveBeenCalledWith(
      "client_exited",
    );
    expect(fake.client.disconnect).toHaveBeenCalledWith(0);
    expect(trame.isConnected()).toBe(false);
  });

  it("exit(timeout) notifies the server lifecycle and disconnects with that timeout", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    trame.exit(120);

    expect(fake.remote.Trame.lifeCycleUpdate).toHaveBeenCalledWith(
      "client_exited",
    );
    expect(fake.client.disconnect).toHaveBeenCalledWith(120);
  });

  it("reconnect() re-establishes the connection using the saved configuration", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });
    trame.disconnect();

    const config = await trame.reconnect();

    expect(trame.isConnected()).toBe(true);
    expect(config).toEqual({ application: "trame" });
  });

  it("exposes client and state on the instance", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    expect(trame.client).toBeTruthy();
    expect(trame.state).toBeTruthy();
  });

  it("state.flush(keys) force-pushes the given keys to the server", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    (trame.state as any)._state.a = 55;
    await trame.state!.flush("a");

    expect(fake.getServerState().a).toBe(55);
  });

  it("state.onChange() reports dirty-state and new-keys events", async () => {
    const trame = new Trame();
    await trame.connect({ application: "trame" });

    const events: any[] = [];
    trame.state!.onChange((event) => events.push(event));

    await trame.state!.set("a", 2);
    expect(events).toContainEqual({ type: "dirty-state", keys: ["a"] });
  });
});
