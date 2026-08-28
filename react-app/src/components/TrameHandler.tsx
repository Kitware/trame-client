import { useImperativeHandle, useRef, forwardRef } from "react";

// Runs a user-provided external script function (registered through
// user_script_handler) with optional inputs; reports through events.
import type { SlotFn } from "../types";

type Props = {
  functionKey?: string;
  triggerOnChange?: boolean;
  inputs?: unknown;
  onSuccess?: (outputs: unknown) => void;
  onFailure?: (outputs: unknown) => void;
  onError?: (error: unknown) => void;
  onCompleted?: (result: unknown) => void;
  slot?: SlotFn;
};

const TrameHandler = forwardRef<any, Props>(function TrameHandler(
  {
    functionKey,
    triggerOnChange = true,
    inputs,
    onSuccess,
    onFailure,
    onError,
    onCompleted,
    slot,
  },
  ref,
) {
  const inputData = useRef<{ value: unknown }>({ value: null });

  const run = async (inputOverride?: unknown, inputsOverride?: unknown) => {
    let input = inputData.current.value;
    let additionalInputs = inputs;

    if (inputOverride) {
      input = inputOverride;
    }
    if (inputsOverride) {
      additionalInputs = inputsOverride;
    }

    const userLogicHandle = (window as any).TRAME_EXTERNAL_SCRIPTS?.[
      functionKey as string
    ];
    if (!userLogicHandle) {
      const message = `Could not find user script function ${functionKey}`;
      console.error(message);
      onError?.(message);
      return;
    }

    try {
      const result = await userLogicHandle.func(input, additionalInputs);
      const success = result.status ?? true;
      const outputs = result.outputs ?? result;
      onCompleted?.({ type: success ? "success" : "failure", outputs });
      (success ? onSuccess : onFailure)?.(outputs);
    } catch (error) {
      console.error(error);
      onError?.(error);
    }
  };

  const setInput = (value: unknown) => {
    inputData.current.value = value;
    if (triggerOnChange) {
      run();
    }
  };

  useImperativeHandle(ref, () => ({ run, setInput }));

  return slot ? slot({ run, input_data: inputData.current, setInput }) : null;
});

export default TrameHandler;
