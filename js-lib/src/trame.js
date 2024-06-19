import { State } from "./state";
import { decorate, registerDecorator } from "./decorators";
import { ListenerManager } from "./listeners";
import wslink from "./wslink";

export class Trame {
  constructor(wsProxy) {
    this._initialized = false;
    this._nextListenerId = 1;
    this._wsProxy = wsProxy;
    this._subscriptions = [];
    this._execAction = (action) => {
      const { ref, type } = action;
      const obj = this.refs[ref];
      if (obj && type === "method") {
        const { method, args } = action;
        obj[method](...args);
      }
    };
    this._closeListeners = new ListenerManager("trame connection close");
    this._errorListeners = new ListenerManager("trame connection error");

    // public objects
    this.client = null;
    this.state = null;
    this.config = null;
    this.refs = {};
  }

  isConnected() {
    return this._initialized && this.client?.isConnected();
  }

  async connect(config) {
    if (this.isConnected()) {
      console.error("Trame.connect() when already connected");
      return;
    }

    while (this._subscriptions.length) {
      try {
        this._subscriptions.pop()();
      } catch (e) {
        console.error("Try to unsubscribe from previous trame client", e);
      }
    }

    if (this.state) {
      this.state.delete();
    }

    this.client = wslink.createClient();

    // Connection close/error listeners
    this._subscriptions.push(
      this.client.onConnectionError((httpReq) => {
        this._errorListeners.emit(httpReq || "Connection error");
      }).unsubscribe
    );
    this._subscriptions.push(
      this.client.onConnectionClose((httpReq) => {
        this._closeListeners.emit(httpReq || "Connection closed");
      }).unsubscribe
    );

    await this.client.connect(config);
    this.config = this.client.getConfig();
    this.state = new State(this.client, this.state);
    await this.state.loadState();
    this._initialized = true;

    // Listen to client
    const wslinkSub = this.client
      .getRemote()
      .Trame.subscribeToActions(([actions]) => actions.map(this._execAction));
    this._subscriptions.push(() =>
      this.client?.getRemote()?.Trame.unsubscribe(wslinkSub)
    );
    this.client?.getRemote()?.Trame?.lifeCycleUpdate("client_connected");
    window.addEventListener("beforeunload", () =>
      this.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited")
    );

    return this.config;
  }

  disconnect() {
    if (this.isConnected()) {
      this.client.disconnect(0);
    }
  }

  exit(timeout = 60) {
    if (this.isConnected()) {
      this.client.disconnect(timeout);
    }
  }

  async reconnect() {
    return this.connect(this.config);
  }

  onClose(fn) {
    return this._closeListeners.on(fn);
  }

  onError(fn) {
    return this._errorListeners.on(fn);
  }

  registerDecorator(decorator) {
    registerDecorator(decorator);
  }

  async trigger(name, args = [], kwargs = {}) {
    let decoratedArgs = [];
    const decoratedKwargs = {};

    if (args) {
      const decorateArgs = args.map((arg) => decorate(arg));
      decoratedArgs = await Promise.all(decorateArgs);
    }

    if (kwargs) {
      const keys = [];
      const values = [];
      Object.entries(kwargs).forEach((entry) => {
        keys.push(entry[0]);
        values.push(decorate(entry[1]));
      });

      const resolvedValues = await Promise.all(values);
      for (let i = 0; i < keys.length; i++) {
        decoratedKwargs[keys[i]] = resolvedValues[i];
      }
    }

    return await this.client
      .getRemote()
      .Trame.trigger(name, decoratedArgs, decoratedKwargs);
  }
}
