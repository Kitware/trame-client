import "./style.css";
import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";
import wslink from "./core/wslink";
import { handlePageResources, loadScript } from "./core/trame/setup";
import { createTrameInstance } from "./core/trame";
import TrameUse from "./use";

const { createApp } = window.Vue;

async function start() {
  // Check if we need to override websocket
  try {
    // Can throw exception if parent is cross-origin
    if (window?.parent?.trameJupyter?.init) {
      window.WSLINK = window.parent.trameJupyter.init(window);
    }
  } catch (e) {
    // eslint-disable-next-line
  }

  const app = createApp({ template: `<trame-app use-url />` });
  let trame = createTrameInstance(app);
  let config = wslink.configDecorator({
    application: "trame",
    useUrl: true,
  });

  // Handle connection
  trame.addConnectListener(() => {
    trame.client.onConnectionError((httpReq) => {
      reportWsError(httpReq?.response?.error || "Connection error");
    });
    trame.client.onConnectionClose((httpReq) => {
      reportWsError(httpReq?.response?.error || "Connection closed");
    });
  });

  // Handle client/server connection error
  function reportWsError(message) {
    if (trame) {
      console.log("about to replace template", message);
      trame.state.set("trame_error_report_msg", message);
      let templateName = "trame__template_main";
      if (vtkURLExtract.extractURLParameters().ui) {
        templateName = `trame__template_${
          vtkURLExtract.extractURLParameters().ui
        }`;
      }
      if (config.reconnect) {
        trame.state.set(
          templateName,
          trame.state.get("trame__template_error_reconnect") ||
            `<trame-reconnect message="${message}"/>`
        );
      } else {
        trame.state.set(
          templateName,
          trame.state.get("trame__template_error") ||
            `<trame-loading message="${message}"/>`
        );
      }
      console.log("template replaced", trame.state.get(templateName));
    } else {
      app.unmount();
      document.querySelector("#app").innerHTML(message);
    }
  }

  // Connect client to server
  try {
    config = await trame.connect(config);
  } catch (e) {
    reportWsError("try/catch on connect()");
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
    console.error(`${event.type}: ${event.message}`)
  );

  // Setup trame app
  app.use(TrameUse);
  app.provide("trame", trame);

  // Load resources (js/css)
  const uses = await handlePageResources(trame.state.state);
  for (let i = 0; i < uses.length; i++) {
    app.use(...uses[i]);
    console.info(`Vue.use(${uses[i]})`);
  }

  app.mount("#app");
}

// Initialize service worker to override headers for SharedArrayBuffer
// > Cross-Origin-Opener-Policy: same-origin
// > Cross-Origin-Embedder-Policy: require-corp
if (vtkURLExtract.extractURLParameters().enableSharedArrayBufferServiceWorker) {
  loadScript("coi-serviceworker.min.js");
}

start();
