const { watch, nextTick } = window.Vue;

export default {
  props: {
    value: {
      type: String,
    },
    immediate: {
      type: Boolean,
      default: false,
    },
    triggerChangeOnCreate: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["change"],
  setup(props, { emit }) {
    watch(
      () => props.value,
      (v) => {
        if (props.immediate) {
          emit("change", v);
        } else {
          nextTick(() => {
            emit("change", v);
          });
        }
      }
    );
    if (props.triggerChangeOnCreate) {
      emit("change", props.value);
    }
  },
};
