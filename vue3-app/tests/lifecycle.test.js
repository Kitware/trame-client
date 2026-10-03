import { beforeEach, expect, it, vi } from "vitest";

/**
 * A wrapper swapped onto `trame.client` is an identity change, not a connection.
 *
 * This runs the REAL `createTrameInstance` and the REAL `TrameApp.setup`, because the
 * claim is about what the two channels do to a component, and a stubbed `trame` cannot
 * make that claim: aliasing `notifyClientReplaced` to `notifyConnection` in the source
 * has to turn this red. Vue's hooks and the transport are doubles; nothing is mounted
 * in a browser.
 *
 * `TrameApp`'s connect listener is a lifecycle consumer -- it announces
 * `client_connected` to the server, registers a `beforeunload` and installs the keyed
 * templates -- so replaying it because something wrapped the client on a transport that
 * never dropped is a far larger blast radius than the problem the wrapper solves.
 */

const hoisted = vi.hoisted(() => ({ clients: [], makeClient: null }));

vi.mock("../src/core/wslink", () => ({
  default: {
    createClient: () => hoisted.makeClient(),
    configDecorator: (config) => config,
  },
}));

const { createTrameInstance } = await import("../src/core/trame");

/** the names `TrameApp` pushes through `lifeCycleUpdate`, in order */
let lifecycle = [];
/** every `window.addEventListener` name registered while a test runs */
let windowEvents = [];
/** `onBeforeMount` callbacks, which a real mount would have run */
let beforeMount = [];

function createFakeClient() {
  const remote = {
    Trame: {
      getState: vi.fn(async () => ({
        name: "test",
        state: { trame__client_only: [], trame__template_main: "<div/>" },
      })),
      updateState: vi.fn(async () => {}),
      subscribeToStateUpdate: vi.fn(() => ({ topic: "trame.state.topic" })),
      subscribeToActions: vi.fn(() => ({ topic: "trame.actions.topic" })),
      unsubscribe: vi.fn(async () => {}),
      lifeCycleUpdate: vi.fn(async (name) => {
        lifecycle.push(name);
      }),
    },
  };
  const client = {
    connected: false,
    isBusy: () => false,
    isConnected: () => client.connected,
    connect: vi.fn(async () => {
      client.connected = true;
      return client;
    }),
    getConfig: () => ({ application: "trame" }),
    getConnection: () => ({
      getSession: () => ({ addAttachment: () => {}, close: () => {} }),
    }),
    getRemote: () => remote,
    onBusyChange: vi.fn(() => ({ unsubscribe() {} })),
    onConnectionClose: vi.fn(),
    onConnectionError: vi.fn(),
  };
  hoisted.clients.push(client);
  return client;
}

beforeEach(() => {
  hoisted.clients = [];
  hoisted.makeClient = createFakeClient;
  lifecycle = [];
  windowEvents = [];
  beforeMount = [];
  // `TrameApp` destructures `window.Vue` at import time, so this has to exist before
  // the dynamic import below and stay the same object afterwards.
  window.Vue = {
    inject: () => window.trame,
    ref: (value) => ({ value }),
    onBeforeMount: (cb) => beforeMount.push(cb),
    onBeforeUnmount: () => {},
  };
});

async function mountTrameApp(trame) {
  window.trame = trame;
  const TrameApp = (await import("../src/components/TrameApp")).default;
  TrameApp.setup();
  beforeMount.forEach((cb) => cb());
}

it("a wrapper swap does not replay the real TrameApp connect lifecycle", async () => {
  const listen = vi
    .spyOn(window, "addEventListener")
    .mockImplementation((name) => windowEvents.push(name));
  try {
    const trame = createTrameInstance({ component: vi.fn() });
    await trame.connect({});
    await mountTrameApp(trame);

    expect(lifecycle.filter((n) => n === "client_connected")).toHaveLength(1);
    const registered = windowEvents.length;

    // What an instrumenting layer does: wrap the client, put it back, say so.
    const adopted = [];
    trame.addClientListener(() => adopted.push(trame.client));
    trame.client = Object.create(trame.client);
    trame.notifyClientReplaced();

    // The identity change reached whoever was holding a client reference...
    expect(adopted.at(-1)).toBe(trame.client);
    // ...and nothing in the connect lifecycle ran again.
    expect(lifecycle.filter((n) => n === "client_connected")).toHaveLength(1);
    expect(windowEvents).toHaveLength(registered);

    // The control that makes the assertion above mean something: a REAL connection
    // still replays it, which is the entire reason there are two channels.
    await trame.connect({});
    expect(lifecycle.filter((n) => n === "client_connected")).toHaveLength(2);
  } finally {
    listen.mockRestore();
  }
});
