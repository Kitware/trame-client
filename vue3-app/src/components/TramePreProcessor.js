const { reactive, watch } = window.Vue;

export default {
  emits: ["success", "failure", "error", "completed"],
  props: {
    preprocessingFunctionKey: {
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
        triggerPreprocessing();
      }
    });

    const triggerPreprocessing = async function triggerPreprocessing(data_to_preprocess, inputs) {
      let input = input_data.value;
      let additional_inputs = props.inputs;

      if (data_to_preprocess) {
        input = data_to_preprocess;
      }

      if (inputs) {
        additional_inputs = inputs;
      }

      const preprocessing_obj = window.TRAME_CLIENT_PREPROCESSING[props.preprocessingFunctionKey];

      if (!preprocessing_obj) {
        const message = `Could not find preprocessing function ${props.preprocessingFunctionKey}`;
        console.error(message);
        emit("error", message);
        return;
      }

      const preprocess_function = preprocessing_obj.preprocess;

      try {
        const result = await preprocess_function(input, additional_inputs);
        console.log({ result });

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
      triggerPreprocessing,
      input_data,
    };
  },
  template: `<slot :trigger_preprocessing="triggerPreprocessing" :input_data="input_data" />`,
};
