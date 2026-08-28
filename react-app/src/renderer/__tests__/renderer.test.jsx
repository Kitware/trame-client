import { describe, expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";

import TrameNode from "../TrameNode";
import { createScope, evalExpr } from "../evaluate";
import registry from "../../registry";

function mockTrame(initial = {}) {
  const store = { trame__client_only: [], ...initial };
  return {
    refs: {},
    utils: {},
    trigger: () => {},
    state: {
      get: (key) => (key === undefined ? store : store[key]),
      set: (key, value) => {
        store[key] = value;
      },
      update: (obj) => Object.assign(store, obj),
      flush: () => {},
      addListener: () => {},
      removeListener: () => {},
    },
  };
}

const render = (node, trame) =>
  renderToStaticMarkup(<TrameNode node={node} trame={trame} />);

describe("evaluate", () => {
  it("resolves state variables and globals", () => {
    const scope = createScope(mockTrame({ count: 41 }));
    expect(evalExpr("count + 1", scope)).toBe(42);
    expect(evalExpr("Math.max(count, 100)", scope)).toBe(100);
  });

  it("resolves $event to the handler argument, not the scope", () => {
    const trame = mockTrame({ count: 0 });
    const scope = createScope(trame);
    expect(evalExpr("$event + 1", scope, 41)).toBe(42);
  });
});

describe("TrameNode", () => {
  it("renders static attrs, bound props and text expressions", () => {
    const trame = mockTrame({ count: 5 });
    const node = {
      tag: "div",
      attrs: { id: "x", class: "a" },
      props: { title: "'c=' + count" },
      children: ["count: ", { expr: "count" }],
    };
    expect(render(node, trame)).toBe(
      '<div id="x" class="a" title="c=5">count: 5</div>',
    );
  });

  it("handles v-if / v-else chains", () => {
    const trame = mockTrame({ show: false });
    const node = {
      tag: "div",
      children: [
        { tag: "span", dirs: { if: "show" }, children: ["yes"] },
        { tag: "span", dirs: { else: true }, children: ["no"] },
      ],
    };
    expect(render(node, trame)).toBe("<div><span>no</span></div>");
  });

  it("handles v-for", () => {
    const trame = mockTrame({ items: ["a", "b"] });
    const node = {
      tag: "ul",
      children: [
        {
          tag: "li",
          dirs: { for: { item: "it", index: "i", source: "items" } },
          children: [{ expr: "i" }, ":", { expr: "it" }],
        },
      ],
    };
    expect(render(node, trame)).toBe("<ul><li>0:a</li><li>1:b</li></ul>");
  });

  it("handles v-show and style strings", () => {
    const trame = mockTrame({ visible: false });
    const node = {
      tag: "div",
      attrs: { style: "color: red; margin-top: 2px" },
      dirs: { show: "visible" },
    };
    expect(render(node, trame)).toBe(
      '<div style="color:red;margin-top:2px;display:none"></div>',
    );
  });

  it("renders v-model on native input from state", () => {
    const trame = mockTrame({ name_var: "hello" });
    const node = {
      tag: "input",
      dirs: { models: [{ arg: null, modifiers: [], expr: "name_var" }] },
    };
    expect(render(node, trame)).toBe('<input value="hello"/>');
  });

  it("model onChange writes the input value back to state", async () => {
    const { default: TestRenderer } = await import("react-dom/client");
    void TestRenderer; // jsdom-free: exercise the handler directly
    const trame = mockTrame({ count: 2 });
    const node = {
      tag: "input",
      attrs: { type: "range" },
      dirs: { models: [{ arg: null, modifiers: ["number"], expr: "count" }] },
    };
    // render to walk buildProps, then invoke the produced handler
    let captured;
    registry.register("probe-input", (props) => {
      captured = props;
      return <input />;
    });
    render({ ...node, tag: "probe-input" }, trame);
    captured.onUpdateValue("7");
    expect(trame.state.get("count")).toBe(7);
    registry.unregister("probe-input");
  });

  it("resolves registered components and maps events to on<Event> props", () => {
    const seen = {};
    registry.register("my-widget", ({ label, onChange }) => {
      seen.onChange = onChange;
      return <button>{label}</button>;
    });
    const trame = mockTrame({ txt: "go" });
    const node = {
      tag: "my-widget",
      props: { label: "txt" },
      on: { change: "txt = 'done'" },
    };
    expect(render(node, trame)).toBe("<button>go</button>");
    seen.onChange("ignored");
    expect(trame.state.get("txt")).toBe("done");
    registry.unregister("my-widget");
  });
});
