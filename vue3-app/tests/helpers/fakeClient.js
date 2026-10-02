import { vi } from "vitest";

/**
 * Minimal stand-in for the vtkWSLinkClient the vue3 app connects with.
 * It keeps its own copy of the server state and, for `Trame.unsubscribe`,
 * reproduces wslink's own contract: the session destructures `{topic}` out of
 * its argument, so an undefined subscription throws synchronously rather than
 * returning a rejected promise.
 */
export function createFakeClient(initialServerState = {}) {
  let connected = true;
  let serverState = { ...initialServerState };
  let pushFails = false;
  const stateUpdateListeners = [];

  const remote = {
    Trame: {
      getState: vi.fn(async () => ({
        name: "test-session",
        state: { ...serverState },
      })),
      updateState: vi.fn(async (changes) => {
        if (pushFails) {
          throw { code: -32099, message: "RPC call unsuccessful" };
        }
        changes.forEach(({ key, value }) => {
          serverState[key] = value;
        });
      }),
      subscribeToStateUpdate: vi.fn((cb) => {
        stateUpdateListeners.push(cb);
        return { topic: "trame.state.topic", callback: cb };
      }),
      unsubscribe: vi.fn((info) => {
        // wslink/src/WebsocketConnection/session.js
        const { topic } = info;
        return topic;
      }),
    },
  };

  const client = {
    isConnected: vi.fn(() => connected),
    isBusy: vi.fn(() => false),
    getRemote: vi.fn(() => remote),
  };

  return {
    client,
    remote,
    getServerState() {
      return serverState;
    },
    setPushFails(value) {
      pushFails = value;
    },
    setConnected(value) {
      connected = value;
    },
    pushServerState(partial) {
      serverState = { ...serverState, ...partial };
      stateUpdateListeners.forEach((cb) => cb([{ ...serverState }]));
    },
  };
}
