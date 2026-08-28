// Built-in component registration (react port of vue3-app use.js + registry)

import TrameClientStateChange from "./TrameClientStateChange";
import TrameClientTriggers from "./TrameClientTriggers";
import TrameDeepReactive from "./TrameDeepReactive";
import TrameExec from "./TrameExec";
import TrameGetter from "./TrameGetter";
import TrameHandler from "./TrameHandler";
import TrameLifeCycleMonitor from "./TrameLifeCycleMonitor";
import TrameLoading from "./TrameLoading";
import TrameReconnect from "./TrameReconnect";
import TrameScript from "./TrameScript";
import TrameSizeObserver from "./TrameSizeObserver";
import TrameStyle from "./TrameStyle";
import TrameTemplate from "./TrameTemplate";

const COMPONENTS = {
  "trame-client-state-change": TrameClientStateChange,
  "trame-client-triggers": TrameClientTriggers,
  "trame-deep-reactive": TrameDeepReactive,
  "trame-exec": TrameExec,
  "trame-getter": TrameGetter,
  "trame-handler": TrameHandler,
  "trame-life-cycle-monitor": TrameLifeCycleMonitor,
  "trame-loading": TrameLoading,
  "trame-reconnect": TrameReconnect,
  "trame-script": TrameScript,
  "trame-size-observer": TrameSizeObserver,
  "trame-style": TrameStyle,
  "trame-template": TrameTemplate,
};

import type { Registry } from "../types";

export default function registerComponents(registry: Registry) {
  Object.entries(COMPONENTS).forEach(([tag, component]) => {
    registry.register(tag, component);
  });
}
