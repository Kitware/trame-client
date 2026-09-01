import { describe, expect, it } from "vitest";
import vtkURLExtract from "../src/URLExtract";

describe("toNativeType()", () => {
  it("parses booleans, null and undefined", () => {
    expect(vtkURLExtract.toNativeType("true")).toBe(true);
    expect(vtkURLExtract.toNativeType("false")).toBe(false);
    expect(vtkURLExtract.toNativeType("null")).toBeNull();
    expect(vtkURLExtract.toNativeType("undefined")).toBeUndefined();
  });

  it("parses numbers", () => {
    expect(vtkURLExtract.toNativeType("42")).toBe(42);
    expect(vtkURLExtract.toNativeType("3.14")).toBe(3.14);
  });

  it("parses bracketed lists recursively", () => {
    expect(vtkURLExtract.toNativeType("[1, 2, 3]")).toEqual([1, 2, 3]);
    expect(vtkURLExtract.toNativeType("[true, false, null]")).toEqual([
      true,
      false,
      null,
    ]);
  });

  it("leaves non-numeric strings as-is", () => {
    expect(vtkURLExtract.toNativeType("hello")).toBe("hello");
  });
});

describe("extractURLParameters()", () => {
  it("extracts and type-casts query parameters by default", () => {
    const result = vtkURLExtract.extractURLParameters(
      true,
      "?application=trame&count=3&debug=true",
    );

    expect(result).toEqual({ application: "trame", count: 3, debug: true });
  });

  it("keeps values as raw strings when castToNativeType is false", () => {
    const result = vtkURLExtract.extractURLParameters(false, "?count=3");

    expect(result).toEqual({ count: "3" });
  });

  it("treats a valueless flag as true", () => {
    const result = vtkURLExtract.extractURLParameters(true, "?useUrl");

    expect(result).toEqual({ useUrl: true });
  });
});
