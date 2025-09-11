const { unref } = window.Vue;

export default {
  props: ["event"],
  emits: ["exec"],
  setup(props, { emit }) {
    function exec(arg) {
      if (arg === undefined) {
        emit("exec", unref(props.event));
      } else {
        emit("exec", arg);
      }
    }
    return { exec };
  },
  template: `<slot />`,
};
