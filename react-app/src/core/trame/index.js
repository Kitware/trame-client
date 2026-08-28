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
  let initialized = false;

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

  trame.connect = async function connect(config) {
    if (!trame.client) {
      trame.client = wslink.createClient();
    }

    if (trame.state) {
      trame.state.delete();
      trame.client = wslink.createClient();
    }

    if (!trame.client.isConnected()) {
      await trame.client.connect(config);
    }

    setAddAttachment(trame.client.getConnection().getSession().addAttachment);
    trame.state = new SharedState(trame.client);
    trame.config = trame.client.getConfig();
    await trame.state.loadState();

    initialized = true;
    notifyConnection();
    return trame.config;
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
