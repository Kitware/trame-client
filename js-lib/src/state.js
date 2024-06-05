import { decorate } from "./decorators";
import { ListenerManager, WatcherManager } from "./listeners";

export class State {
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

  async loadState() {
    const { state, name } = await this._client.getRemote().Trame.getState();
    this._name = name;
    this._updateFromServer(state);
    this._ready = true;
  }

  canDirty(name) {
    return !this._state.trame__client_only.includes(name);
  }

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

  getAllKeys() {
    return Object.keys(this._state);
  }

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

  get(key) {
    if (key === undefined) {
      return this._state;
    }
    return this._state[key];
  }

  onChange(fn) {
    return this._listeners.on(fn);
  }

  watch(keys, fn) {
    const unsubscribe = this._watchers.on(keys, fn);

    // Call it right away with available values
    fn(...keys.map((v) => this._state[v]));

    return unsubscribe;
  }

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
