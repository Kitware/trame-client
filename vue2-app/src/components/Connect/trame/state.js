import Vue from 'vue';
import { loadScript, loadCSS } from '@kitware/vtk.js/IO/Core/ResourceLoader';
import VRuntimeTemplate from 'v-runtime-template';
import { decorate, registerDecorator } from './decorators';
import utils from '../../../utils';

// ----------------------------------------------------------------------------
// Make utils global
// ----------------------------------------------------------------------------

if (!window.trame) {
  window.trame = {};
}
if (!window.trame.utils) {
  window.trame.utils = utils;
}

// ----------------------------------------------------------------------------
// Helper functions for state reactivity handling
// ----------------------------------------------------------------------------

function createStateTS(keys) {
  const dataForStateTS = { tts: 0 };

  keys.forEach((name) => {
    dataForStateTS[name] = 0;
  });

  return new Vue({ data: dataForStateTS });
}

// ----------------------------------------------------------------------------

function monitorChanges(trame, stateTS) {
  function onChange(names) {
    for (let i = 0; i < names.length; i++) {
      stateTS[names[i]]++;
    }
  }

  trame.$on('stateChange', onChange);

  return () => {
    trame.$off('stateChange', onChange);
  };
}

// ----------------------------------------------------------------------------

function createComputed(trame, keys, stateTS) {
  const computed = {};
  keys.forEach((name) => {
    computed[name] = {
      get() {
        stateTS[name];
        return trame.state.get(name);
      },
      set(v) {
        trame.state.set(name, v);
      },
    };
  });
  return computed;
}

// ----------------------------------------------------------------------------
// Initialisation helpers
//   1. trame__styles  : list of url to load as css
//   2. trame__scripts : list of url to load as scripts
//   3. trame__use     : list of vue plugins to load
//   4. trame__favicon : favicon
//   5. trame__title   : browser tab title
// ----------------------------------------------------------------------------

export const GLOBAL_VUE_OPTIONS = {};
const VUE_USE_LOADED = {};

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

export async function handlePageUpdate(modifiedKeys, state, exclude = []) {
  const filterFn = (v) => !exclude.includes(v);
  if (modifiedKeys.includes('trame__styles')) {
    await loadURLs(state.trame__styles.filter(filterFn), loadCSS);
  }

  if (modifiedKeys.includes('trame__scripts')) {
    await loadURLs(state.trame__scripts.filter(filterFn), loadScript);
  }

  if (modifiedKeys.includes('trame__vue_use')) {
    // utils.get(path, obj)
    state.trame__vue_use.forEach((libUseEntry) => {
      let libKey = libUseEntry;
      let libOptions = {};
      if (Array.isArray(libUseEntry)) {
        [libKey, libOptions] = libUseEntry;
      }
      let lib = utils.get(libKey);

      // Invalid lib name
      if (!lib) {
        console.error(`Lookup error: Vue.use(${libKey}, ${JSON.stringify(libOptions)})`);
        return;
      }

      if (VUE_USE_LOADED[libKey] || exclude.includes(libKey)) {
        return;
      }
      VUE_USE_LOADED[libKey] = true;

      // Resolve "default" namespace if any
      if (lib.default) {
        lib = lib.default;
      }

      // Resolve "lib.install" requirement
      console.info(
        `Vue.use(${libKey}, ${JSON.stringify(libOptions)}) - ${!!lib} - install(${!!lib.install})`
      );
      if (lib.install) {
        Vue.use(lib, libOptions);
        if (lib.getOptions) {
          Object.assign(GLOBAL_VUE_OPTIONS, lib.getOptions());
        }
      } else {
        Vue.use({ install: lib }, libOptions);
      }
    });
  }

  if (modifiedKeys.includes('trame__favicon') && state.trame__favicon) {
    document.querySelector('link[rel=icon]').href = state.trame__favicon;
  }

  if (modifiedKeys.includes('trame__title') && state.trame__title) {
    document.title = state.trame__title;
  }
}

// ----------------------------------------------------------------------------
// State helper
// ----------------------------------------------------------------------------

export class TrameState {
  constructor(vueInstance, client = null, exclude = []) {
    this.name = 'Default trame application';
    this.vueInstance = vueInstance;
    this.client = vueInstance?.client || client;
    this.exclude = vueInstance?.exclude || exclude;
    this.subscriptions = [];
    this.state = {};
    this.keyTS = {};
    this.ts = 0;
    this.trameTemplateTS = 0;
    this.trameTemplate = { template: '<div>Too early for trame template</div>' };
    this.dirtyKeys = new Set();

    // bind decorator helper
    this.registerDecorator = registerDecorator;

    const updateFromServer = async (serverState) => {
      const updatedKeys = [];
      const allKeys = Object.keys(serverState);
      for (let i = 0; i < allKeys.length; i++) {
        let modified = true;
        const key = allKeys[i];
        const value = serverState[key];

        // Handle _filter field
        if (value?._filter?.length) {
          modified = false;
          const prevValue = this.state[key];
          const objKeys = Object.keys(value);
          for (let j = 0; !modified && j < objKeys.length; j++) {
            const subKey = objKeys[j];
            if (subKey[0] === '_') {
              continue;
            }
            if (prevValue === undefined || prevValue[subKey] !== value[subKey]) {
              modified = true;
            }
          }
        }

        if (modified) {
          updatedKeys.push(key);
          this.state[key] = value;
        }
      }

      this.ts += 1;
      let newKeyCount = 0;
      for (let i = 0; i < updatedKeys.length; i++) {
        const key = updatedKeys[i];
        if (this.keyTS[key] === undefined) {
          newKeyCount++;
        }
        this.keyTS[key] = this.ts;
      }

      // Handle any page update (resource loading, vue plugins, title, favicon)
      await handlePageUpdate(updatedKeys, this.state, this.exclude);

      if (newKeyCount) {
        this.updateTrameTemplate();
        if (this.vueInstance) {
          this.vueInstance.$emit('trameTemplateChange', this.trameTemplateTS);
        }
      }

      if (this.vueInstance) {
        this.vueInstance.$emit('stateChange', updatedKeys);

        // Setup router if available
        if (this.vueInstance.$router && serverState?.trame__routes?.length) {
          const router = this.vueInstance.$router;
          serverState.trame__routes.forEach((route) => {
            router.addRoute(route);
          });
        }
      }
    };

    this.subscriptions.push(
      this.client
        .getRemote()
        .Trame.subscribeToStateUpdate(([serverState]) => updateFromServer(serverState))
    );

    this.client
      .getRemote()
      .Trame.getState()
      .then(({ state, name }) => {
        this.name = name;
        updateFromServer(state);
        if (vueInstance) {
          vueInstance.ready = true;
        }
      });

    // Keep it so we can call it on disconnect
    this._updateFromServer = updateFromServer;
  }

  updateTrameTemplate() {
    if (!this.vueInstance) {
      return;
    }
    this.trameTemplateTS += 1;
    const availableKeys = Object.keys(this.state);
    const stateTS = createStateTS(availableKeys);
    const unbindState = monitorChanges(this.vueInstance, stateTS);
    const computed = createComputed(this.vueInstance, availableKeys, stateTS);
    let refCount = 0;

    this.trameTemplate = {
      name: 'TrameTemplate',
      inject: ['trame'],
      props: {
        templateName: {
          type: String,
          default: 'main',
        },
      },
      components: {
        VRuntimeTemplate,
      },
      computed: {
        ...computed,
        contentTemplate() {
          const templateKey = `trame__template_${this.templateName}`;
          return (
            this[templateKey] ||
            `<div>No state variable for ${templateKey} with the following state.<br><pre>${JSON.stringify(
              this.trame.state.get(),
              null,
              2
            )}</pre></div>`
          );
        },
        tts() {
          return stateTS.tts;
        },
        utils() {
          return utils;
        },
      },
      watch: {
        contentTemplate() {
          setTimeout(() => (stateTS.tts += 1), 10);
        },
      },
      methods: {
        set(key, value) {
          return this.trame.state.set(key, value);
        },
        get(key = null) {
          return this.trame.state.get(key);
        },
        setAll(obj) {
          return this.trame.state.update(obj);
        },
        flushState(...keys) {
          return this.trame.state.flush(...keys);
        },
        registerDecorator(...args) {
          return this.trame.state.registerDecorator(...args);
        },
        async trigger(name, args = [], kwargs = {}) {
          let decoratedArgs = [];
          const decoratedKwargs = {};

          if (args) {
            const decorateArgs = args.map((arg) => decorate(arg));
            decoratedArgs = await Promise.all(decorateArgs);
          }

          if (kwargs) {
            const keys = [];
            const values = [];
            Object.entries(kwargs).forEach((key, value) => {
              keys.push(key);
              values.push(decorate(value));
            });

            const resolvedValues = await Promise.all(values);
            for (let i = 0; i < keys.length; i++) {
              decoratedKwargs[keys[i]] = resolvedValues[i];
            }
          }

          return await this.trame.client
            .getRemote()
            .Trame.trigger(name, decoratedArgs, decoratedKwargs);
        },
        getRef(ref) {
          const { trameTemplateRootRef } = this.$refs;
          if (trameTemplateRootRef.$refs && trameTemplateRootRef.$refs[ref]) {
            return trameTemplateRootRef.$refs[ref];
          }
          return trameTemplateRootRef.$children[0].$refs[ref];
        },
        execAction(action) {
          const { ref, type } = action;
          const elem = this.getRef(ref);
          if (elem && type === 'method') {
            const { method, args } = action;
            elem[method](...args);
          }
          if (elem && type === 'property') {
            const { property, value } = action;
            elem[property] = value;
          }
        },
      },
      created() {
        refCount++;
        this.onActions = ([actions]) => {
          for (let i = 0; i < actions.length; i++) {
            this.execAction(actions[i]);
          }
        };
        this.clientSub = this.trame.client.getRemote().Trame.subscribeToActions(this.onActions);
      },
      beforeDestroy() {
        refCount--;
        if (refCount === 0) {
          unbindState();
        }
        this.trame.client.getRemote().Trame.unsubscribe(this.clientSub);
      },
      template: '<v-runtime-template ref="trameTemplateRootRef" :template="contentTemplate" />',
    };
  }

  delete() {
    while (this.subscriptions.length) {
      this.client.getRemote().Trame.unsubscribe(this.subscriptions.pop());
    }
  }

  get(key) {
    if (key === undefined) {
      return this.state;
    }
    return this.state[key];
  }

  getTimeStamp(key) {
    return this.keyTS[key] || 0;
  }

  async set(key, value) {
    // Prevent triggering change when same value is set
    if (this.state[key] === value) {
      return;
    }

    this.ts += 1;
    this.state[key] = value;
    this.keyTS[key] = this.ts;
    this.dirty(key);
    await this.flush();
  }

  async update(obj) {
    this.ts += 1;
    for (const [key, value] of Object.entries(obj)) {
      if (this.state[key] !== value) {
        this.state[key] = value;
        this.keyTS[key] = this.ts;
        this.dirty(key);
      }
    }
    await this.flush();
  }

  canDirty(name) {
    return !this.state.trame__client_only.includes(name);
  }

  dirty(...keys) {
    keys.forEach((key) => {
      if (this.canDirty(key)) {
        this.dirtyKeys.add(key);
      }

      // Make sure client side is aware of that change...
      if (this.vueInstance) {
        this.vueInstance.$emit('stateChange', [key]);
      }
    });
  }

  async flush(...keys) {
    if (keys.length) {
      keys.forEach((key) => {
        if (Array.isArray(key)) {
          this.dirty(...key);
        } else {
          this.dirty(key);
        }
      });
    }

    if (this.dirtyKeys.size && !this.client.isBusy()) {
      const waitOn = [];
      const keys = [];
      this.dirtyKeys.forEach((key) => {
        waitOn.push(decorate(this.state[key]));
        keys.push(key);
      });
      this.dirtyKeys.clear();
      const values = await Promise.all(waitOn);
      const deltaState = keys.map((key, i) => ({ key, value: values[i] }));
      await this.client.getRemote().Trame.updateState(deltaState);

      // Make sure we don't leave any pending update...
      if (this.dirtyKeys.size) {
        this.flush();
      }
    }

    // when connection died, the client is busy...
    if (this.vueInstance && !this.vueInstance.connected) {
      // Handle dynamic update once disconnected
      this._updateFromServer(this.state);
    }
  }
}
