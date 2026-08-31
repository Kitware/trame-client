import "./style.css";
import React from "react";
import * as ReactDOMBase from "react-dom";
import ReactDOM from "react-dom/client";
import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";
import wslink from "./core/wslink";
import { handlePageResources } from "./core/trame/setup";
import { createTrameInstance } from "./core/trame";
import { registerUserScripts } from "./user_script_handler";
import { createMessageChannelWSFactory } from "./messageChannel";
import registry from "./registry";
import registerComponents from "./components";
import TrameApp from "./components/TrameApp";
import { TrameContext } from "./renderer/hooks";
import type { TrameInstance } from "./types";

// Widget library bundles build with react/react-dom as externals and resolve
// them from the host page, so the whole page shares ONE React instance.
// Expose the full react-dom namespace (createPortal, flushSync, ...) merged
// with the client entry points (createRoot, hydrateRoot).
window.React = React;
window.ReactDOM = { ...ReactDOMBase, ...ReactDOM };

function errorPayload(tag: string, message: string) {
  return {
    version: 1,
    root: { tag, attrs: { message } },
  };
}

async function start() {
  // Check if we need to override websocket
  try {
    // Can throw exception if parent is cross-origin
    const win = window as any;
    if (!win.WSLINK && win?.parent?.trameJupyter?.init) {
      win.WSLINK = win.parent.trameJupyter.init(window);
    }
  } catch {
    // parent is cross-origin
  }

  const root = ReactDOM.createRoot(
    document.querySelector("#app") as Element,
  );
  const trame = createTrameInstance(registry) as unknown as TrameInstance;
  let config: any = wslink.configDecorator({
    application: "trame",
    useUrl: true,
  });

  // Clean URL params once config is generated
  const params = new URL(window.location.href).searchParams;
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

  // Handle connection
  trame.addConnectListener(() => {
    trame.client.onConnectionError((httpReq: any) => {
      reportWsError(httpReq?.response?.error || "Connection error");
    });
    trame.client.onConnectionClose((httpReq: any) => {
      reportWsError(httpReq?.response?.error || "Connection closed");
    });
  });

  // Handle client/server connection error
  function reportWsError(message: string) {
    if (trame && trame.state) {
      trame.state.set("trame_error_report_msg", message);
      let templateName = "trame__template_main";
      const urlParams = vtkURLExtract.extractURLParameters() as any;
      if (urlParams.ui) {
        templateName = `trame__template_${urlParams.ui}`;
      }
      if (config.reconnect) {
        trame.state.set(
          templateName,
          trame.state.get("trame__template_error_reconnect") ||
            errorPayload("trame-reconnect", message),
        );
      } else {
        trame.state.set(
          templateName,
          trame.state.get("trame__template_error") ||
            errorPayload("trame-loading", message),
        );
      }
    } else {
      root.unmount();
      const app = document.querySelector("#app");
      if (app) app.innerHTML = message;
    }
  }

  // Connect client to server
  try {
    config = await trame.connect(config);
  } catch (e) {
    reportWsError((e as any)?.response?.error || "try/catch on connect()");
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

  // Setup trame app
  registerComponents(registry);

  // Load resources (js/css) and registry plugins
  const uses: any[] = await handlePageResources(trame.state.state);
  for (let i = 0; i < uses.length; i++) {
    if (uses[i]) {
      const { name, plugin, options } = uses[i];
      registry.use(plugin, ...options);
      console.info(`registry.use(${name})`);
    }
  }

  root.render(
    <TrameContext.Provider value={trame}>
      <TrameApp useUrl />
    </TrameContext.Provider>,
  );

  registerUserScripts();
}

const urlParams = vtkURLExtract.extractURLParameters() as any;

if (urlParams.wsChannel) {
  window.addEventListener("message", (event) => {
    // Waiting for message initializing channel communication
    // for websocket proxying
    if (event.data !== "trame-ws-channel-init") {
      // not for us! skip
      return;
    }

    // Grab communication port and register fake WebSocket
    (window as any).WSLINK = {
      createWebSocket: createMessageChannelWSFactory(event.ports[0]),
    };

    // Start trame client
    start();
  });
} else {
  start();
}
