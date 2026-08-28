// Renders one server-defined template (trame__template_<name> state key).
// The payload is the JSON component tree produced by trame_client
// (utils/react.py) when the server runs with client_type="react".

import { useEffect, useMemo } from "react";
import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";
import TrameNode from "../renderer/TrameNode";
import { useTrame, useTrameState } from "../renderer/hooks";
import type { TrameJsonNode, TrameTemplatePayload } from "../types";

function parsePayload(payload: unknown): TrameJsonNode | null {
  if (!payload) return null;
  try {
    const { root } = JSON.parse(payload as string) as TrameTemplatePayload;
    return root;
  } catch (e) {
    console.error("trame: invalid react template payload", e);
    return null;
  }
}

export default function TrameTemplate({
  templateName = "main",
  urlKey = "ui",
  useUrl = false,
  stateKey = null,
}: {
  templateName?: string;
  urlKey?: string;
  useUrl?: boolean;
  stateKey?: string | null;
}) {
  const trame = useTrame();
  useTrameState(); // template-wide re-render on any dirty state

  let name = templateName;
  const urlParams = vtkURLExtract.extractURLParameters() as Record<
    string,
    string
  >;
  if (useUrl && urlParams[urlKey]) {
    name = urlParams[urlKey];
  }
  const key = stateKey || `trame__template_${name}`;
  const payload = trame.state.get(key);
  const root = useMemo(() => parsePayload(payload), [payload]);

  // favicon / title side effects (parity with vue clients)
  const favicon = trame.state.get("trame__favicon");
  const title = trame.state.get("trame__title");
  useEffect(() => {
    if (favicon) {
      (document.querySelector("link[rel=icon]") as HTMLLinkElement).href =
        favicon;
    }
  }, [favicon]);
  useEffect(() => {
    if (title) document.title = title;
  }, [title]);

  if (!root) return null;
  return <TrameNode node={root} trame={trame} />;
}
