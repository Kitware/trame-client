import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";
import utils from "../utils";

function toRef(trame, name, triggers) {
  return window.Vue.customRef((track, trigger) => {
    triggers[name] = trigger;
    return {
      get() {
        track();
        return trame.state.get(name);
      },
      set(value) {
        trame.state.set(name, value);
        trigger();
      },
    };
  });
}

export default {
  props: {
    templateName: {
      type: String,
      default: "main",
    },
    urlKey: {
      type: String,
      default: "ui",
    },
    useUrl: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const trame = window.Vue.inject("trame");
    const state = window.Vue.reactive({});
    const modifiedState = {};
    const publicAPI = { trame, utils, state };

    // Dynamic state reactivity
    trame.state.getAllKeys().forEach((name) => {
      publicAPI[name] = toRef(trame, name, modifiedState);
    });
    trame.state.getMutableStateKeys().forEach((name) => {
      state[name] = publicAPI[name];
    });

    // template content
    publicAPI.__template = window.Vue.computed(() => {
      let templateName = props.templateName;
      if (props.useUrl && vtkURLExtract.extractURLParameters()[props.urlKey]) {
        templateName = vtkURLExtract.extractURLParameters()[props.urlKey];
      }
      return window.Vue.unref(publicAPI[`trame__template_${templateName}`]);
    });

    // Server update reactivity
    const onDirty = ({ type, keys }) => {
      if (type === "dirty-state") {
        for (let i = 0; i < keys.length; i++) {
          modifiedState[keys[i]]();
        }

        if (
          keys.includes("trame__favicon") &&
          trame.state.get("trame__favicon")
        ) {
          document.querySelector("link[rel=icon]").href =
            trame.state.get("trame__favicon");
        }
        if (keys.includes("trame__title") && trame.state.get("trame__title")) {
          document.title = trame.state.get("trame__title");
        }
      }
    };

    window.Vue.onMounted(() => {
      trame.state.addListener(onDirty);
    });

    window.Vue.onBeforeUnmount(() => {
      trame.state.removeListener(onDirty);
    });

    // Expose API
    publicAPI.trigger = (...args) => trame.trigger(...args);
    publicAPI.set = (name, value) => trame.state.set(name, value);
    publicAPI.get = (name) => publicAPI[name];
    publicAPI.setAll = (obj) => trame.state.update(obj);
    publicAPI.flushState = (...keys) => trame.state.flush(...keys);
    publicAPI.registerDecorator = (...args) =>
      trame.state.registerDecorator(...args);

    return function render() {
      return window.Vue.h(
        window.Vue.compile(window.Vue.unref(publicAPI.__template)),
        publicAPI
      );
    };
  },
};
