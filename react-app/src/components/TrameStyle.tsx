import { useEffect, useRef } from "react";

let ID = 1;

import type { SlotFn } from "../types";

export default function TrameStyle({
  css = "",
  slot,
}: {
  css?: string;
  slot?: SlotFn;
}) {
  const elemId = useRef<string | null>(null);
  if (elemId.current === null) {
    elemId.current = `trame_style_elem_${ID++}`;
  }

  useEffect(() => {
    let elem = document.querySelector(`#${elemId.current}`) as any;
    if (css) {
      if (!elem) {
        elem = document.createElement("style");
        elem.id = elemId.current as string;
        document.head.appendChild(elem);
      }
      elem.innerHTML = css;
    } else if (elem) {
      elem.parentNode.removeChild(elem);
    }
  }, [css]);

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
