import type { vtkWSLinkClient } from "@kitware/wslink/src/WsLinkClient";
import { State } from "./state";
import { decorate, registerDecorator, type Decorator } from "./decorators";
import { ListenerManager } from "./listeners";
import wslink from "./wslink";

export interface TrameConnectConfig {
  /** (/paraview) http(s) url for the launcher endpoint */
  sessionManagerURL?: string;
  /** (/ws if no launcher) ws(s) url for WebSocket session endpoint */
  sessionURL?: string;
  /** (trame) name for the session to launch */
  application?: string;
  /** (wslink-secret) authorization token for WebSocket connection */
  secret?: string;
  /** A way to inject alternative WebSocket connection */
  wsProxy?: any;
  /** Extract additional connection arguments from the current URL */
  useUrl?: boolean;
  [key: string]: any;
}

interface TrameAction {
  ref: string;
  type: string;
  method: string;
  args: any[];
}

export class Trame {
  private _initialized: boolean;
  private _nextListenerId: number;
  private _wsProxy: any;
  private _subscriptions: Array<() => void>;
  private _execAction: (action: TrameAction) => void;
  private _closeListeners: ListenerManager;
  private _errorListeners: ListenerManager;

  client: vtkWSLinkClient | null;
  state: State | null;
  config: TrameConnectConfig | null;
  refs: Record<string, any>;

  /**
   * Create a trame object that once connectect will have the following set of properties:
   *  - client: Object responsible for handling the network communication with the server.
   *  - state: Object handling the shared state between the server and client.
   *  - config: connection configuration provided as a response to the launcher.
   *  - refs: dictionary mapping a user element name to an object on which method can be called.
   *
   * @param wsProxy aim to provide a mean to provide your own websocket implementation.
   *        While it is not currently fully implemented, we use a similar infrastructure within
   *        Jupyter to reuse their communication infrastructure rather than creating our own
   *        websocket connection.
   */
  constructor(wsProxy?: any) {
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

  /**
   * Return the status of the client connection.
   * Is trame fully initialized and connected to its server or no?
   */
  isConnected(): boolean {
    return Boolean(this._initialized && this.client?.isConnected());
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
   * The secret is used to authorized the connection on the given
   * sessionURL. And works in pair with the --authKey arg.
   *
   * @return the updated configuration once fully connected
   */
  async connect(
    config?: TrameConnectConfig | null,
  ): Promise<TrameConnectConfig | undefined> {
    if (this.isConnected()) {
      console.error("Trame.connect() when already connected");
      return;
    }

    while (this._subscriptions.length) {
      try {
        this._subscriptions.pop()!();
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
      }).unsubscribe,
    );
    this._subscriptions.push(
      this.client.onConnectionClose((httpReq) => {
        this._closeListeners.emit(httpReq || "Connection closed");
      }).unsubscribe,
    );

    await this.client.connect(config ?? {});
    this.config = this.client.getConfig();
    this.state = new State(this.client, this.state);
    await this.state.loadState();
    this._initialized = true;

    // Listen to client
    const wslinkSub = this.client
      .getRemote()
      .Trame.subscribeToActions(([actions]: [TrameAction[]]) =>
        actions.map(this._execAction),
      );
    this._subscriptions.push(() =>
      this.client?.getRemote()?.Trame.unsubscribe(wslinkSub),
    );
    this.client?.getRemote()?.Trame?.lifeCycleUpdate("client_connected");

    return this.config;
  }

  /**
   * Disconnect the current connection and stop the server right away.
   */
  disconnect(): void {
    if (this.isConnected()) {
      this.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited");
      this.client?.disconnect(0);
    }
  }

  /**
   * Disconnect and ask the server to exit after the provided
   * timeout in seconds.
   *
   * If we want to disconnect but let the server running,
   * you can set the timeout to -1.
   *
   * @param timeout (default: 60s) time after
   *        which the server will exit automatically.
   */
  exit(timeout = 60): void {
    if (this.isConnected()) {
      this.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited");
      this.client?.disconnect(timeout);
    }
  }

  /**
   * Try to reconnect reusing the previously saved configuration
   * which should have a sessionURL and secret.
   */
  async reconnect(): Promise<TrameConnectConfig | undefined> {
    return this.connect(this.config);
  }

  /**
   * Register a function that should be called if the connection
   * get closed.
   *
   * @return function to call in case you want to unsubscribe.
   */
  onClose(fn: (...args: any[]) => void): () => void {
    return this._closeListeners.on(fn);
  }

  /**
   * Register a function that should be called if the connection
   * trigger an error and close.
   *
   * @return function to call in case you want to unsubscribe.
   */
  onError(fn: (...args: any[]) => void): () => void {
    return this._errorListeners.on(fn);
  }

  /**
   * Register a decorator that aim extend JavaScript structure serialization
   */
  registerDecorator(decorator: Decorator): void {
    registerDecorator(decorator);
  }

  /**
   * Trigger a method call on the server using its name
   *
   * @return result from server method call
   */
  async trigger(
    name: string,
    args: any[] = [],
    kwargs: Record<string, any> = {},
  ): Promise<any> {
    let decoratedArgs: any[] = [];
    const decoratedKwargs: Record<string, any> = {};

    if (args) {
      const decorateArgs = args.map((arg) => decorate(arg));
      decoratedArgs = await Promise.all(decorateArgs);
    }

    if (kwargs) {
      const keys: string[] = [];
      const values: Promise<any>[] = [];
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
      ?.getRemote()
      .Trame.trigger(name, decoratedArgs, decoratedKwargs);
  }
}
