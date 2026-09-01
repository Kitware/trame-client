import { describe, expect, it, vi } from "vitest";
import { ListenerManager, WatcherManager } from "../src/listeners";

describe("ListenerManager", () => {
  it("calls every registered listener on emit()", () => {
    const manager = new ListenerManager("test");
    const a = vi.fn();
    const b = vi.fn();
    manager.on(a);
    manager.on(b);

    manager.emit("payload", 2);

    expect(a).toHaveBeenCalledWith("payload", 2);
    expect(b).toHaveBeenCalledWith("payload", 2);
  });

  it("on() returns an unsubscribe function", () => {
    const manager = new ListenerManager("test");
    const fn = vi.fn();
    const unsubscribe = manager.on(fn);

    unsubscribe();
    manager.emit();

    expect(fn).not.toHaveBeenCalled();
  });

  it("keeps emitting to the remaining listeners if one throws", () => {
    const manager = new ListenerManager("test");
    const failing = vi.fn(() => {
      throw new Error("boom");
    });
    const ok = vi.fn();
    manager.on(failing);
    manager.on(ok);

    expect(() => manager.emit()).not.toThrow();
    expect(ok).toHaveBeenCalled();
  });
});

describe("WatcherManager", () => {
  it("notifies only watchers whose dependencies changed", () => {
    const manager = new WatcherManager();
    const watchA = vi.fn();
    const watchB = vi.fn();
    manager.watch(["a"], watchA);
    manager.watch(["b"], watchB);

    manager.notifyWatchers(["a"], { a: 1, b: 2 });

    expect(watchA).toHaveBeenCalledWith(1);
    expect(watchB).not.toHaveBeenCalled();
  });

  it("unsubscribe stops further notifications", () => {
    const manager = new WatcherManager();
    const watch = vi.fn();
    const unsubscribe = manager.watch(["a"], watch);

    unsubscribe();
    manager.notifyWatchers(["a"], { a: 1 });

    expect(watch).not.toHaveBeenCalled();
  });
});
