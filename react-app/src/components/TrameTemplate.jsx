import { useSyncExternalStore } from "react";
import { extractURLParameters } from "@kitware/trame";
import { useTrame } from "../runtime/trameContext";
import TrameNode from "./TrameNode.jsx";

// Direct analog of vue3-app/src/components/TrameTemplate.js's default export
// (not its separate setup() helper, which exists only to build a
// Vue-instance-reactive API object for Vue's template compiler - no
// equivalent need here, since TrameNode reads trame.state/scope directly).
// Simpler than the Vue original precisely because there's no
// dynamic-component-by-name indirection to replicate: AbstractLayout's
// flush_content() already puts the JSON tree dict directly into this state key.
export default function TrameTemplate({ templateName = "main", urlKey = "ui", useUrl = false }) {
  const { trame } = useTrame();
  const params = useUrl ? extractURLParameters() : {};
  const stateKey = `trame__template_${params[urlKey] ?? templateName}`;
  const tree = useSyncExternalStore(
    (cb) => trame.state.watch([stateKey], cb),
    () => trame.state.get(stateKey),
  );
  return <TrameNode nodes={tree} scope={undefined} />;
}
