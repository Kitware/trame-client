import { describe, expect, it, vi, afterEach } from "vitest";
import { act } from "react";
import { Children, cloneElement } from "react";
import { render, screen, cleanup } from "@testing-library/react";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import { registerTag } from "../../src/runtime/tags";
import TrameNode from "../../src/components/TrameNode.jsx";
import { createFakeTrame } from "../helpers/fakeTrame";

afterEach(cleanup);

// Mimics MUI's SelectInput closely enough to exercise the bug this module
// fixes: it reads `child.props.value` / `child.props.children` straight off
// its `children` array via `Children.toArray`, before anything renders, and
// re-attaches its own `onClick` via `cloneElement` - both only work if
// `children` are real <FakeMenuItem> elements, not a wrapper component.
function FakeSelect({ value, onSelect, children }) {
  const renderSpy = FakeSelect.renderSpy;
  renderSpy?.();
  const items = Children.toArray(children);
  const selected = items.find((child) => child.props.value === value);
  return (
    <div data-testid="fake-select">
      {/* Rendered the way MUI's real SelectInput renders its computed
          `display` value - `child.props.children` isn't necessarily a plain
          string (grandchildren still go through the normal <TrameNode>
          wrapper, see resolveLiteralChildren.js), so it has to be rendered,
          not read as a string. */}
      <div data-testid="fake-select-display">{selected?.props.children}</div>
      {items.map((child) =>
        cloneElement(child, { onClick: () => onSelect(child.props.value) }),
      )}
    </div>
  );
}

function FakeMenuItem({ value, onClick, children }) {
  return (
    <div role="option" data-value={value} onClick={onClick}>
      {children}
    </div>
  );
}

registerTag("fake-select", FakeSelect);
registerTag("fake-menu-item", FakeMenuItem);

function selectTree(valueExpr) {
  return {
    tag: "fake-select",
    props: {
      value: { js: valueExpr },
      onSelect: { callback: { trigger: "onSelect", args: { js: "[$event]" } } },
    },
    literalChildren: true,
    children: [
      { tag: "fake-menu-item", props: { value: "vanilla" }, children: ["Vanilla"] },
      { tag: "fake-menu-item", props: { value: "chocolate" }, children: ["Chocolate"] },
    ],
  };
}

function renderTree(nodes, trame, scope) {
  const ctx = { trame, getRefCallback: createRefRegistry(trame) };
  return render(
    <TrameContext.Provider value={ctx}>
      <TrameNode nodes={nodes} scope={scope} />
    </TrameContext.Provider>,
  );
}

describe("literalChildren", () => {
  it("gives a React.Children-inspecting parent real elements with real props", () => {
    const { trame } = createFakeTrame({ flavor: "vanilla" });
    renderTree(selectTree("flavor"), trame);

    expect(screen.getByTestId("fake-select-display").textContent).toBe("Vanilla");
    expect(screen.getAllByRole("option")).toHaveLength(2);
  });

  it("clicking a cloned item's onClick still reaches the python trigger", () => {
    const { trame } = createFakeTrame({ flavor: "vanilla" });
    renderTree(selectTree("flavor"), trame);

    screen.getByText("Chocolate").click();

    expect(trame.trigger).toHaveBeenCalledWith("onSelect", ["chocolate"], {});
  });

  it("re-renders with the new selection when trame state changes", () => {
    const { trame, setState } = createFakeTrame({ flavor: "vanilla" });
    renderTree(selectTree("flavor"), trame);

    act(() => setState({ flavor: "chocolate" }));

    expect(screen.getByTestId("fake-select-display").textContent).toBe("Chocolate");
  });

  it("does not re-render when an untracked state key changes", () => {
    const { trame, setState } = createFakeTrame({ flavor: "vanilla", other: "a" });
    FakeSelect.renderSpy = vi.fn();
    renderTree(selectTree("flavor"), trame);
    FakeSelect.renderSpy.mockClear();

    act(() => setState({ other: "b" }));

    expect(FakeSelect.renderSpy).not.toHaveBeenCalled();
    FakeSelect.renderSpy = undefined;
  });
});
