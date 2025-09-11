const { onMounted, onBeforeUnmount } = window.Vue;

export default {
  emits: ["mounted", "created", "beforeDestroy", "beforeUnmount", "exit"],
  setup(props, { emit, expose }) {
    function emitTopic(topic, event) {
      emit(topic, event);
    }

    onMounted(() => emit("mounted"));
    onBeforeUnmount(() => {
      emit("beforeDestroy");
      emit("beforeUnmount");
    });
    window.addEventListener("beforeunload", () => {
      emit("exit");
    });
    expose({ emit: emitTopic });

    emit("created");
    return { emit: emitTopic };
  },
  template: `<slot />`,
};
