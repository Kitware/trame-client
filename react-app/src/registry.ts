// Component registry: maps tags used in the server-sent JSON tree to React
// components. Widget libraries (e.g. trame-mui) register their
// components through the plugin interface:
//
//   export default {
//     install(registry) {
//       registry.register("my-widget", MyWidget);
//     },
//   };

import type { ComponentType } from "react";

import type { Registry, RegistryPlugin } from "./types";

const COMPONENTS = new Map<string, ComponentType<any>>();

export const registry: Registry = {
  register(tag: string, component: ComponentType<any>) {
    if (COMPONENTS.has(tag)) {
      console.warn(`registry: tag "${tag}" is being overridden`);
    }
    COMPONENTS.set(tag, component);
  },
  unregister(tag: string) {
    COMPONENTS.delete(tag);
  },
  resolve(tag: string) {
    return COMPONENTS.get(tag);
  },
  has(tag: string) {
    return COMPONENTS.has(tag);
  },
  use(plugin: RegistryPlugin, ...options: unknown[]) {
    if (typeof plugin === "object" && plugin?.install) {
      plugin.install(registry, ...options);
    } else if (typeof plugin === "function") {
      plugin(registry, ...options);
    } else {
      console.error("registry.use: plugin has no install()", plugin);
    }
  },
};

export default registry;
