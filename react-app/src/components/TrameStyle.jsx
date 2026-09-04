import { useEffect, useRef } from "react";

// Port of vue3-app/src/components/TrameStyle.js: injects/updates a global
// `<style>` tag from a bound state string, removing it when the content
// becomes falsy (mirrors the vue original's create-on-demand/remove-when-
// empty behavior) and always on unmount.
export default function TrameStyle({ css, children }) {
  const elRef = useRef(null);

  useEffect(
    () => () => {
      elRef.current?.remove();
      elRef.current = null;
    },
    [],
  );

  useEffect(() => {
    if (!css) {
      elRef.current?.remove();
      elRef.current = null;
      return;
    }
    if (!elRef.current) {
      elRef.current = document.createElement("style");
      document.head.appendChild(elRef.current);
    }
    elRef.current.textContent = css;
  }, [css]);

  return children ?? null;
}
