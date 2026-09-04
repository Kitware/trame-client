import { useEffect, useRef } from "react";

// Port of vue3-app/src/components/TrameScript.js: injects/updates a global
// `<script>` tag from a bound state string, removing it when the content
// becomes falsy and always on unmount. `type` is only set at creation time,
// matching the vue original.
export default function TrameScript({ script, module, children }) {
  const elRef = useRef(null);

  useEffect(
    () => () => {
      elRef.current?.remove();
      elRef.current = null;
    },
    [],
  );

  useEffect(() => {
    if (!script) {
      elRef.current?.remove();
      elRef.current = null;
      return;
    }
    if (!elRef.current) {
      elRef.current = document.createElement("script");
      elRef.current.type = module ? "module" : "text/javascript";
      document.head.appendChild(elRef.current);
    }
    elRef.current.textContent = script;
  }, [script, module]);

  return children ?? null;
}
