import { afterEach, describe, expect, it, vi } from "vitest";
import { act } from "react";
import { render, cleanup } from "@testing-library/react";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import TrameJSEval from "../../src/components/TrameJSEval.jsx";
import TrameStyle from "../../src/components/TrameStyle.jsx";
import TrameScript from "../../src/components/TrameScript.jsx";
import TrameClientStateChange from "../../src/components/TrameClientStateChange.jsx";
import TrameClientTriggers from "../../src/components/TrameClientTriggers.jsx";
import TrameLifeCycleMonitor from "../../src/components/TrameLifeCycleMonitor.jsx";
import TrameSizeObserver from "../../src/components/TrameSizeObserver.jsx";
import { createFakeTrame } from "../helpers/fakeTrame";

afterEach(cleanup);

function withContext(trame, node) {
  const ctx = { trame, getRefCallback: createRefRegistry(trame) };
  return <TrameContext.Provider value={ctx}>{node}</TrameContext.Provider>;
}

describe("TrameJSEval", () => {
  it("exec() with no arg fires onExec with the bound event prop", () => {
    const onExec = vi.fn();
    const { trame } = createFakeTrame();
    const getRefCallback = createRefRegistry(trame);
    render(
      withContext(
        trame,
        <TrameJSEval ref={getRefCallback("myExec")} event="hello" onExec={onExec} />,
      ),
    );

    trame.refs.myExec.exec();
    expect(onExec).toHaveBeenCalledWith("hello");
  });

  it("exec(arg) fires onExec with arg instead of the bound event prop", () => {
    const onExec = vi.fn();
    const { trame } = createFakeTrame();
    const getRefCallback = createRefRegistry(trame);
    render(
      withContext(
        trame,
        <TrameJSEval ref={getRefCallback("myExec")} event="hello" onExec={onExec} />,
      ),
    );

    trame.refs.myExec.exec("world");
    expect(onExec).toHaveBeenCalledWith("world");
  });
});

describe("TrameStyle", () => {
  it("injects a <style> tag with the bound css and removes it when cleared", () => {
    const { trame } = createFakeTrame();
    const { rerender } = render(
      withContext(trame, <TrameStyle css="body { color: red; }" />),
    );

    let styleEl = document.head.querySelector("style");
    expect(styleEl.textContent).toBe("body { color: red; }");

    rerender(withContext(trame, <TrameStyle css="" />));
    styleEl = document.head.querySelector("style");
    expect(styleEl).toBeNull();
  });
});

describe("TrameScript", () => {
  it("injects a <script> tag with the bound content and type", () => {
    const { trame } = createFakeTrame();
    render(withContext(trame, <TrameScript script="console.log(1)" module />));

    const scriptEl = document.head.querySelector("script");
    expect(scriptEl.textContent).toBe("console.log(1)");
    expect(scriptEl.type).toBe("module");
  });
});

describe("TrameClientStateChange", () => {
  it("fires onChange when value changes, not on mount by default", () => {
    const onChange = vi.fn();
    const { trame } = createFakeTrame();
    const { rerender } = render(
      withContext(trame, <TrameClientStateChange value={1} onChange={onChange} />),
    );
    expect(onChange).not.toHaveBeenCalled();

    rerender(withContext(trame, <TrameClientStateChange value={2} onChange={onChange} />));
    expect(onChange).toHaveBeenCalledWith(2);
  });

  it("triggerChangeOnCreate fires onChange once on mount", () => {
    const onChange = vi.fn();
    const { trame } = createFakeTrame();
    render(
      withContext(
        trame,
        <TrameClientStateChange value={1} triggerChangeOnCreate onChange={onChange} />,
      ),
    );
    expect(onChange).toHaveBeenCalledWith(1);
  });
});

describe("TrameClientTriggers", () => {
  it("fires created/beforeMount synchronously and mounted after commit", () => {
    const created = vi.fn();
    const mounted = vi.fn();
    const { trame } = createFakeTrame();
    const getRefCallback = createRefRegistry(trame);
    render(
      withContext(
        trame,
        <TrameClientTriggers ref={getRefCallback("trig")} created={created} mounted={mounted} />,
      ),
    );

    expect(created).toHaveBeenCalled();
    expect(mounted).toHaveBeenCalled();
  });

  it("fires beforeDestroy/beforeUnmount on unmount", () => {
    const beforeDestroy = vi.fn();
    const beforeUnmount = vi.fn();
    const { trame } = createFakeTrame();
    const getRefCallback = createRefRegistry(trame);
    const { unmount } = render(
      withContext(
        trame,
        <TrameClientTriggers
          ref={getRefCallback("trig")}
          beforeDestroy={beforeDestroy}
          beforeUnmount={beforeUnmount}
        />,
      ),
    );
    unmount();
    expect(beforeDestroy).toHaveBeenCalled();
    expect(beforeUnmount).toHaveBeenCalled();
  });

  it("server-triggered emit(topic, event) dispatches to any custom event by name", () => {
    const myCustomEvent = vi.fn();
    const { trame } = createFakeTrame();
    const getRefCallback = createRefRegistry(trame);
    render(
      withContext(
        trame,
        <TrameClientTriggers ref={getRefCallback("trig")} myCustomEvent={myCustomEvent} />,
      ),
    );

    trame.refs.trig.emit("myCustomEvent", "payload");
    expect(myCustomEvent).toHaveBeenCalledWith("payload");
  });
});

describe("TrameLifeCycleMonitor", () => {
  it("logs created/beforeMount/mounted on first render, then beforeUpdate/updated on re-render", () => {
    const spy = vi.spyOn(console, "log").mockImplementation(() => {});
    const { trame } = createFakeTrame();
    const { rerender } = render(
      withContext(trame, <TrameLifeCycleMonitor name="mon" value="v1" />),
    );

    expect(spy.mock.calls.map((c) => c[1])).toEqual(["created", "beforeMount", "mounted"]);
    spy.mockClear();

    rerender(withContext(trame, <TrameLifeCycleMonitor name="mon" value="v2" />));
    expect(spy.mock.calls.map((c) => c[1])).toEqual(["beforeUpdate", "updated"]);

    spy.mockRestore();
  });

  it("logs beforeDestroy/destroyed on unmount", () => {
    const spy = vi.spyOn(console, "log").mockImplementation(() => {});
    const { trame } = createFakeTrame();
    const { unmount } = render(withContext(trame, <TrameLifeCycleMonitor name="mon" />));
    spy.mockClear();

    unmount();
    expect(spy.mock.calls.map((c) => c[1])).toEqual(["beforeDestroy", "destroyed"]);
    spy.mockRestore();
  });
});

describe("TrameSizeObserver", () => {
  it("writes {size, pixelRatio, dpi} into trame state on resize", () => {
    let resizeCallback;
    const originalRO = window.ResizeObserver;
    window.ResizeObserver = class {
      constructor(cb) {
        resizeCallback = cb;
      }
      observe() {}
      disconnect() {}
    };

    const { trame } = createFakeTrame();
    render(withContext(trame, <TrameSizeObserver name="mySize" />));

    act(() => resizeCallback());
    expect(trame.state.get("mySize").name).toBe("mySize");
    expect(trame.state.get("mySize").size).toBeDefined();
    expect(trame.state.get("mySize").dpi).toBeDefined();

    window.ResizeObserver = originalRO;
  });
});
