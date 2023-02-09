export default {
  props: {
    useUrl: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    const trame = window.Vue.inject("trame");
    const connected = window.Vue.ref(false);
    const ready = window.Vue.ref(false);
    const busy = window.Vue.ref(1);
    const refreshTS = window.Vue.ref(1);
    const subscriptions = [];

    function onRefresh({ type }) {
      if (type === "refresh") {
        refreshTS.value++;
      }
    }

    function onReady({ type }) {
      if (type === "ready") {
        ready.value = true;
        refreshTS.value++;
      }
    }

    function onBusy(count) {
      const emitBusyChange = !count !== !window.Vue.unref(busy);
      busy.value = count;
      if (emitBusyChange && trame.state) {
        trame.state.set("trame__busy", count);
      }
      if (count === 0) {
        trame.state.flush();
      }
      if (emitBusyChange) {
        emit("busyChange", count);
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
      trame.state.addListener(onRefresh);
      subscriptions.push(() => trame.state.removeListener(onRefresh));
      trame.state.addListener(onReady);
      subscriptions.push(() => trame.state.removeListener(onReady));
      if (trame.state.ready) {
        ready.value = true;
        connected.value = true;
      }

      // Attach lifecycles
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_connected");
      window.addEventListener("beforeunload", () =>
        trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited")
      );
    }

    window.Vue.onBeforeMount(() => {
      trame.addConnectListener(onConnect);
    });

    // Clean subscription at delete
    window.Vue.onBeforeUnmount(() => {
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
