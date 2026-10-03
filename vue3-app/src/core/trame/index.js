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
  let clientListeners = [];
  //: Completed connections on this page, so the first one can say it is the first.
  let completedConnections = 0;
  //: The config of the session this page is ON. A reconnect reuses it; see
  //: `trame.connect`.
  let lastConfig = null;
  //: Bumped every time `lastConfig` is replaced. An attempt remembers the generation
  //: it used, so a LATE failure of an old one cannot forget a session a newer one has
  //: since established -- object identity is not enough, because `getConfig()` may
  //: hand back the very object that was passed in.
  let configGeneration = 0;
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
   * A SECOND channel, for "`trame.client` is a different object now".
   *
   * `doConnect` is not the only thing that assigns it: an instrumenting layer can
   * wrap the client and put the wrapper back, and it does so AFTER the connect that
   * notified everyone, so anything holding a client reference is left holding the raw
   * one and the wrapper is in nobody's path.
   *
   * Deliberately NOT `notifyConnection`. A connect listener is a LIFECYCLE consumer:
   * `TrameApp`'s announces `client_connected` to the server, registers a `beforeunload`
   * and installs the template, and consumers downstream of that reset playback and
   * close editors. Replaying all of it because a wrapper was swapped in on a connection
   * that never dropped is a far larger blast radius than the problem. Client listeners
   * carry only the identity change, and `notifyConnection` keeps meaning what it meant:
   * a real, physical connection came up.
   */
  function notifyClientChanged(connection) {
    for (let i = 0; i < clientListeners.length; i++) {
      clientListeners[i](connection);
    }
  }

  trame.addClientListener = function addClientListener(listener) {
    clientListeners.push(listener);
    if (trame.client) {
      // A replay is not a connection event, and is told so by being given nothing:
      // a listener that acts on the DETAILS of a new connection must not act here.
      listener();
    }
  };

  trame.removeClientListener = function removeClientListener(listener) {
    clientListeners = clientListeners.filter((l) => l !== listener);
  };

  trame.notifyClientReplaced = notifyClientChanged;

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
    // This attempt was trying to go back to the session the page was on, and its
    // transport died doing it -- so that session is very likely gone. Forget it, or
    // every remaining retry asks for the same dead worker and the page never falls
    // back to a fresh one. Retirement rejects the DEFERRED while `doConnect` is still
    // waiting on a call that may never settle, so this cannot be left to the
    // rejection handler in `connect`.
    forgetSession(attempt);
    // Its state too, if it got as far as building one: the listener array is
    // handed to the state that replaces it, so a `loadState()` that resolves
    // after the handover -- which it can, from a reply already inside wslink's
    // decoder when the socket closed -- would otherwise emit "ready" into the
    // live UI and remount the template under a session it knows nothing about.
    attempt.state?.retire();
    attempt.reject(new Error(reason));
  }

  /**
   * Drop the remembered session, if this attempt is the one that may drop it.
   *
   * Guarded by the GENERATION it used, not by the config object: an attempt that
   * fails late must not forget a session a newer attempt has since established.
   */
  function forgetSession(attempt) {
    if (!attempt || !attempt.usedRemembered) {
      return;
    }
    if (attempt.generation === configGeneration) {
      lastConfig = null;
    }
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
    // Remembered only once an attempt has actually COMPLETED, so a half-finished
    // bootstrap cannot pin the page to a session it never loaded.
    lastConfig = trame.config;
    configGeneration += 1;
    completedConnections += 1;
    /* The client this attempt built is new too, and both channels say so: a real
     * connect is also an identity change.
     *
     * The detail it carries is about HOW THE ROUTE WAS CHOSEN, and nothing more.
     * `reusedSession` is true when this connect asked to resume the route the page
     * was already on rather than asking the session manager for a new one -- it is
     * NOT an attestation that the process on the other end is the same one. Nothing
     * on the client can attest that: the route is what was requested, the server is
     * free to answer with a different one, and a launcher may have restarted a
     * process at the same address. A consumer that needs certainty must check
     * something the server issued.
     *
     * `false` is just as narrow, and does NOT mean the page went somewhere else: a
     * caller that passes the previous route explicitly gets `false` on the very same
     * session. It means only that no remembered config was reused. Both values
     * describe route SELECTION; neither says anything about what answered. */
    notifyClientChanged({
      reusedSession: Boolean(attempt && attempt.usedRemembered),
      firstConnection: completedConnections === 1,
    });
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

    // A RECONNECT CARRIES NO CONFIG OF ITS OWN -- `TrameReconnect` calls `connect()`
    // with nothing -- and without one the client goes back to the SESSION MANAGER.
    // Behind a launcher that starts one worker process per session, that is a DIFFERENT
    // process, so the page comes back on an empty application while everything the user
    // did -- every `server.state` value they changed -- is on the old one. Measured
    // behind a launcher: the websocket URL's `sessionid` differs before and after a
    // drop, and the recovered page shows the application's initial state.
    //
    // So a reconnect asks for the session this page already had. If that session is
    // gone -- often the very reason the socket dropped -- this attempt fails, the
    // remembered config is forgotten, and the next retry asks the session manager for a
    // fresh one. That is the old behaviour, now as the fallback rather than the first
    // move, and it costs one retry tick in the case where the process really is dead.
    const reconnecting = config === undefined || config === null;
    const usedRemembered = Boolean(reconnecting && lastConfig);
    const requested = usedRemembered ? lastConfig : config;

    const attempt = { usedRemembered, generation: configGeneration };
    attempt.promise = new Promise((resolve, reject) => {
      attempt.resolve = resolve;
      attempt.reject = reject;
    });
    pending = attempt;
    doConnect(requested, attempt).then(
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
        // That session did not take us back. Let the next attempt ask for a new one
        // rather than retrying a worker that is gone ten more times.
        forgetSession(attempt);
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
