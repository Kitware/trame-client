import { describe, expect, it, vi } from "vitest";
import { act, Children, cloneElement } from "react";
import { render, screen, cleanup } from "@testing-library/react";
import { afterEach } from "vitest";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import { registerTag } from "../../src/runtime/tags";
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

  it("a style prop mixing static values with a {js: ...} entry resolves both and reacts to state changes", () => {
    const { trame, setState } = createFakeTrame({ color: "red" });
    renderTree(
      {
        tag: "div",
        props: {
          style: { fontWeight: "bold", color: { js: "color" } },
        },
        children: ["hi"],
      },
      trame,
    );

    const el = screen.getByText("hi");
    expect(el.style.fontWeight).toBe("bold");
    expect(el.style.color).toBe("red");

    act(() => setState({ color: "blue" }));
    expect(el.style.color).toBe("blue");
    expect(el.style.fontWeight).toBe("bold");
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

  it("forwards props a parent injects via cloneElement onto a wrapped child's real element", () => {
    // Mimics MUI compound components (Tabs/RadioGroup/ButtonGroup/...) that
    // clone each of their `children` to graft on props like `onClick` -
    // without needing literal_children, since this one doesn't read anything
    // off `child.props` before cloning (contrast with resolveLiteralChildren
    // .test.jsx's FakeSelect, which does and so still needs that flag).
    function FakeGroup({ children }) {
      return (
        <div data-testid="group">
          {Children.map(children, (child) => cloneElement(child, { extra: "injected" }))}
        </div>
      );
    }
    function FakeItem({ label, extra }) {
      return <div data-testid="item">{label}-{extra}</div>;
    }
    registerTag("fake-group", FakeGroup);
    registerTag("fake-item", FakeItem);

    const { trame } = createFakeTrame();
    renderTree(
      {
        tag: "fake-group",
        props: {},
        children: [{ tag: "fake-item", props: { label: "a" }, children: [] }],
      },
      trame,
    );

    expect(screen.getByTestId("item").textContent).toBe("a-injected");
  });
});
