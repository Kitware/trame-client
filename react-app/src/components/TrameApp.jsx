import { useEffect, useMemo, useState } from "react";
import { TrameContext } from "../runtime/trameContext";
import { createRefRegistry } from "../runtime/refs";
import { registerTag } from "../runtime/tags";
import ReactIf from "./ReactIf.jsx";
import ReactFor from "./ReactFor.jsx";
import TrameLoading from "./TrameLoading.jsx";
import TrameTemplate from "./TrameTemplate.jsx";
import TrameReconnect from "./TrameReconnect.jsx";
import TrameJSEval from "./TrameJSEval.jsx";
import TrameStyle from "./TrameStyle.jsx";
import TrameScript from "./TrameScript.jsx";
import TrameClientStateChange from "./TrameClientStateChange.jsx";
import TrameClientTriggers from "./TrameClientTriggers.jsx";
import TrameLifeCycleMonitor from "./TrameLifeCycleMonitor.jsx";
import TrameSizeObserver from "./TrameSizeObserver.jsx";

// Registered once at module load, before first render (§6 of the plan).
registerTag("ReactIf", ReactIf);
registerTag("ReactFor", ReactFor);
registerTag("trame-loading", TrameLoading);
registerTag("trame-template", TrameTemplate);
registerTag("trame-exec", TrameJSEval);
registerTag("trame-style", TrameStyle);
registerTag("trame-script", TrameScript);
registerTag("trame-client-state-change", TrameClientStateChange);
registerTag("trame-client-triggers", TrameClientTriggers);
registerTag("trame-life-cycle-monitor", TrameLifeCycleMonitor);
registerTag("trame-size-observer", TrameSizeObserver);

// Responsibilities ported from vue3-app/src/components/TrameApp.js, minus
// per-`trame__template_*`-name dynamic-component registration (no Vue-style
// "register a component by string name" system to feed - TrameTemplate just
// reads its state key directly and hands the dict to TrameNode).
export default function TrameApp({ trame, useUrl = false }) {
  const [connected, setConnected] = useState(() => trame.isConnected());
  const [refreshTS, setRefreshTS] = useState(0);

  useEffect(() => {
    const unsubscribe = trame.onClose(() => setConnected(false));

    function onBeforeUnload() {
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_exited");
    }
    window.addEventListener("beforeunload", onBeforeUnload);

    return () => {
      unsubscribe();
      window.removeEventListener("beforeunload", onBeforeUnload);
      trame.client?.getRemote()?.Trame?.lifeCycleUpdate("client_unmounted");
    };
  }, [trame]);

  const ctx = useMemo(
    () => ({ trame, getRefCallback: createRefRegistry(trame) }),
    [trame, refreshTS],
  );

  if (!connected) {
    return (
      <TrameReconnect
        trame={trame}
        onReconnected={() => {
          setRefreshTS((v) => v + 1);
          setConnected(true);
        }}
      />
    );
  }

  return (
    <TrameContext.Provider key={refreshTS} value={ctx}>
      <TrameTemplate useUrl={useUrl} />
    </TrameContext.Provider>
  );
}
