const { inject, ref, onMounted, onBeforeUnmount } = window.Vue;

export default {
  props: {
    name: {
      type: String,
    },
  },
  emits: ["change"],
  setup(props, { emit }) {
    const trame = inject("trame");
    const elem = ref(null);

    function resize() {
      const { x, y, width, height } = elem.value.getBoundingClientRect();
      const size = { x, y, width, height };
      const pixelRatio = window.devicePixelRatio;
      const dpi = 96 * pixelRatio;
      const event = { size, pixelRatio, dpi };
      if (props.name) {
        event.name = props.name;
      }

      if (trame) {
        trame.state.set(props.name, event);
      }

      emit("change", event);
    }

    const sizeObserver = new ResizeObserver(resize);

    onMounted(() => {
      sizeObserver.observe(elem.value);
    });

    onBeforeUnmount(() => {
      sizeObserver.unobserve(elem.value);
    });

    return { elem, resize };
  },
  template:
    '<div ref="elem" style="overflow: hidden; position: relative; width: 100%; height: 100%; margin: 0; padding: 0;"><slot></slot></div>',
};
