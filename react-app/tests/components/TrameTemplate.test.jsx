import { afterEach, describe, expect, it, vi } from "vitest";
import { act, useEffect } from "react";
import { cleanup, render } from "@testing-library/react";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import { registerTag } from "../../src/runtime/tags";
import TrameTemplate from "../../src/components/TrameTemplate.jsx";
import { createFakeTrame } from "../helpers/fakeTrame";

afterEach(cleanup);

function renderTemplate(trame, templateName) {
  const ctx = { trame, getRefCallback: createRefRegistry(trame) };
  return render(
    <TrameContext.Provider value={ctx}>
      <TrameTemplate templateName={templateName} />
    </TrameContext.Provider>,
  );
}

describe("TrameTemplate", () => {
  it("remounts its subtree when a reused instance switches template name", () => {
    const mountSpy = vi.fn();
    const unmountSpy = vi.fn();

    function Probe() {
      useEffect(() => {
        mountSpy();
        return () => unmountSpy();
      }, []);
      return <div data-testid="probe" />;
    }
    registerTag("test-probe", Probe);

    const probeTree = { tag: "test-probe", props: {}, children: [] };
    const { trame } = createFakeTrame({
      trame__template_a: probeTree,
      trame__template_b: probeTree,
    });

    const { rerender } = renderTemplate(trame, "a");
    expect(mountSpy).toHaveBeenCalledTimes(1);
    expect(unmountSpy).toHaveBeenCalledTimes(0);

    const ctx = { trame, getRefCallback: createRefRegistry(trame) };
    rerender(
      <TrameContext.Provider value={ctx}>
        <TrameTemplate templateName="b" />
      </TrameContext.Provider>,
    );

    expect(unmountSpy).toHaveBeenCalledTimes(1);
    expect(mountSpy).toHaveBeenCalledTimes(2);
  });

  it("does not remount its subtree when the same template's content updates", () => {
    const mountSpy = vi.fn();
    const unmountSpy = vi.fn();

    function Probe() {
      useEffect(() => {
        mountSpy();
        return () => unmountSpy();
      }, []);
      return <div data-testid="probe" />;
    }
    registerTag("test-probe-stable", Probe);

    const { trame, setState } = createFakeTrame({
      trame__template_a: { tag: "test-probe-stable", props: {}, children: [] },
    });

    renderTemplate(trame, "a");
    expect(mountSpy).toHaveBeenCalledTimes(1);

    act(() =>
      setState({
        trame__template_a: {
          tag: "test-probe-stable",
          props: {},
          children: ["updated"],
        },
      }),
    );

    expect(mountSpy).toHaveBeenCalledTimes(1);
    expect(unmountSpy).toHaveBeenCalledTimes(0);
  });
});
