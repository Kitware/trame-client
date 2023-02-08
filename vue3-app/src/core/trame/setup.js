// ----------------------------------------------------------------------------
// Initialisation helpers
//   1. trame__styles  : list of url to load as css
//   2. trame__scripts : list of url to load as scripts
//   3. trame__use     : list of vue plugins to load
//   4. trame__favicon : favicon
//   5. trame__title   : browser tab title
// ----------------------------------------------------------------------------

var LOADED_URLS = [];

function loadScript(url) {
  return new Promise(function (resolve, reject) {
    if (LOADED_URLS.indexOf(url) === -1) {
      LOADED_URLS.push(url);
      var newScriptTag = document.createElement("script");
      newScriptTag.type = "text/javascript";
      newScriptTag.src = url;
      newScriptTag.onload = resolve;
      newScriptTag.onerror = reject;
      document.body.appendChild(newScriptTag);
    } else {
      resolve(false);
    }
  });
}

function loadScriptAsModule(url) {
  return new Promise(function (resolve, reject) {
    if (LOADED_URLS.indexOf(url) === -1) {
      LOADED_URLS.push(url);
      var newScriptTag = document.createElement("script");
      newScriptTag.type = "module";
      newScriptTag.src = url;
      newScriptTag.onload = resolve;
      newScriptTag.onerror = reject;
      document.body.appendChild(newScriptTag);
    } else {
      resolve(false);
    }
  });
}

function loadCSS(url) {
  return new Promise(function (resolve, reject) {
    if (LOADED_URLS.indexOf(url) === -1) {
      LOADED_URLS.push(url);
      var newScriptTag = document.createElement("link");
      newScriptTag.rel = "stylesheet";
      newScriptTag.href = url;
      newScriptTag.onload = resolve;
      newScriptTag.onerror = reject;
      document.head.appendChild(newScriptTag);
    } else {
      resolve(false);
    }
  });
}

export const GLOBAL_VUE_OPTIONS = {};

async function serialLoad(urls, loadFn) {
  for (let i = 0; i < urls.length; i++) {
    /* eslint-disable no-await-in-loop */
    await loadFn(urls[i]);
  }
}

// ----------------------------------------------------------------------------

function loadURLs(urls, loadFn) {
  const mainGroup = [];
  const serialGroups = {};
  for (let i = 0; i < urls.length; i++) {
    let container = mainGroup;
    let url = urls[i];
    if (Array.isArray(url)) {
      const groupName = url[1].serial;
      if (groupName) {
        if (!serialGroups[groupName]) {
          serialGroups[groupName] = [];
        }
        container = serialGroups[groupName];
      }
      [url] = url;
    }
    container.push(url);
  }

  const waitList = mainGroup.map(loadFn);
  const serialScripts = Object.values(serialGroups);
  for (let i = 0; i < serialScripts.length; i++) {
    waitList.push(serialLoad(serialScripts[i], loadFn));
  }

  return Promise.all(waitList);
}

// ----------------------------------------------------------------------------
// Resource management (script/css/vue_use)
// ----------------------------------------------------------------------------

export async function handlePageResources(state) {
  await loadURLs(state.trame__styles, loadCSS);
  await loadURLs(state.trame__scripts, loadScript);
  await loadURLs(state.trame__module_scripts, loadScriptAsModule);

  if (state.trame__favicon) {
    document.querySelector("link[rel=icon]").href = state.trame__favicon;
  }

  if (state.trame__title) {
    document.title = state.trame__title;
  }

  return state.trame__vue_use.map((libUseEntry) => {
    let libKey = libUseEntry;
    let libOptions = [];
    if (Array.isArray(libUseEntry)) {
      [libKey, ...libOptions] = libUseEntry;
    }
    let lib = window.eval(libKey);
    for (let i = 0; i < libOptions.length; i++) {
      const arg = libOptions[i];
      if (arg.js_eval) {
        libOptions[i] = window.eval(arg.js_eval);
      }
    }

    // Invalid lib name
    if (!lib) {
      console.error(
        `Lookup error: Vue.use(${libKey}, ${JSON.stringify(libOptions)})`
      );
      return;
    }
    return [lib, ...libOptions];
  });
}
