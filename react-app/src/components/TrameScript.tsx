import { useEffect, useRef } from "react";

let ID = 1;

import type { SlotFn } from "../types";

export default function TrameScript({
  script = "",
  module = false,
  slot,
}: {
  script?: string;
  module?: boolean;
  slot?: SlotFn;
}) {
  const elemId = useRef<string | null>(null);
  if (elemId.current === null) {
    elemId.current = `trame_script_elem_${ID++}`;
  }

  useEffect(() => {
    let elem = document.querySelector(`#${elemId.current}`) as any;
    if (script) {
      if (!elem) {
        elem = document.createElement("script");
        elem.id = elemId.current as string;
        elem.type = module ? "module" : "text/javascript";
        document.head.appendChild(elem);
      }
      elem.innerHTML = script;
    } else if (elem) {
      elem.parentNode.removeChild(elem);
    }
  }, [script, module]);

  useEffect(
    () => () => {
      const elem = document.querySelector(`#${elemId.current}`) as any;
      if (elem) {
        elem.parentNode.removeChild(elem);
      }
    },
    [],
  );

  return slot ? slot() : null;
}
