const { reactive, watch } = window.Vue;

export default {
  emits: ["success", "failure", "error", "completed"],
  props: {
    functionKey: {
      type: String,
    },
    triggerOnChange: {
      type: Boolean,
      default: true,
    },
    inputs: {
      type: Object,
    },
  },
  setup(props, { emit }) {
    // optional use
    const input_data = reactive({ value: null });

    watch(input_data, () => {
      if (props.triggerOnChange) {
        run();
      }
    });

    const run = async function run(input_override, inputs) {
      let input = input_data.value;
      let additional_inputs = props.inputs;

      if (input_override) {
        input = input_override;
      }

      if (inputs) {
        additional_inputs = inputs;
      }

      const user_logic_handle = window.TRAME_EXTERNAL_SCRIPTS[props.functionKey];

      if (!user_logic_handle) {
        const message = `Could not find user script function ${props.functionKey}`;
        console.error(message);
        emit("error", message);
        return;
      }

      const function_handle = user_logic_handle.func;

      try {
        const result = await function_handle(input, additional_inputs);

        const event_type = (result.status ?? true) ? "success" : "failure";

        emit("completed", {
          type: event_type,
          outputs: result.outputs ?? result,
        });

        emit(event_type, result.outputs);
      } catch (error) {
        console.error(error);
        emit("error", error);
      }
    };

    return {
      run,
      input_data,
    };
  },
  template: `<slot :run="run" :input_data="input_data" />`,
};
