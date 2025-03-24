import Vue from 'vue';
import App from './components/App';
import Trame from './use';

import vtkURLExtract from '@kitware/vtk.js/Common/Core/URLExtract';

import { setAddAttachment } from './components/Connect/trame/decorators';
import { handlePageUpdate, loadScript, GLOBAL_VUE_OPTIONS } from './components/Connect/trame/state';
import wslink from './components/Connect/wslink';

const DEFAULT_CONNECTION_NAME = 'TrameConnect';

function reportWsError() {
  const status = wslink.getStatus(DEFAULT_CONNECTION_NAME);
  const elem = document.querySelector('.trame__message');
  if (elem) {
    elem.innerHTML = status.message || status.type;
  } else {
    console.error('WsError', status.message || status.type);
  }
}

async function initializeApplication(Vue) {
  // Check if we need to override websocket
  try {
    // Can throw exception if parent is cross-origin
    if (window?.parent?.trameJupyter?.init) {
      window.WSLINK = window.parent.trameJupyter.init(window);
    }
  } catch (e) {
    // eslint-disable-next-line
  }

  // Add default trame components
  Vue.use(Trame);

  // Connect to server
  const config = wslink.configDecorator({
    application: 'trame',
    useUrl: true,
  });
  const client = wslink.getClient(DEFAULT_CONNECTION_NAME);
  try {
    await client.connect(config);
  } catch (e) {
    reportWsError();
    return;
  }

  // Attach basic error feedback
  client.onConnectionError(reportWsError);
  client.onConnectionClose(reportWsError);

  setAddAttachment(client.getConnection().getSession().addAttachment);

  const { state } = await client.getRemote().Trame.getState();
  await handlePageUpdate(Object.keys(state), state);

  new Vue({
    ...GLOBAL_VUE_OPTIONS,
    render: (h) => h(App),
  }).$mount('#app');
}

// Initialize service worker to override headers for SharedArrayBuffer
// > Cross-Origin-Opener-Policy: same-origin
// > Cross-Origin-Embedder-Policy: require-corp
if (vtkURLExtract.extractURLParameters().enableSharedArrayBufferServiceWorker) {
  loadScript('coi-serviceworker.min.js');
}

initializeApplication(Vue);
