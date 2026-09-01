import type { vtkWSLinkClient } from "@kitware/wslink/src/WsLinkClient";
import { decorate } from "./decorators";
import { ListenerManager, WatcherManager } from "./listeners";

export interface StateChangeEvent {
  type: "dirty-state" | "new-keys";
  keys: string[];
}

export class State {
  private _name: string;
  private _client: vtkWSLinkClient;
  private _dirtyKeys: Set<string>;
  private _state: Record<string, any>;
  private _keyTS: Record<string, number>;
  private _mtime: number;
  private _ready: boolean;
  private _listeners: ListenerManager;
  private _watchers: WatcherManager;
  private _subscriptions: Array<() => void>;
  private _wslinkSubscriptions: any[];
  private _updateFromServer: (
    serverState: Record<string, any>,
  ) => Promise<void>;

  /**
   * State constructor
   *
   * @param client managing the communication to the server
   * @param oldState previous state so we can keep existing listener
   */
  constructor(client: vtkWSLinkClient, oldState?: State | null) {
    this._name = "undefined";
    this._client = client;
    this._dirtyKeys = new Set();
    this._state = {};
    this._keyTS = {};
    this._mtime = 0;
    this._ready = false;
    this._listeners =
      oldState?._listeners || new ListenerManager("trame state change");
    this._watchers = oldState?._watchers || new WatcherManager();
    this._subscriptions = [];
    this._wslinkSubscriptions = [];
    this._subscriptions.push(
      this._client.onBusyChange((v) => {
        this.set("trame__busy", v);
        if (v === 0) {
          this.flush();
        }
      }).unsubscribe,
    );
    this._subscriptions.push(
      this.onChange(({ type, keys }) => {
        if (type === "dirty-state") {
          this._watchers.notifyWatchers(keys, this._state);
        }
      }),
    );

    this._updateFromServer = async (serverState: Record<string, any>) => {
      const updatedKeys: string[] = [];
      const allKeys = Object.keys(serverState);
      for (let i = 0; i < allKeys.length; i++) {
        let modified = true;
        const key = allKeys[i];
        const value = serverState[key];

        // Handle _filter field
        if (value?._filter?.length) {
          modified = false;
          const prevValue = this._state[key];
          const objKeys = Object.keys(value);
          for (let j = 0; !modified && j < objKeys.length; j++) {
            const subKey = objKeys[j];
            if (subKey[0] === "_") {
              continue;
            }
            if (
              prevValue === undefined ||
              prevValue[subKey] !== value[subKey]
            ) {
              modified = true;
            }
          }
        }

        if (modified) {
          updatedKeys.push(key);
          this._state[key] = value;
        }
      }

      this._mtime += 1;
      const newKeys: string[] = [];
      for (let i = 0; i < updatedKeys.length; i++) {
        const key = updatedKeys[i];
        if (this._keyTS[key] === undefined) {
          newKeys.push(key);
        }
        this._keyTS[key] = this._mtime;
      }

      if (newKeys.length > 0) {
        this._listeners.emit({ type: "new-keys", keys: newKeys });
      }
      this._listeners.emit({ type: "dirty-state", keys: updatedKeys });
    };

    this._wslinkSubscriptions.push(
      this._client
        .getRemote()
        .Trame.subscribeToStateUpdate(([serverState]: [Record<string, any>]) =>
          this._updateFromServer(serverState),
        ),
    );
  }

  /**
   * Async method used to bootstrap state content.
   */
  async loadState(): Promise<void> {
    const { state, name } = await this._client.getRemote().Trame.getState();
    this._name = name;
    this._updateFromServer(state);
    this._ready = true;
  }

  /**
   * Return true if the given state variable can be modified and
   * therefore can be sent to the server when changed.
   */
  canDirty(name: string): boolean {
    if (!this._state.trame__client_only) {
      return true;
    }
    return !this._state.trame__client_only.includes(name);
  }

  /**
   * Mark any local state variables dirty using their name(s)
   */
  dirty(...keys: string[]): void {
    keys.forEach((key) => {
      if (this.canDirty(key)) {
        this._dirtyKeys.add(key);
      }
    });
    // Make sure client side is aware of that change...
    this._listeners.emit({
      type: "dirty-state",
      keys,
    });
  }

  /**
   * Set a new value into the state with its key name and push
   * the dirty state to the server. The returned promise can
   * be use for waiting for network exchange completion.
   *
   * @return in case you want to wait for completion
   */
  async set(key: string, value: any): Promise<void> {
    // Prevent triggering change when same value is set
    if (this._state[key] === value) {
      return;
    }

    this._mtime += 1;
    this._state[key] = value;
    this._keyTS[key] = this._mtime;
    this.dirty(key);
    await this.flush();
  }

  /**
   * @return list of keys that compose the state
   */
  getAllKeys(): string[] {
    return Object.keys(this._state);
  }

  /**
   * Update the state with a set of key/value pair.
   *
   * @return in case you want to wait for completion
   */
  async update(obj: Record<string, any>): Promise<void> {
    this._mtime += 1;
    for (const [key, value] of Object.entries(obj)) {
      if (this._state[key] !== value) {
        this._state[key] = value;
        this._keyTS[key] = this._mtime;
        this.dirty(key);
      }
    }
    await this.flush();
  }

  /**
   * @returns the full state
   */
  get(): Record<string, any>;
  /**
   * @returns the state value for that given key
   */
  get(key: string): any;
  get(key?: string): any {
    if (key === undefined) {
      return this._state;
    }
    return this._state[key];
  }

  /**
   * Register function to listen to any change happening on the state.
   * The function will receive a single object with the following structure.
   *
   *    {
   *        type: "dirty-state",   # dirty-state or new-keys
   *        keys: [...],           # list of key name affected
   *    }
   *
   * @return unsubscribe function
   */
  onChange(fn: (event: StateChangeEvent) => void): () => void {
    return this._listeners.on(fn);
  }

  /**
   * Register a listener for variable(s) change.
   * The provided method will be called with all the listed keys
   * as args.
   *
   * @return unsubscribe function
   */
  watch(keys: string[], fn: (...values: any[]) => void): () => void {
    const unsubscribe = this._watchers.watch(keys, fn);

    // Call it right away with available values
    fn(...keys.map((v) => this._state[v]));

    return unsubscribe;
  }

  /**
   * Delete state by unsubscribing to all its internal listeners
   */
  delete(): void {
    while (this._wslinkSubscriptions.length) {
      this._client
        .getRemote()
        .Trame.unsubscribe(this._wslinkSubscriptions.pop());
    }
    while (this._subscriptions.length) {
      this._subscriptions.pop()!();
    }
  }

  /**
   * Push dirty data over the network.
   * If any argument (state key name(s)) is provided,
   * they will be marked dirty and pushed to the server.
   */
  async flush(...keys: (string | string[])[]): Promise<void> {
    if (keys.length) {
      keys.forEach((key) => {
        if (Array.isArray(key)) {
          this.dirty(...key);
        } else {
          this.dirty(key);
        }
      });
    }

    if (this._dirtyKeys.size && !this._client.isBusy()) {
      const waitOn: Promise<any>[] = [];
      const keys: string[] = [];
      this._dirtyKeys.forEach((key) => {
        waitOn.push(decorate(this._state[key]));
        keys.push(key);
      });
      this._dirtyKeys.clear();
      const values = await Promise.all(waitOn);
      const deltaState = keys.map((key, i) => ({ key, value: values[i] }));
      if (this._client.isConnected()) {
        await this._client.getRemote().Trame.updateState(deltaState);
      }

      // Make sure we don't leave any pending update...
      if (this._dirtyKeys.size) {
        this.flush();
      }
    }

    // when connection died, the client is busy...
    if (!this._client.isConnected()) {
      // Handle dynamic update once disconnected
      this._updateFromServer(this._state);
    }
  }
}
