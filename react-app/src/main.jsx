import "./style.css";
import { createRoot } from "react-dom/client";
import Trame, { configDecorator, extractURLParameters } from "@kitware/trame";
import { handlePageResources } from "./setup";
import { createMessageChannelWSFactory } from "./messageChannel";
import TrameApp from "./components/TrameApp.jsx";
import TrameLoading from "./components/TrameLoading.jsx";
import TrameReconnect from "./components/TrameReconnect.jsx";
import { registerTag } from "./runtime/tags";

async function start() {
  // Check if we need to override websocket
  try {
    // Can throw exception if parent is cross-origin
    if (!window.WSLINK && window?.parent?.trameJupyter?.init) {
      window.WSLINK = window.parent.trameJupyter.init(window);
    }
  } catch (e) {
    // eslint-disable-next-line no-empty
  }

  const trame = new Trame(window.WSLINK);
  // Exposed so third-party react widgets (loaded as separate scripts, no
  // build-time import access to this app's modules) can reach the live
  // trame instance and register their own tags against the same registry
  // TrameNode resolves tags from (runtime/tags.js).
  window.trame = trame;
  window.trame.registerTag = registerTag;

  let config = configDecorator({
    application: "trame",
    useUrl: true,
  });

  // Clean URL params once config is generated
  const params = new URL(window.location).searchParams;
  const paramsToClean = [
    "sessionURL",
    "sessionManagerURL",
    "secret",
    "application",
    "remove",
  ].concat(params.get("remove")?.split(",") || []);
  paramsToClean.forEach((v) => params.delete(v));
  const cleanURL = `${window.location.pathname}${
    params.size ? "?" : ""
  }${params.toString()}${window.location.hash}`;
  window.history.replaceState({}, document.title, cleanURL);

  const root = createRoot(document.getElementById("app"));

  // Connect client to server. React doesn't need a template round-trip
  // through state to render arbitrary content before the app tree exists
  // (unlike the Vue original), so a connect failure renders directly.
  try {
    config = await trame.connect(config);
  } catch (e) {
    const message = e?.response?.error || "try/catch on connect()";
    if (config.reconnect) {
      root.render(<TrameReconnect trame={trame} message={message} />);
    } else {
      root.render(<TrameLoading message={message} />);
    }
    return;
  }

  // Forward JS error to Python
  const _error = console.error;
  console.error = (...args) => {
    try {
      if (trame.client.isConnected()) {
        trame.client.getRemote().Trame.sendError(args.join(" "));
      }
    } catch (e) {
      _error(e);
    } finally {
      _error(...args);
    }
  };
  window.addEventListener("error", (event) =>
    console.error(`${event.type}: ${event.message}`),
  );

  // Load resources (js/css)
  await handlePageResources(trame.state.get());

  root.render(<TrameApp trame={trame} useUrl />);
}

const urlParams = extractURLParameters();

if (urlParams.wsChannel) {
  window.addEventListener("message", (event) => {
    // Waiting for message initializing channel communication
    // for websocket proxying
    if (event.data !== "trame-ws-channel-init") {
      // not for us! skip
      return;
    }

    // Grab communication port and register fake WebSocket
    window.WSLINK = {
      createWebSocket: createMessageChannelWSFactory(event.ports[0]),
    };

    // Start trame client
    start();
  });
} else {
  start();
}
