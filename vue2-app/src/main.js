import Vue from 'vue';
import App from './components/App';
import Trame from './use';

import { setAddAttachment } from './components/Connect/trame/decorators';
import { handlePageUpdate, GLOBAL_VUE_OPTIONS } from './components/Connect/trame/state';
import wslink from './components/Connect/wslink';

const DEFAULT_CONNECTION_NAME = 'TrameConnect';

function reportWsError() {
  const status = wslink.getStatus(DEFAULT_CONNECTION_NAME);
  const elem = document.querySelector('.trame__message');
  if (elem) {
    elem.innerHTML = status.message || status.type;
  }
}

async function initializeApplication(Vue) {
  // Add default trame components
  Vue.use(Trame);

  // Connect to server
  const client = wslink.getClient(DEFAULT_CONNECTION_NAME);
  try {
    await client.connect(
      wslink.configDecorator({
        application: 'trame',
        useUrl: true,
      })
    );
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

initializeApplication(Vue);
