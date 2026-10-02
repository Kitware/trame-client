import { beforeEach, describe, expect, it, vi } from "vitest";

const hoisted = vi.hoisted(() => ({ clients: [], makeClient: null }));

vi.mock("../src/core/wslink", () => ({
  default: {
    createClient: () => hoisted.makeClient(),
    configDecorator: (config) => config,
  },
}));

const { createTrameInstance } = await import("../src/core/trame");

/**
 * A client whose bootstrap can be held open, the way a real one is when the
 * socket dies with `Trame.getState` in flight: wslink never settles that call.
 */
function createFakeClient() {
  const closeListeners = [];
  const errorListeners = [];
  const client = {
    id: hoisted.clients.length,
    serverState: { trame__client_only: [], trame__template_main: "<div/>" },
    /** when true, getState() returns a promise that never settles */
    holdBootstrap: false,
    connectFails: null,
    connected: false,
    isBusy: () => false,
    isConnected: () => client.connected,
    connect: vi.fn(async () => {
      if (client.connectFails) {
        throw client.connectFails;
      }
      client.connected = true;
      return client;
    }),
    getConfig: () => ({ application: "trame", client: client.id }),
    getConnection: () => ({
      getSession: () => ({ addAttachment: () => {} }),
    }),
    getRemote: () => ({
      Trame: {
        getState: vi.fn(() =>
          client.holdBootstrap
            ? new Promise(() => {})
            : Promise.resolve({
                name: "test",
                state: { ...client.serverState },
              }),
        ),
        updateState: vi.fn(async () => {}),
        subscribeToStateUpdate: vi.fn(() => ({ topic: "trame.state.topic" })),
        unsubscribe: vi.fn((info) => info.topic),
      },
    }),
    onConnectionClose: vi.fn((cb) => closeListeners.push(cb)),
    onConnectionError: vi.fn((cb) => errorListeners.push(cb)),
    /** what wslink does when the socket dies: fire close, settle nothing */
    killTransport() {
      client.connected = false;
      closeListeners.forEach((cb) => cb("Connection closed"));
    },
    raiseError() {
      errorListeners.forEach((cb) => cb("Connection error"));
    },
  };
  hoisted.clients.push(client);
  return client;
}

beforeEach(() => {
  hoisted.clients = [];
  hoisted.makeClient = createFakeClient;
});

/** let the pending microtasks run without waiting on anything that may hang */
const settle = () => new Promise((resolve) => setTimeout(resolve, 0));

describe("trame.connect", () => {
  it("connects and exposes the state", async () => {
    const trame = createTrameInstance({});

    const config = await trame.connect({});

    expect(config).toMatchObject({ application: "trame" });
    expect(trame.state.get("trame__template_main")).toBe("<div/>");
    expect(hoisted.clients).toHaveLength(1);
  });

  it("two overlapping calls share one attempt and one client", async () => {
    const trame = createTrameInstance({});

    const [first, second] = await Promise.all([
      trame.connect({}),
      trame.connect({}),
    ]);

    expect(hoisted.clients).toHaveLength(1);
    expect(first).toBe(second);
  });

  it("a later call after a successful one starts a fresh client", async () => {
    const trame = createTrameInstance({});
    await trame.connect({});

    await trame.connect({});

    expect(hoisted.clients).toHaveLength(2);
  });

  it("a rejected bootstrap does not block the next attempt", async () => {
    const trame = createTrameInstance({});
    hoisted.makeClient = () => {
      const client = createFakeClient();
      client.connectFails = new Error("no route to host");
      return client;
    };

    await expect(trame.connect({})).rejects.toThrow("no route to host");

    // the server comes back; a failed handshake leaves the client reusable, as
    // vtk.js's does -- what matters is that the attempt did not stay pending
    hoisted.clients[0].connectFails = null;
    await expect(trame.connect({})).resolves.toMatchObject({
      application: "trame",
    });
  });

  it("losing the transport mid-bootstrap retires that attempt", async () => {
    const trame = createTrameInstance({});
    hoisted.makeClient = () => {
      const client = createFakeClient();
      client.holdBootstrap = true;
      return client;
    };

    // The state RPC is in flight and will never settle, as wslink leaves it.
    const held = trame.connect({});
    const rejected = expect(held).rejects.toThrow(
      "Connection closed while connecting",
    );
    await settle();
    hoisted.clients[0].killTransport();
    await rejected;
  });

  it("a retry after a lost bootstrap builds a fresh client and connects", async () => {
    const trame = createTrameInstance({});
    hoisted.makeClient = () => {
      const client = createFakeClient();
      client.holdBootstrap = true;
      return client;
    };

    const held = trame.connect({});
    held.catch(() => {});
    await settle();
    hoisted.clients[0].killTransport();
    await settle();

    // THE REGRESSION: joining the held attempt here can never create a client,
    // because the call it is waiting on is one wslink will never settle.
    hoisted.makeClient = createFakeClient;
    const config = await trame.connect({});

    expect(config).toMatchObject({ application: "trame" });
    expect(hoisted.clients).toHaveLength(2);
    expect(trame.state.get("trame__template_main")).toBe("<div/>");
  });

  it("a connection error mid-bootstrap retires the attempt too", async () => {
    const trame = createTrameInstance({});
    hoisted.makeClient = () => {
      const client = createFakeClient();
      client.holdBootstrap = true;
      return client;
    };

    const held = trame.connect({});
    held.catch(() => {});
    await settle();
    hoisted.clients[0].raiseError();
    await settle();

    hoisted.makeClient = createFakeClient;
    await expect(trame.connect({})).resolves.toMatchObject({
      application: "trame",
    });
  });

  it("a retired attempt that settles late does not take the instance back", async () => {
    const trame = createTrameInstance({});
    let releaseHeld;
    hoisted.makeClient = () => {
      const client = createFakeClient();
      const remote = client.getRemote;
      client.getRemote = () => {
        const api = remote();
        api.Trame.getState = () =>
          new Promise((resolve) => {
            releaseHeld = () =>
              resolve({ name: "stale", state: { ...client.serverState } });
          });
        return api;
      };
      return client;
    };

    const held = trame.connect({});
    held.catch(() => {});
    await settle();
    const staleClient = hoisted.clients[0];
    staleClient.killTransport();
    await settle();

    hoisted.makeClient = createFakeClient;
    await trame.connect({});
    const liveState = trame.state;
    const liveClient = trame.client;

    // the old bootstrap finally answers, long after it was retired
    releaseHeld();
    await settle();

    expect(trame.state).toBe(liveState);
    expect(trame.client).toBe(liveClient);
    expect(trame.client).not.toBe(staleClient);
  });

  it("losing the transport of a LIVE session does not silence its state", async () => {
    // The close listener an attempt registers outlives the attempt, and the
    // ordinary drop fires it on a session that COMPLETED. Retiring that state
    // would silence the only path that can show the reconnect screen: the close
    // handler sets `trame__template_main`, which has to reach the template.
    const trame = createTrameInstance({});
    await trame.connect({});
    const listener = vi.fn();
    trame.state.addListener(listener);

    hoisted.clients[0].killTransport();
    await settle();

    await trame.state.set("trame__template_main", "<trame-reconnect/>");

    expect(trame.state.retired).toBe(false);
    expect(listener).toHaveBeenCalled();
  });

  it("a retired bootstrap must not notify current listeners", async () => {
    // A reply can already be inside wslink's decoder when the socket closes, so
    // an abandoned loadState() CAN resolve -- after a fresh session has loaded.
    // The listener array is handed down the chain of states, so an emit from the
    // retired one reaches the live UI, and its "ready" remounts the keyed
    // template under a session that has already recovered.
    const trame = createTrameInstance({});
    await trame.connect({}); // A
    const listener = vi.fn();
    trame.state.addListener(listener); // a mounted component

    let releaseHeld;
    hoisted.makeClient = () => {
      const client = createFakeClient();
      const remote = client.getRemote;
      client.getRemote = () => {
        const api = remote();
        api.Trame.getState = () =>
          new Promise((resolve) => {
            releaseHeld = () =>
              resolve({
                name: "stale",
                state: {
                  ...client.serverState,
                  late_key: "from the dead session",
                },
              });
          });
        return api;
      };
      return client;
    };
    const held = trame.connect({}); // B, interrupted mid-bootstrap
    held.catch(() => {});
    await settle();
    hoisted.clients[1].killTransport();
    await settle();

    hoisted.makeClient = createFakeClient;
    await trame.connect({}); // C, the session the user is now on
    const liveState = trame.state;
    listener.mockClear();

    releaseHeld(); // B's reply finally decodes
    await settle();

    expect(listener).not.toHaveBeenCalled();
    expect(trame.state).toBe(liveState);
    expect(trame.state.get("late_key")).toBeUndefined();
  });

  it("a connect listener is notified once per successful attempt", async () => {
    const trame = createTrameInstance({});
    const listener = vi.fn();
    trame.addConnectListener(listener);

    await trame.connect({});
    expect(listener).toHaveBeenCalledTimes(1);

    await trame.connect({});
    expect(listener).toHaveBeenCalledTimes(2);
  });
});
