import { describe, expect, it, vi } from "vitest";
import { act } from "react";
import { render, screen, cleanup } from "@testing-library/react";
import { afterEach } from "vitest";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import TrameNode from "../../src/components/TrameNode.jsx";
import { createFakeTrame } from "../helpers/fakeTrame";

afterEach(cleanup);

function renderTree(nodes, trame, scope) {
  const ctx = { trame, getRefCallback: createRefRegistry(trame) };
  return render(
    <TrameContext.Provider value={ctx}>
      <TrameNode nodes={nodes} scope={scope} />
    </TrameContext.Provider>,
  );
}

describe("TrameNode", () => {
  it("renders a {tag, props, children} tree to the expected DOM", () => {
    const { trame } = createFakeTrame();
    renderTree({ tag: "div", props: { className: "x" }, children: ["hi"] }, trame);

    const el = screen.getByText("hi");
    expect(el.tagName).toBe("DIV");
    expect(el.className).toBe("x");
  });

  it("a {js: ...} child re-renders only when the state it reads changes", () => {
    const { trame, setState } = createFakeTrame({ count: 1, other: "a" });
    const renderSpy = vi.fn();

    function Wrapper() {
      renderSpy();
      return <TrameNode nodes={{ js: "count" }} />;
    }

    const ctx = { trame, getRefCallback: createRefRegistry(trame) };
    render(
      <TrameContext.Provider value={ctx}>
        <Wrapper />
      </TrameContext.Provider>,
    );

    expect(screen.getByText("1")).toBeTruthy();
    renderSpy.mockClear();

    act(() => setState({ other: "b" }));
    expect(renderSpy).not.toHaveBeenCalled();

    act(() => setState({ count: 2 }));
    expect(screen.getByText("2")).toBeTruthy();
  });

  it("ref='name' populates trame.refs.name on mount, removes it on unmount", () => {
    const { trame } = createFakeTrame();
    const { unmount } = renderTree(
      { tag: "div", props: { ref: "myRef" }, children: [] },
      trame,
    );

    expect(trame.refs.myRef).toBeTruthy();
    expect(trame.refs.myRef.tagName).toBe("DIV");

    unmount();
    expect(trame.refs.myRef).toBeUndefined();
  });
});
