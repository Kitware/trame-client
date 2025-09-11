const { onMounted, onBeforeUnmount } = window.Vue;

export default {
  emits: ['mounted', 'created', 'beforeDestroy', 'beforeUnmount', 'exit'],
  setup(props, { emit, expose }) {
    function emitTopic(topic, event) {
      emit(topic, event);
    }

    onMounted(() => emit('mounted'));
    onBeforeUnmount(() => {
      emit('beforeDestroy');
      emit('beforeUnmount');
    });
    expose({ emit: emitTopic });
    window.addEventListener('beforeunload', () => {
      emit('exit');
    });
    emit('created');
    return { emit: emitTopic };
  },
  template: `<slot />`,
};
