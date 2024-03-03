import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";
import utils from "../utils";

const {
  inject,
  ref,
  computed,
  onMounted,
  onBeforeUnmount,
  nextTick,
  customRef,
} = window.Vue;

function toRef(trame, name, triggers) {
  return customRef((track, trigger) => {
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

export function setup() {
  const trame = inject("trame");
  const tts = ref(0);
  const modifiedState = {};
  const publicAPI = { trame, window, utils, tts };

  // Dynamic state reactivity
  trame.state.getAllKeys().forEach((name) => {
    publicAPI[name] = toRef(trame, name, modifiedState);
  });

  // Server update reactivity
  const onDirty = ({ type, keys }) => {
    if (type === "new-keys") {
      for (let i = 0; i < keys.length; i++) {
        const name = keys[i];
        if (publicAPI[name] === undefined) {
          publicAPI[name] = toRef(trame, name, modifiedState);
        }
      }
    }

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

  onMounted(() => {
    trame.state.addListener(onDirty);
  });

  onBeforeUnmount(() => {
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

  return publicAPI;
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
    const trame = inject("trame");
    const tts = ref(0);
    const componentName = computed(() => {
      let templateName = props.templateName;
      if (props.useUrl && vtkURLExtract.extractURLParameters()[props.urlKey]) {
        templateName = vtkURLExtract.extractURLParameters()[props.urlKey];
      }
      return `trame-template-${templateName.toLowerCase()}`
        .replaceAll("_", "-")
        .replaceAll("--", "-");
    });

    async function updateTemplate() {
      await nextTick();
      tts.value++;
    }

    const onDirty = ({ type, keys }) => {
      if (type === "dirty-state") {
        for (let i = 0; i < keys.length; i++) {
          const tName = keys[i]
            .toLowerCase()
            .replaceAll("_", "-")
            .replaceAll("--", "-");
          if (tName === componentName.value) {
            updateTemplate();
          }
        }
      }
    };
    onMounted(() => {
      trame.state.addListener(onDirty);
    });
    onBeforeUnmount(() => {
      trame.state.removeListener(onDirty);
    });

    return { tts, componentName };
  },
  template:
    '<component :key="tts" :is="componentName" :name="componentName" />',
};
