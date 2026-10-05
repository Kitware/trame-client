import wslink from "../wslink";
import { SharedState } from "./state";
import { decorate, setAddAttachment } from "./decorators";
import utils from "../../utils";

export function createTrameInstance(app) {
  const trame = {
    app,
    client: null,
    state: null,
    config: null,
    utils,
    refs: {},
  };
  let listeners = [];
  //: The config of the session this page is on, kept once a connection has
  //: actually completed so a half-finished bootstrap cannot pin the page to a
  //: session it never loaded. A reconnect goes back to it; see `trame.connect`.
  let lastConfig = null;
  let initialized = false;
  //: The connect attempt in flight, if any. An attempt OWNS the transport it is
  //: bootstrapping on: wslink never settles a call that was in flight when the
  //: socket closed, so an attempt whose transport dies between `connect()` and
  //: the end of `loadState()` would hang on its own `getState` forever -- and,
  //: being what every later connect() joins, would wedge reconnection
  //: permanently. Losing the transport RETIRES the attempt instead.
  let pending = null;

  function isConnected() {
    return initialized && trame?.client?.isConnected();
  }

  function notifyConnection() {
    for (let i = 0; i < listeners.length; i++) {
      listeners[i]();
    }
  }

  trame.addConnectListener = function addConnectListener(listener) {
    listeners.push(listener);
    if (isConnected()) {
      listener();
    }
  };

  trame.removeConnectListener = function removeConnectListener(listener) {
    listeners = listeners.filter((l) => l !== listener);
  };

  /**
   * Give up on an attempt whose transport is gone. The next connect() then
   * starts a fresh client rather than joining a promise that can never settle,
   * and anything already waiting on this one is told rather than left hanging.
   */
  function retireAttempt(attempt, reason) {
    // A COMPLETED attempt has handed its client and state to `trame`, and its
    // close listener still fires when that session later dies -- which is the
    // ordinary drop, where the state must keep emitting so the UI can show the
    // reconnect screen. Only an attempt still in its bootstrap is retired.
    if (attempt.retired || attempt.completed) {
      return;
    }
    attempt.retired = true;
    if (pending === attempt) {
      pending = null;
    }
    // Its state too, if it got as far as building one: the listener array is
    // handed to the state that replaces it, so a `loadState()` that resolves
    // after the handover -- which it can, from a reply already inside wslink's
    // decoder when the socket closed -- would otherwise emit "ready" into the
    // live UI and remount the template under a session it knows nothing about.
    attempt.state?.retire();
    attempt.reject(new Error(reason));
  }

  async function doConnect(config, attempt) {
    if (!trame.client) {
      trame.client = wslink.createClient();
    }

    const previousState = trame.state;
    if (previousState) {
      previousState.delete();
      trame.client = wslink.createClient();
    }

    const client = trame.client;
    // Registered BEFORE connecting, because the window this closes is after
    // `client.connect()` has resolved: a transport lost during the handshake
    // rejects `connect()` on its own, one lost while `loadState()` is in flight
    // does not reject anything at all.
    client.onConnectionClose(() =>
      retireAttempt(attempt, "Connection closed while connecting"),
    );
    client.onConnectionError(() =>
      retireAttempt(attempt, "Connection error while connecting"),
    );

    if (!client.isConnected()) {
      await client.connect(config);
    }

    // A retired attempt must not touch `trame`: a later attempt may already own
    // it. Checked at every point this function can resume on.
    if (attempt.retired) {
      return undefined;
    }

    setAddAttachment(client.getConnection().getSession().addAttachment);
    // The previous state is handed over so the listeners and watchers the UI
    // registered survive the session: the components that own them are not
    // remounted by a reconnect, and a state nobody listens to can no longer
    // refresh anything.
    trame.state = new SharedState(client, previousState);
    // Named on the attempt BEFORE it can emit anything, so losing the transport
    // during the load below silences this state rather than the live one.
    attempt.state = trame.state;
    trame.config = client.getConfig();
    await trame.state.loadState();

    if (attempt.retired) {
      return undefined;
    }

    // Before anything can observe the new session: from here on this attempt
    // owns `trame`, and its transport dying is an ordinary drop rather than an
    // abandoned bootstrap.
    attempt.completed = true;
    initialized = true;
    lastConfig = trame.config;
    notifyConnection();
    return trame.config;
  }

  trame.connect = function connect(config) {
    // Re-entrant: `?reconnect=auto` retries on a timer and does not wait for
    // the attempt in flight, so without this a successful connection is torn
    // down by the next tick. The attempt is a deferred rather than the
    // `doConnect` promise itself, so that losing the transport can retire it
    // even though `doConnect` is stuck on a call wslink will never settle.
    if (pending) {
      return pending.promise;
    }

    const attempt = {};
    attempt.promise = new Promise((resolve, reject) => {
      attempt.resolve = resolve;
      attempt.reject = reject;
    });
    pending = attempt;
    // A reconnect carries no config of its own -- `TrameReconnect` calls
    // `connect()` with nothing -- and without one the client goes back to the
    // session manager, which behind a launcher hands out a DIFFERENT worker
    // process: the page comes back empty while everything the user did is on the
    // old one. So a reconnect goes back to the session this page is on, and only
    // to that one. If it is really gone, `TrameReconnect` gives up after its
    // retries and asks for a page reload.
    doConnect(config ?? lastConfig, attempt).then(
      (result) => {
        if (pending === attempt) {
          pending = null;
        }
        // Both are no-ops once the attempt has been retired: a late settlement
        // of a retired attempt changes nothing.
        attempt.resolve(result);
      },
      (error) => {
        if (pending === attempt) {
          pending = null;
        }
        attempt.reject(error);
      },
    );
    return attempt.promise;
  };

  trame.trigger = async function trigger(name, args = [], kwargs = {}) {
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

    return await trame.client
      .getRemote()
      .Trame.trigger(name, decoratedArgs, decoratedKwargs);
  };

  // Make it available globally
  window.trame = trame;

  return trame;
}
