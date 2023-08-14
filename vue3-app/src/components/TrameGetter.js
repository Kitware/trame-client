const { inject, ref, onBeforeMount, onBeforeUnmount, watch } = window.Vue;

export default {
  props: ["name"],
  setup(props) {
    const trame = inject("trame");
    const computedValue = ref(null);
    const computedName = ref(null);

    function updateNested(key, value) {
      const newData = JSON.parse(JSON.stringify(trame.state.get(props.name)));
      let current = newData;
      const steps = String(key).split(".");
      for (let i = 0; i < steps.length - 1; i++) {
        current = current[steps[i]];
      }
      current[steps.at(-1)] = value;
      trame.state.set(props.name, newData);
    }

    function update(value) {
      trame.state.set(props.name, value);
    }

    function updateState() {
      const newValue = trame.state.get(props.name);
      if (computedName.value !== props.name) {
        computedName.value = props.name;
      }
      if (newValue !== computedValue.value) {
        computedValue.value = newValue;
      }
    }

    watch(() => props.name, updateState);

    onBeforeMount(() => {
      trame.state.addListener(updateState);
      updateState();
    });

    onBeforeUnmount(() => {
      trame.state.removeListener(updateState);
    });

    return { computedValue, computedName, updateNested, update };
  },
  template:
    '<slot :keyName="computedName" :update="update" :updateNested="updateNested" :value="computedValue"></slot>',
};
