const { inject, reactive, onBeforeMount, onBeforeUnmount, watch } = window.Vue;

export default {
  props: ["name"],
  setup(props) {
    const trame = inject("trame");
    const value = reactive({});
    let trameStr = null;
    let refStr = null;

    function pushChange() {
      refStr = JSON.stringify(value);
      if (refStr !== trameStr) {
        trame.state.set(props.name, JSON.parse(refStr));
      }
    }

    function fetchValue() {
      trameStr = JSON.stringify(trame.state.get(props.name));
      if (trameStr !== refStr) {
        const updatedValue = JSON.parse(trameStr);
        Object.assign(value, updatedValue);
        const keyToDelete = Object.keys(value).filter(
          (name) => !(name in updatedValue)
        );
        for (let i = 0; i < keyToDelete.length; i++) {
          delete value[keyToDelete[i]];
        }
      }
    }

    function updateState({ type, keys }) {
      if (type === "dirty-state" && keys.includes(props.name)) {
        fetchValue();
      }
    }

    onBeforeMount(() => {
      trame.state.addListener(updateState);
      fetchValue();
    });

    onBeforeUnmount(() => {
      trame.state.removeListener(updateState);
    });

    watch(value, pushChange);

    return { value };
  },
  template: '<slot :value="value"></slot>',
};
