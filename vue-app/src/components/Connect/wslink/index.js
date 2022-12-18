import vtkURLExtract from '@kitware/vtk.js/Common/Core/URLExtract';
import SmartConnect from 'wslink/src/SmartConnect';
import vtkWSLinkClient from '@kitware/vtk.js/IO/Core/WSLinkClient';

import protocols from './protocols';

vtkWSLinkClient.setSmartConnectClass(SmartConnect);

const WS_CLIENTS = {};

const WS_PROTOCOL = {
  'http:': 'ws:',
  'https:': 'wss:',
  'ws:': 'ws:',
  'wss:': 'wss:',
};

const NOT_BUSY_LIST = [
  // *
  'unsubscribe',
  // SyncView
  'subscribeToViewChange',
  // Trame
  'subscribeToStateUpdate',
  'subscribeToActions',
  'subscribeToViewChange',
];

function configDecorator(config) {
  const outputConfig = { ...config };

  // Process sessionURL
  if (outputConfig.sessionURL) {
    let sessionURL = outputConfig.sessionURL.toLowerCase();
    const httpURL = window.location;

    // handle protocol mapping http(s) => ws(s)
    if (sessionURL.includes('use_')) {
      const wsURL = new URL(sessionURL);
      wsURL.protocol = WS_PROTOCOL[httpURL.protocol];
      sessionURL = wsURL.toString();
    }

    // handle variable replacement
    const use_mapping = {
      use_hostname: httpURL.hostname,
      use_host: httpURL.host,
    };
    for (const [key, value] of Object.entries(use_mapping)) {
      sessionURL = sessionURL.replaceAll(key, value);
    }

    // update config
    outputConfig.sessionURL = sessionURL;
  }

  // Extract app-name from html
  outputConfig.application =
    document.querySelector('html').dataset.appName || outputConfig.application;

  const sessionManagerURL =
    document.querySelector('html').dataset.sessionManagerUrl || outputConfig.sessionManagerURL;
  if (sessionManagerURL) {
    outputConfig.sessionManagerURL = sessionManagerURL;
  }

  // Process arguments from URL
  if (outputConfig.useUrl) {
    return {
      ...outputConfig,
      ...vtkURLExtract.extractURLParameters(),
    };
  }
  return outputConfig;
}

function createClient() {
  return vtkWSLinkClient.newInstance({
    protocols,
    configDecorator,
    notBusyList: NOT_BUSY_LIST,
  });
}

function getClient(name) {
  let client = WS_CLIENTS[name]?.client;

  if (!client) {
    client = createClient();
    const subscriptions = [];
    const status = { type: 'created', message: 'Client connected...' };
    WS_CLIENTS[name] = {
      client,
      status,
      subscriptions,
    };

    /* eslint-disable no-inner-declarations */
    function updateStatus(status) {
      WS_CLIENTS[name].status = status;
    }

    subscriptions.push(
      client.onConnectionError((httpReq) => {
        updateStatus({
          type: 'Connection error',
          message: httpReq?.response?.error,
        });
      })
    );

    subscriptions.push(
      client.onConnectionClose((httpReq) => {
        updateStatus({
          type: 'Connection close',
          message: httpReq?.response?.error,
        });
      })
    );
  }

  return client;
}

function resetClient(name) {
  WS_CLIENTS[name] = null;
}

function getStatus(name) {
  return WS_CLIENTS[name].status;
}

export default {
  getClient,
  resetClient,
  getStatus,
  configDecorator,
};
