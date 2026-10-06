import { afterEach, beforeEach, expect, it, vi } from "vitest";

/**
 * When the session is really gone, the retries stop and the user is told.
 *
 * A reconnect only ever goes back to the session the page is on, so there is
 * nothing else to try once that session stops answering: the component has to
 * end on "we tried our best, reload the page" rather than spinning forever.
 */

vi.mock("@kitware/vtk.js/Common/Core/URLExtract", () => ({
  default: { extractURLParameters: () => ({ reconnect: "auto" }) },
}));

let mounted = [];
let trame = null;

beforeEach(() => {
  mounted = [];
  trame = { connect: vi.fn(async () => Promise.reject(new Error("gone"))) };
  // The component destructures `window.Vue` at import time, so this has to
  // exist before the import below and stay the same object afterwards.
  window.Vue = {
    inject: () => trame,
    ref: (value) => ({ value }),
    onMounted: (cb) => mounted.push(cb),
    onBeforeUnmount: () => {},
  };
  vi.useFakeTimers();
});

afterEach(() => {
  vi.useRealTimers();
});

it("a session that never comes back ends on a reload prompt", async () => {
  const TrameReconnect = (await import("../src/components/TrameReconnect"))
    .default;
  const api = TrameReconnect.setup({ maxRetry: 3, delay: 10 });
  mounted.forEach((cb) => cb());

  expect(api.gaveUp.value).toBe(false);

  await vi.advanceTimersByTimeAsync(10 * 5);

  expect(api.gaveUp.value).toBe(true);
  expect(trame.connect).toHaveBeenCalledTimes(3);
  // Every attempt was a plain reconnect: nothing ever asked for another session.
  expect(trame.connect.mock.calls).toEqual([[], [], []]);
  // ...and the retries stopped rather than running on a dead session forever.
  await vi.advanceTimersByTimeAsync(10 * 5);
  expect(trame.connect).toHaveBeenCalledTimes(3);
});
