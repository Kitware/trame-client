// Public contract between the trame react client, the renderer and widget
// libraries (trame-mui, trame-vtk react-components, application components).

import type { ComponentType, ReactNode } from "react";

// ----------------------------------------------------------------------------
// trame instance (created by core/trame, framework-agnostic JS)
// ----------------------------------------------------------------------------

export interface TrameState {
  state: Record<string, any>;
  ready: boolean;
  ts: number;
  get(key?: string): any;
  set(key: string, value: unknown): Promise<void>;
  update(obj: Record<string, unknown>): Promise<void>;
  flush(...keys: unknown[]): Promise<void> | void;
  getAllKeys(): string[];
  addListener(listener: TrameStateListener): void;
  removeListener(listener: TrameStateListener): void;
  registerDecorator(...args: unknown[]): void;
  delete(): void;
}

export type TrameStateEvent = {
  type: "dirty-state" | "new-keys" | "ready" | "refresh";
  keys?: string[];
};
export type TrameStateListener = (event: TrameStateEvent) => void;

export interface TrameInstance {
  app: Registry;
  client: any; // vtkWSLinkClient
  state: TrameState;
  config: Record<string, unknown> | null;
  utils: Record<string, any>;
  refs: Record<string, any>;
  connect(config?: Record<string, unknown>): Promise<Record<string, unknown>>;
  trigger(
    name: string,
    args?: unknown[],
    kwargs?: Record<string, unknown>,
  ): Promise<unknown>;
  addConnectListener(listener: () => void): void;
  removeConnectListener(listener: () => void): void;
}

// ----------------------------------------------------------------------------
// Component registry (widget libraries plug in through `react_use`)
// ----------------------------------------------------------------------------

export interface Registry {
  register(tag: string, component: ComponentType<any>): void;
  unregister(tag: string): void;
  resolve(tag: string): ComponentType<any> | undefined;
  has(tag: string): boolean;
  use(plugin: RegistryPlugin, ...options: unknown[]): void;
}

export type RegistryPlugin =
  | { install(registry: Registry, ...options: unknown[]): void }
  | ((registry: Registry, ...options: unknown[]) => void);

// Registered components receive their children through the scoped-slot
// render prop, and two-way bindings as `value` + `onUpdateValue`.
export type SlotFn = (slotProps?: Record<string, unknown>) => ReactNode;

// ----------------------------------------------------------------------------
// Serialized layout (wire schema produced by trame_client/utils/react.py)
// ----------------------------------------------------------------------------

export interface TrameNodeDirs {
  if?: string;
  elseIf?: string;
  else?: boolean;
  show?: string;
  for?: { item: string; index?: string | null; source: string; extra?: string };
  models?: { arg: string | null; modifiers: string[]; expr: string }[];
  text?: string;
  html?: string;
  slot?: { arg: string | null; expr: string | null };
  onObject?: string;
  bindObject?: string;
  custom?: Record<string, unknown>;
}

export interface TrameJsonNode {
  tag: string;
  attrs?: Record<string, string | number | boolean>;
  props?: Record<string, string>;
  on?: Record<string, string>;
  dirs?: TrameNodeDirs;
  raw?: string[];
  children?: TrameJsonChild[];
}

export type TrameJsonChild = string | { expr: string } | TrameJsonNode;

export interface TrameTemplatePayload {
  version: number;
  root: TrameJsonNode;
}

// Expression scope proxy (see renderer/evaluate.ts)
export type Scope = Record<string, any>;
