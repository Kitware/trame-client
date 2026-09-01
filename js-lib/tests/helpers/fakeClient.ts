import { vi } from "vitest";

export type TriggerHandler = (...args: any[]) => any;

/**
 * Minimal stand-in for a vtkWSLinkClient connected to a trame server.
 * It keeps its own copy of the server-side state. Per trame_server's
 * `update_state` RPC (trame.state.update), the server pushes state changes
 * back over "trame.state.topic" with `skip_last_active_client=True`, so the
 * client that sent an update does not get its own values echoed back; use
 * `pushServerState()` to simulate a genuine server/other-client broadcast.
 */
export function createFakeClient(initialServerState: Record<string, any> = {}) {
  let connected = false;
  let serverState: Record<string, any> = { ...initialServerState };
  const stateUpdateListeners: Array<(args: [Record<string, any>]) => void> = [];
  const actionsListeners: Array<(args: [any[]]) => void> = [];
  const closeListeners: Array<(...args: any[]) => void> = [];
  const errorListeners: Array<(...args: any[]) => void> = [];
  const triggerHandlers: Record<string, TriggerHandler> = {};

  const lifeCycleUpdate = vi.fn(async (_phase: string) => {});

  const remote = {
    Trame: {
      getState: vi.fn(async () => ({
        name: "test-session",
        state: serverState,
      })),
      updateState: vi.fn(
        async (changes: Array<{ key: string; value: any }>) => {
          // Mirrors trame_server: the sender's own values are applied
          // locally but not echoed back to it (skip_last_active_client).
          changes.forEach(({ key, value }) => {
            serverState[key] = value;
          });
        },
      ),
      trigger: vi.fn(
        async (
          name: string,
          args: any[] = [],
          kwargs: Record<string, any> = {},
        ) => {
          const handler = triggerHandlers[name];
          if (!handler) {
            throw new Error(`No trigger registered for "${name}"`);
          }
          return handler(...args, kwargs);
        },
      ),
      subscribeToStateUpdate: vi.fn(
        (cb: (args: [Record<string, any>]) => void) => {
          stateUpdateListeners.push(cb);
          return { id: `state-${stateUpdateListeners.length}` };
        },
      ),
      subscribeToActions: vi.fn((cb: (args: [any[]]) => void) => {
        actionsListeners.push(cb);
        return { id: `actions-${actionsListeners.length}` };
      }),
      unsubscribe: vi.fn(),
      lifeCycleUpdate,
    },
  };

  const client = {
    isConnected: vi.fn(() => connected),
    isBusy: vi.fn(() => false),
    connect: vi.fn(async (_config: any) => {
      connected = true;
      return client;
    }),
    disconnect: vi.fn((_timeout: number) => {
      connected = false;
      closeListeners.forEach((cb) => cb("Connection closed"));
    }),
    getConfig: vi.fn(() => ({ application: "trame" })),
    getRemote: vi.fn(() => remote),
    onConnectionError: vi.fn((cb: (...args: any[]) => void) => {
      errorListeners.push(cb);
      return { unsubscribe: () => {} };
    }),
    onConnectionClose: vi.fn((cb: (...args: any[]) => void) => {
      closeListeners.push(cb);
      return { unsubscribe: () => {} };
    }),
    onBusyChange: vi.fn(() => ({ unsubscribe: () => {} })),
  };

  return {
    client,
    remote,
    registerTrigger(name: string, handler: TriggerHandler) {
      triggerHandlers[name] = handler;
    },
    getServerState() {
      return serverState;
    },
    /** Simulate the server unilaterally broadcasting new/changed state, e.g. from another client. */
    pushServerState(partial: Record<string, any>) {
      serverState = { ...serverState, ...partial };
      stateUpdateListeners.forEach((cb) => cb([{ ...serverState }]));
    },
    emitAction(action: any) {
      actionsListeners.forEach((cb) => cb([[action]]));
    },
    emitClose(info: any) {
      closeListeners.forEach((cb) => cb(info));
    },
    emitError(info: any) {
      errorListeners.forEach((cb) => cb(info));
    },
  };
}

export type FakeClient = ReturnType<typeof createFakeClient>;
