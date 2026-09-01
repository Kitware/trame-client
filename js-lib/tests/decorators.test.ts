import { describe, expect, it } from "vitest";
import {
  decorate,
  fileHandler,
  fileListHandler,
  registerDecorator,
} from "../src/decorators";

describe("decorate()", () => {
  it("passes plain values through untouched", async () => {
    expect(await decorate(5)).toBe(5);
    expect(await decorate("hello")).toBe("hello");
    expect(await decorate(null)).toBe(null);
    expect(await decorate(undefined)).toBe(undefined);
  });

  it("serializes a File into a plain, transferable object", async () => {
    const file = new File(["hello world"], "greeting.txt", {
      type: "text/plain",
    });

    const result = await decorate(file);

    expect(result.name).toBe("greeting.txt");
    expect(result.type).toBe("text/plain");
    expect(result.content).toBeInstanceOf(DataView);
    expect(result.error).toBeNull();
    expect(result._filter).toEqual(["content"]);
  });

  it("serializes each File found in a FileList-like collection", async () => {
    // jsdom has no DataTransfer to build a real FileList; fileListHandler
    // accepts any array-like with a length, which is what <input type="file">
    // effectively hands the app in a real browser.
    const files = [new File(["a"], "a.txt"), new File(["b"], "b.txt")];

    const result = await decorate(files);

    expect(result).toHaveLength(2);
    expect(result.map((r: any) => r.name)).toEqual(["a.txt", "b.txt"]);
  });

  it("recurses into plain objects to find nested Files", async () => {
    const file = new File(["hi"], "nested.txt");

    const result = await decorate({ label: "upload", payload: file });

    expect(result.label).toBe("upload");
    expect(result.payload.name).toBe("nested.txt");
    expect(result.payload._filter).toEqual(["content"]);
  });

  it("registerDecorator() (README: trame.registerDecorator) plugs in custom serialization", async () => {
    registerDecorator({
      priority: 1000,
      async decorate(value) {
        if (typeof value === "number") {
          return value * 2;
        }
        return value;
      },
    });

    expect(await decorate(21)).toBe(42);
  });

  it("fileHandler ignores non-File values", async () => {
    expect(await fileHandler.decorate("not a file")).toBe("not a file");
  });

  it("fileListHandler passes through plain strings", async () => {
    expect(await fileListHandler.decorate("keep-me")).toBe("keep-me");
  });
});
