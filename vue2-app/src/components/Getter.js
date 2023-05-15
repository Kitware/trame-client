const { inject, ref, onBeforeMount, onBeforeUnmount, watch } = window.Vue;

export default {
  props: ['name'],
  setup(props) {
    const trame = inject('trame');
    const computed = ref(null);

    function updateState() {
      const newValue = trame.state.get(props.name);
      if (newValue !== computed.value) {
        computed.value = newValue;
      }
    }

    watch(() => props.name, updateState);

    onBeforeMount(() => {
      trame.$on('stateChange', updateState);
      updateState();
    });

    onBeforeUnmount(() => {
      trame.$off('stateChange', updateState);
    });

    return { computed };
  },
  template: '<slot :value="computed"></slot>',
};
