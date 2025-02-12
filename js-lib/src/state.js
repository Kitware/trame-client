import { decorate } from "./decorators";
import { ListenerManager, WatcherManager } from "./listeners";

export class State {
  /**
   * State constructor
   *
   * @param {TrameClient} client managing the communication to the server
   * @param {State} oldState previous state so we can keep existing listener
   */
  constructor(client, oldState) {
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
      }).unsubscribe
    );
    this._subscriptions.push(
      this.onChange(({ type, keys }) => {
        if (type === "dirty-state") {
          this._watchers.notifyWatchers(keys, this._state);
        }
      })
    );

    this._updateFromServer = async (serverState) => {
      const updatedKeys = [];
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
      const newKeys = [];
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
        .Trame.subscribeToStateUpdate(([serverState]) =>
          this._updateFromServer(serverState)
        )
    );
  }

  /**
   * Async method used to bootstrap state content.
   */
  async loadState() {
    const { state, name } = await this._client.getRemote().Trame.getState();
    this._name = name;
    this._updateFromServer(state);
    this._ready = true;
  }

  /**
   * Return true if the given state variable can be modified and
   * therefore can be sent to the server when changed.
   *
   * @param {string} name
   * @return {boolean}
   */
  canDirty(name) {
    if (!this._state.trame__client_only) {
      return true;
    }
    return !this._state.trame__client_only.includes(name);
  }

  /**
   * Mark any local state variables dirty using their name(s)
   *
   * @param  {...string} keys
   */
  dirty(...keys) {
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
   * @param {string} key
   * @param {any} value
   *
   * @return {Promise<void>} in case you want to wait for completion
   */
  async set(key, value) {
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
   * @return {Array<string>} list of keys that compose the state
   */
  getAllKeys() {
    return Object.keys(this._state);
  }

  /**
   * Update the state with a set of key/value pair.
   *
   * @param {Map<string, any>} obj
   * @return {Promise<void>} in case you want to wait for completion
   */
  async update(obj) {
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
   * @param {string} key
   * @returns the state value for that given key
   */
  get(key) {
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
   *
   * @param {function} fn
   * @return {function} unsubscribe function
   */
  onChange(fn) {
    return this._listeners.on(fn);
  }

  /**
   * Register a listener for variable(s) change.
   * The provided method will be called with all the listed keys
   * as args.
   *
   * @param {Array<string>} keys
   * @param {function} fn
   * @return {function} unsubscribe function
   */
  watch(keys, fn) {
    const unsubscribe = this._watchers.watch(keys, fn);

    // Call it right away with available values
    fn(...keys.map((v) => this._state[v]));

    return unsubscribe;
  }

  /**
   * Delete state by unsubscribing to all its internal listeners
   */
  delete() {
    while (this._wslinkSubscriptions.length) {
      this.client
        .getRemote()
        .Trame.unsubscribe(this._wslinkSubscriptions.pop());
    }
    while (this._subscriptions.length) {
      this._subscriptions.pop()();
    }
  }

  /**
   * Push dirty data over the network.
   * If any argument (state key name(s)) is provided,
   * they will be marked dirty and pushed to the server.
   *
   * @param  {...string} keys
   */
  async flush(...keys) {
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
      const waitOn = [];
      const keys = [];
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
