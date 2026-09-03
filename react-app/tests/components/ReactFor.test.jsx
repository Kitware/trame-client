import { afterEach, describe, expect, it } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import { TrameContext } from "../../src/runtime/trameContext";
import { createRefRegistry } from "../../src/runtime/refs";
import { extendScope } from "../../src/runtime/scope";
import ReactFor from "../../src/components/ReactFor.jsx";
import { createFakeTrame } from "../helpers/fakeTrame";

afterEach(cleanup);

describe("ReactFor", () => {
  it("isolates each row's own loop variable (row N must not see row N-1's value)", () => {
    const { trame } = createFakeTrame();
    const ctx = { trame, getRefCallback: createRefRegistry(trame) };
    const rawChildren = [{ tag: "li", props: {}, children: [{ js: "row.id" }] }];

    render(
      <TrameContext.Provider value={ctx}>
        <ReactFor
          items={[{ id: "a" }, { id: "b" }, { id: "c" }]}
          name="row"
          rawChildren={rawChildren}
          scope={undefined}
        />
      </TrameContext.Provider>,
    );

    expect(screen.getByText("a")).toBeTruthy();
    expect(screen.getByText("b")).toBeTruthy();
    expect(screen.getByText("c")).toBeTruthy();
  });

  it("nests correctly inside an outer scope (For inside For style composition)", () => {
    const { trame } = createFakeTrame();
    const ctx = { trame, getRefCallback: createRefRegistry(trame) };
    const rawChildren = [
      { tag: "li", props: {}, children: [{ js: "outer + '-' + row.id" }] },
    ];

    render(
      <TrameContext.Provider value={ctx}>
        <ReactFor
          items={[{ id: 1 }, { id: 2 }]}
          name="row"
          rawChildren={rawChildren}
          scope={extendScope(undefined, ["outer"], ["group"])}
        />
      </TrameContext.Provider>,
    );

    expect(screen.getByText("group-1")).toBeTruthy();
    expect(screen.getByText("group-2")).toBeTruthy();
  });
});
