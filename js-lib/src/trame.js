import { State } from "./state";
import { decorate, registerDecorator } from "./decorators";
import { ListenerManager } from "./listeners";
import wslink from "./wslink";
import vtkWSLinkClient from "@kitware/vtk.js/IO/Core/WSLinkClient";

/**
 * @typedef TrameConnectConfig
 * @type {object}
 * @property {string} sessionManagerURL (/paraview) http(s) url for the launcher endpoint
 * @property {string} sessionURL (/ws if no launcher) ws(s) url for WebSocket session endpoint
 * @property {string} application (trame) name for the session to launch
 * @property {string} secret (wslink-secret) authorization token for WebSocket connection
 * @property {object} wsProxy A way to inject alternative WebSocket connection
 */

/**
 * @typedef {Object} Decorator
 * @property {number} priority
 * @property {function} decorate: async function aiming to return the value as is or modify it.
 */

export class Trame {
  /**
   * Create a trame object that once connectect will have the following set of properties:
   *  - client: Object responsible for handling the network communication with the server.
   *  - state: Object handling the shared state between the server and client.
   *  - config: connection configuration provided as a response to the launcher.
   *  - refs: dictionary mapping a user element name to an object on which method can be called.
   *
   * @param {Object} wsProxy aim to provide a mean to provide your own websocket implementation.
   *        While it is not currently fully implemented, we use a similar infrastructure within
   *        Jupyter to re-use their communication infrastructure rather than creating our own
   *        websocket connection.
   */
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
    /**@type{vtkWSLinkClient}*/
    this.client = null;
    /**@type{State}*/
    this.state = null;
    /**@type{TrameConnectConfig}*/
    this.config = null;
    /**@type{Object.<string,any>}*/
    this.refs = {};
  }

  /**
   * Return the status of the client connection.
   * Is trame fully initialized and connected to its server or no?
   *
   * @return {Boolean}
   */
  isConnected() {
    return this._initialized && this.client?.isConnected();
  }

  /**
   * Connect to a remote server using the provided configuration.
   *
   * The configuration aimed to be used by a launcher to start a
   * new server process so the client can connect to it.
   * While we could find several implementation of a launcher,
   * the client will behave as follow:
   *
   * 0. If the key "sessionURL" is part of the configuration,
   *    the client will directly connect to it using that URL
   *    for its WebSocket. If not, move to 1.
   *
   * 1. The key "sessionManagerURL" will be used to submit
   *    an HTTP/POST request with the content of that config object.
   *    If not provided, sessionManagerURL="/paraview".
   *
   * 2a. If the launcher reply successfully, the configuration will be
   *     extended with some additional key/pair. The "sessionURL" key
   *     should be available and then use to establish a WebSocket
   *     connection to the server side process.
   *
   * 2b. If the launcher fails (no launcher, like local setup), we try
   *     to establish a WebSocket connection to "ws://{host}:{port}/ws"
   *
   * The default launcher expect an "application" key that will be use
   * to select which command line should be executed to start the new
   * user process. On top of that key, you can add as many other keys
   * as you want, which could then be used to template the command line
   * for that given user server session.
   *
   * Another behavior of the default launcher is to generate a one-time
   * token to prevent un-authorized access to an established session.
   * The launcher will tend to return a config like:
   *
   *    {...input, secret, sessionURL}
   *
   * The secret is used to autorized the connection on the given
   * sessionURL. And works in pair with the --authKey arg.
   *
   *
   * @param {TrameConnectConfig} config
   * @return {Promise<TrameConnectConfig>} the updated configuration once
   *         fully connected
   */
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

  /**
   * Disconnect the current connection and stop the server right away.
   */
  disconnect() {
    if (this.isConnected()) {
      this.client.disconnect(0);
    }
  }

  /**
   * Diconnect and ask the server to exit after the provided
   * timeout in seconds.
   *
   * If we want to disconnect but let the server running,
   * you can set the timeout to -1.
   *
   * @param {number} timeout (default: 60s) time after
   *        which the server will exit automatically.
   */
  exit(timeout = 60) {
    if (this.isConnected()) {
      this.client.disconnect(timeout);
    }
  }

  /**
   * Try to reconnect reusing the previously saved configuration
   * which should have a sessionURL and secret.
   *
   * @return {Promise<TrameConnectConfig>}
   */
  async reconnect() {
    return this.connect(this.config);
  }

  /**
   * Register a function that should be called if the connection
   * get closed.
   *
   * @param {function} fn
   * @return {function} to call in case you want to unsubscribe.
   */
  onClose(fn) {
    return this._closeListeners.on(fn);
  }

  /**
   * Register a function that should be called if the connection
   * trigger an error and close.
   *
   * @param {function} fn
   * @return {function} to call in case you want to unsubscribe.
   */
  onError(fn) {
    return this._errorListeners.on(fn);
  }

  /**
   * Register a decorator that aim extend JavaScript structure serialization
   *
   * @param {Decorator} decorator
   */
  registerDecorator(decorator) {
    registerDecorator(decorator);
  }

  /**
   * Trigger a method call on the server using its name
   *
   * @param {string} name
   * @param {Array<any>} args
   * @param {Map<string, any>} kwargs
   * @return {Promise<any>} result from server method call
   */
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
