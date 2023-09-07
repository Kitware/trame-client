import { setup } from "./TrameTemplate";

const { inject, ref, onBeforeMount, onBeforeUnmount } = window.Vue;

export default {
  props: {
    useUrl: {
      type: Boolean,
      default: false,
    },
  },
  setup() {
    const trame = inject("trame");
    const connected = ref(false);
    const ready = ref(false);
    const busy = ref(1);
    const refreshTS = ref(1);
    const subscriptions = [];

    function registerComponent(name) {
      const templateName = `trame-template-${name.toLowerCase().substring(16)}`;
      const template = trame.state.get(name);
      trame.app.component(templateName, {
        props: ["name"],
        setup,
        template,
      });
    }

    const stateListener = ({ type, keys }) => {
      if (type === "dirty-state") {
        for (let i = 0; i < keys.length; i++) {
          const dirtyName = keys[i];
          if (dirtyName.startsWith("trame__template_")) {
            registerComponent(dirtyName);
          }
        }
      } else if (type === "refresh") {
        refreshTS.value++;
      } else if (type === "ready") {
        ready.value = true;
        refreshTS.value++;
      }
    };

    function onBusy(count) {
      busy.value = count;
      if (trame.state) {
        trame.state.set("trame__busy", count);
      }
      if (count === 0) {
        trame.state.flush();
      }
    }

    function onConnect() {
      while (subscriptions.length) {
        subscriptions.pop()();
      }

      // Client handling
      subscriptions.push(trame.client.onBusyChange(onBusy).unsubscribe);
      connected.value = trame.client.isConnected();

      // State handling
      trame.state.addListener(stateListener);
      subscriptions.push(() => trame.state.removeListener(stateListener));
      if (trame.state.ready) {
        // Register components
        const keys = trame.state.getAllKeys();
        for (let i = 0; i < keys.length; i++) {
          const key = keys[i];
          if (key.startsWith("trame__template_")) {
            registerComponent(key);
          }
        }

        // We are ready
        ready.value = true;
        connected.value = true;
      }

      // js_call handling
      function execAction(action) {
        const { ref, type } = action;
        const elem = trame.refs[ref];

        if (elem && type === "method") {
          const { method, args } = action;
          elem[method](...args);
        }
        if (elem && type === "property") {
          const { property, value } = action;
          elem[property] = value;
        }
      }
      const wslinkSub = trame.client
        .getRemote()
        .Trame.subscribeToActions(([actions]) => actions.map(execAction));
      subscriptions.push(() =>
        trame?.client?.getRemote()?.Trame?.unsubscribe(wslinkSub)
      );

      // Attach lifecycles
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_connected");
      window.addEventListener("beforeunload", () =>
        trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited")
      );

      // Handle router if available
      const router = window.trame.utils.router;
      const routes = trame.state.get("trame__routes");
      if (routes?.length && router) {
        routes.forEach((route) => {
          router.addRoute(route);
        });
      }
    }

    onBeforeMount(() => {
      trame.addConnectListener(onConnect);
    });

    // Clean subscription at delete
    onBeforeUnmount(() => {
      trame.removeConnectListener(onConnect);
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_unmounted");
      while (subscriptions.length) {
        subscriptions.pop()();
      }
    });

    return {
      connected,
      ready,
      busy,
      refreshTS,
    };
  },
  template: `<trame-template v-if="ready" :key="refreshTS" :use-url="useUrl" />`,
};
