import { decorate, registerDecorator } from "./decorators";

// ----------------------------------------------------------------------------
// State helper
// ----------------------------------------------------------------------------
export class WatcherManager {
  constructor() {
    this.nextId = 1;
    this.listeners = {};
  }

  watch(dependencies, callback) {
    const key = `${this.nextId++}`;
    this.listeners[key] = {
      key,
      dependencies,
      callback,
    };
    const unsubscribe = () => delete this.listeners[key];
    return unsubscribe;
  }

  notifyWatchers(changedKeys, fullState) {
    const watchers = Object.values(this.listeners);
    const keys = new Set(changedKeys);

    for (let i = 0; i < watchers.length; i++) {
      const { dependencies, callback } = watchers[i];
      if (keys.intersection(new Set(dependencies)).size) {
        const args = dependencies.map((v) => fullState[v]);
        try {
          callback(...args);
        } catch (e) {
          console.error(`Watcher error with dependencies: ${dependencies}`, e);
        }
      }
    }
  }

  getWatchers() {
    return Object.values(this.listeners);
  }
}

export class SharedState {
  /**
   * @param client managing the communication with the server
   * @param oldState previous state, when reconnecting, so the listeners and
   *        watchers registered by the UI outlive the session they were made in.
   *        Matches js-lib's `State(client, oldState)`.
   */
  constructor(client, oldState = null) {
    this.name = "Default trame application";
    this.client = client;
    // wslink subscriptions, released with Trame.unsubscribe()
    this.subscriptions = [];
    // local unsubscribe functions owned by this instance
    this.unsubscribes = [];
    this.dirtyKeys = new Set();
    this.pushFailed = false;
    this.state = {};
    this.keyTS = {};
    this.mtime = 0;
    this.listeners = oldState?.listeners || [];
    this.ready = false;
    //: A state stops emitting once its session is gone -- see `retire()`. The
    //: listener array is SHARED with the state that replaces this one, so an
    //: emit from here after that handover reaches the live UI.
    this.retired = false;
    this._watchers = oldState?._watchers || new WatcherManager();

    // bind decorator helper
    this.registerDecorator = registerDecorator;

    const updateFromServer = async (serverState) => {
      const updatedKeys = [];
      const allKeys = Object.keys(serverState);
      for (let i = 0; i < allKeys.length; i++) {
        let modified = true;
        const key = allKeys[i];
        const value = serverState[key];

        // Handle _filter field
        if (value?._filter?.length) {
          modified = false;
          const prevValue = this.state[key];
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
          this.state[key] = value;
        }
      }

      this.mtime += 1;
      const newKeys = [];
      for (let i = 0; i < updatedKeys.length; i++) {
        const key = updatedKeys[i];
        if (this.keyTS[key] === undefined) {
          newKeys.push(key);
        }
        this.keyTS[key] = this.mtime;
      }

      if (newKeys.length > 0) {
        this.notifyListeners({ type: "new-keys", keys: newKeys });
      }

      this.notifyListeners({ type: "dirty-state", keys: updatedKeys });
    };

    this.subscriptions.push(
      this.client
        .getRemote()
        .Trame.subscribeToStateUpdate(([serverState]) =>
          updateFromServer(serverState),
        ),
    );

    this.unsubscribes.push(
      this.addListener(({ type, keys }) => {
        if (type === "dirty-state") {
          this._watchers.notifyWatchers(keys, this.state);
        }
      }),
    );

    // Keep it so we can call it on disconnect
    this._updateFromServer = updateFromServer;
  }

  async loadState() {
    const { state, name } = await this.client.getRemote().Trame.getState();
    this.name = name;
    this._updateFromServer(state);
    this.notifyListeners({ type: "ready" });
    this.ready = true;
  }

  /**
   * Stop emitting, without touching the listener array: the state that replaces
   * this one inherits that array, and the components on it are live.
   *
   * A reply can already be inside wslink's decoder when the socket closes, so an
   * abandoned `loadState()` CAN still resolve, minutes later and after a fresh
   * session has loaded. Everything it does to its own copy of the state is
   * harmless; what is not harmless is the "new-keys"/"dirty-state"/"ready" it
   * emits on the way, because `ready` remounts the keyed template under a UI
   * that has already recovered.
   */
  retire() {
    this.retired = true;
  }

  notifyListeners(even) {
    if (this.retired) {
      return;
    }
    for (let i = 0; i < this.listeners.length; i++) {
      this.listeners[i](even);
    }
  }

  /**
   * @return unsubscribe function
   */
  addListener(listener) {
    this.listeners.push(listener);
    return () => this.removeListener(listener);
  }

  removeListener(listener) {
    // in place, so a listener registered on a previous session keeps working
    const index = this.listeners.indexOf(listener);
    if (index !== -1) {
      this.listeners.splice(index, 1);
    }
  }

  getAllKeys() {
    return Object.keys(this.state);
  }

  getMutableStateKeys() {
    const keysToRemove = new Set(this.state.trame__disable_mutation || []);
    return this.getAllKeys().filter((v) => !keysToRemove.has(v));
  }

  delete() {
    const skip = (e) =>
      console.log("Skipping subscription we could not release", e);
    while (this.subscriptions.length) {
      const subscription = this.subscriptions.pop();
      try {
        // Both halves are needed: wslink's unsubscribe throws synchronously on a
        // malformed argument and REJECTS on a subscription the session does not
        // hold -- the second being normal during teardown, where it would land as
        // an unhandled rejection in the middle of a reconnect.
        this.client.getRemote().Trame.unsubscribe(subscription)?.catch?.(skip);
      } catch (e) {
        skip(e);
      }
    }
    while (this.unsubscribes.length) {
      try {
        this.unsubscribes.pop()();
      } catch (e) {
        console.log("Skipping listener we could not release", e);
      }
    }
  }

  get(key) {
    if (key === undefined) {
      return this.state;
    }
    return this.state[key];
  }

  watch(keys, fn) {
    const unsubscribe = this._watchers.watch(keys, fn);

    // Call it right away with available values
    fn(...keys.map((v) => this.state[v]));

    return unsubscribe;
  }

  async set(key, value) {
    // Prevent triggering change when same value is set
    if (this.state[key] === value) {
      return;
    }

    this.mtime += 1;
    this.state[key] = value;
    this.dirty(key);
    await this.flush();
  }

  async update(obj) {
    this.mtime += 1;
    for (const [key, value] of Object.entries(obj)) {
      if (this.state[key] !== value) {
        this.state[key] = value;
        this.dirty(key);
      }
    }
    await this.flush();
  }

  canDirty(name) {
    if (!this.state.trame__client_only) {
      return true;
    }
    return !this.state.trame__client_only.includes(name);
  }

  dirty(...keys) {
    const newKeys = [];
    keys.forEach((key) => {
      if (this.canDirty(key)) {
        this.dirtyKeys.add(key);
      }
      if (this.keyTS[key] === undefined) {
        newKeys.push(key);
      }
      this.keyTS[key] = this.mtime;
    });

    // A key created on the client is new to the listeners too. Announce it the
    // same way a key coming from the server is, or a listener that builds its
    // per-key structures on "new-keys" has none when the "dirty-state" for that
    // key reaches it.
    if (newKeys.length > 0) {
      this.notifyListeners({ type: "new-keys", keys: newKeys });
    }

    // Make sure client side is aware of that change...
    this.notifyListeners({
      type: "dirty-state",
      keys,
    });
  }

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

    if (this.dirtyKeys.size && !this.client.isBusy()) {
      const waitOn = [];
      const keys = [];
      this.dirtyKeys.forEach((key) => {
        waitOn.push(decorate(this.state[key]));
        keys.push(key);
      });
      this.dirtyKeys.clear();
      const values = await Promise.all(waitOn);
      const deltaState = keys.map((key, i) => ({ key, value: values[i] }));
      let pushed = true;
      if (this.client.isConnected()) {
        try {
          await this.client.getRemote().Trame.updateState(deltaState);
        } catch (e) {
          // The transport can die between isConnected() and the call landing.
          // Keep those keys dirty so the next flush sends them, rather than
          // rejecting a promise nobody is waiting on: set() is routinely called
          // without await, so the rejection would surface as an unhandled one.
          pushed = false;
          keys.forEach((key) => this.dirtyKeys.add(key));
          // Once per outage: the busy counter flushes on every change, so an
          // unreachable server would otherwise be reported several times a second.
          if (!this.pushFailed) {
            this.pushFailed = true;
            console.log("Could not push state, keys stay dirty", keys, e);
          }
        }
      }
      this.pushFailed = !pushed;

      // Make sure we don't leave any pending update...
      // Only when the push went through: re-flushing the keys we just put back
      // would spin against a transport that is still down.
      if (pushed && this.dirtyKeys.size) {
        this.flush();
      }
    }

    // when connection died, the client is busy...
    if (!this.client.isConnected()) {
      // Handle dynamic update once disconnected
      this._updateFromServer(this.state);
    }
  }
}
