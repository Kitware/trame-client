// Renders the server-sent JSON component tree (see trame_client/utils/react.py
// for the schema) into React elements.
//
// Event mapping convention (locked per PLAN.md §4.0):
// - native DOM tags: trame event "click" -> onClick, "mouseout.left.stop" ->
//   onMouseOut with modifiers applied; handler receives the React synthetic
//   event as $event.
// - registered components: trame event "change" -> prop onChange; $event is
//   the first callback argument.
// - v_model: native inputs get value/checked + onChange (modifiers: lazy ->
//   onBlur, number -> parseFloat, trim); registered components get
//   props[arg || "value"] + props["onUpdate" + Pascal(arg || "value")].

import React from "react";
import type { ReactNode } from "react";

import registry from "../registry";
import type {
  Scope,
  SlotFn,
  TrameInstance,
  TrameJsonChild,
  TrameJsonNode,
} from "../types";
import { createScope, evalExpr, execStatement } from "./evaluate";

const KEY_ALIASES: Record<string, string> = {
  enter: "Enter",
  tab: "Tab",
  delete: "Delete",
  esc: "Escape",
  space: " ",
  left: "ArrowLeft",
  up: "ArrowUp",
  right: "ArrowRight",
  down: "ArrowDown",
};
const MOUSE_BUTTONS: Record<string, number> = { left: 0, middle: 1, right: 2 };

const DOM_ATTR_MAP: Record<string, string> = {
  class: "className",
  for: "htmlFor",
  tabindex: "tabIndex",
  readonly: "readOnly",
  maxlength: "maxLength",
  minlength: "minLength",
  autocomplete: "autoComplete",
  autofocus: "autoFocus",
  spellcheck: "spellCheck",
  contenteditable: "contentEditable",
  crossorigin: "crossOrigin",
  srcset: "srcSet",
  colspan: "colSpan",
  rowspan: "rowSpan",
};

function pascal(name: string): string {
  return name
    .split(/[-_:]/)
    .map((t) => t.charAt(0).toUpperCase() + t.slice(1))
    .join("");
}

export function styleStringToObject(style: unknown) {
  if (typeof style !== "string") return style;
  const result: Record<string, string> = {};
  style.split(";").forEach((rule) => {
    const idx = rule.indexOf(":");
    if (idx === -1) return;
    const key = rule.slice(0, idx).trim();
    const value = rule.slice(idx + 1).trim();
    if (!key) return;
    const reactKey = key.startsWith("--")
      ? key
      : key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    result[reactKey] = value;
  });
  return result;
}

function domAttrName(name: string): string {
  return DOM_ATTR_MAP[name] || name;
}

function eventPropName(eventName: string): string {
  // "update:modelValue" -> onUpdateModelValue ; "click" -> onClick
  // names already in handler form ("onReady") are kept as-is
  if (/^on[A-Z]/.test(eventName)) return eventName;
  return `on${pascal(eventName)}`;
}

type Handler = (event?: any, ...rest: unknown[]) => unknown;

function wrapWithModifiers(handler: Handler, modifiers: string[]): Handler {
  if (!modifiers.length) return handler;
  const keys = modifiers.filter((m) => KEY_ALIASES[m] && !MOUSE_BUTTONS[m]);
  let fired = false;
  return (event?: any, ...rest: unknown[]) => {
    if (event && typeof event === "object") {
      if (modifiers.includes("self") && event.target !== event.currentTarget)
        return;
      if (
        keys.length &&
        event.key !== undefined &&
        !keys.some((k) => event.key === KEY_ALIASES[k])
      )
        return;
      if (
        event.button !== undefined &&
        modifiers.some((m) => m in MOUSE_BUTTONS) &&
        !modifiers.some((m) => event.button === MOUSE_BUTTONS[m])
      )
        return;
      if (modifiers.includes("stop")) event.stopPropagation();
      if (modifiers.includes("prevent")) event.preventDefault();
    }
    if (modifiers.includes("once")) {
      if (fired) return;
      fired = true;
    }
    return handler(event, ...rest);
  };
}

function parseEventKey(key: string) {
  const [name, ...tokens] = key.split(".");
  return { name, modifiers: tokens };
}

function buildEventProps(
  on: Record<string, string> | undefined,
  scope: Scope,
  props: Record<string, any>,
) {
  Object.entries(on || {}).forEach(([key, body]) => {
    const { name, modifiers } = parseEventKey(key);
    const captureSuffix = modifiers.includes("capture") ? "Capture" : "";
    const handler: Handler = ($event?: unknown) =>
      execStatement(body, scope, $event);
    props[`${eventPropName(name)}${captureSuffix}`] = wrapWithModifiers(
      handler,
      modifiers,
    );
  });
}

function buildModelProps(
  models: TrameJsonNode["dirs"] extends infer D
    ? D extends { models?: infer M }
      ? M
      : never
    : never,
  scope: Scope,
  tag: string,
  isDom: boolean,
  props: Record<string, any>,
) {
  (models || []).forEach(({ arg, modifiers, expr }) => {
    const current = evalExpr(expr, scope);
    const assign = (value: unknown) => {
      let v = value;
      if (modifiers.includes("number")) {
        const n = parseFloat(v as string);
        if (!Number.isNaN(n)) v = n;
      }
      if (modifiers.includes("trim") && typeof v === "string") v = v.trim();
      // expr is a state variable name (possibly translated); assign via scope
      execStatement(`${expr} = $event`, scope, v);
    };

    if (isDom) {
      const isCheckbox = tag === "input" && props.type === "checkbox";
      const isRadio = tag === "input" && props.type === "radio";
      const lazy = modifiers.includes("lazy");
      if (isCheckbox) {
        props.checked = !!current;
        props.onChange = (e: any) => assign(e.target.checked);
      } else if (isRadio) {
        props.checked = current === props.value;
        props.onChange = (e: any) => assign(e.target.value);
      } else {
        props.value = current === undefined || current === null ? "" : current;
        const apply = (e: any) => assign(e.target.value);
        if (lazy) {
          props.onBlur = apply;
          props.onChange = () => {};
        } else {
          props.onChange = apply;
        }
      }
    } else {
      const propName = arg || "value";
      props[propName] = current;
      props[`onUpdate${pascal(propName)}`] = (value: unknown) => assign(value);
    }
  });
}

function buildProps(
  node: TrameJsonNode,
  scope: Scope,
  isDom: boolean,
  trame: TrameInstance,
) {
  const props: Record<string, any> = {};
  Object.entries(node.attrs || {}).forEach(([name, value]) => {
    const key = isDom ? domAttrName(name) : name;
    props[key] = key === "style" ? styleStringToObject(value) : value;
  });
  Object.entries(node.props || {}).forEach(([name, expr]) => {
    const key = isDom ? domAttrName(name) : name;
    const value = evalExpr(expr, scope);
    props[key] = key === "style" ? styleStringToObject(value) : value;
  });

  const dirs = node.dirs || {};
  if (dirs.bindObject) {
    Object.assign(props, evalExpr(dirs.bindObject, scope) || {});
  }
  buildEventProps(node.on, scope, props);
  if (dirs.onObject) {
    const handlers = evalExpr(dirs.onObject, scope) || {};
    Object.entries(handlers).forEach(([name, fn]) => {
      props[eventPropName(name)] = fn;
    });
  }
  buildModelProps(dirs.models || [], scope, node.tag, isDom, props);

  if (dirs.show && !evalExpr(dirs.show, scope)) {
    props.style = { ...(props.style || {}), display: "none" };
  }
  if (dirs.text !== undefined) {
    props.children = evalExpr(dirs.text, scope);
  }
  if (dirs.html !== undefined) {
    props.dangerouslySetInnerHTML = { __html: evalExpr(dirs.html, scope) };
  }

  // ref -> trame.refs registration (parity with vue clients)
  if (typeof props.ref === "string") {
    const refName: string = props.ref;
    props.ref = (el: unknown) => {
      trame.refs[refName] = el;
    };
  }
  return props;
}

// Map slot props through the template's v-slot destructuring pattern,
// e.g. "{ keyName: var_key, value }" exposes slotProps.keyName as `var_key`
// and slotProps.value as `value` in the children scope.
export function mapSlotLocals(
  pattern: string | null | undefined,
  slotProps: Record<string, unknown>,
): Record<string, unknown> {
  if (!pattern) return {};
  const inner = pattern.trim().replace(/^\{/, "").replace(/\}$/, "");
  const locals: Record<string, unknown> = {};
  inner.split(",").forEach((part) => {
    const token = part.trim();
    if (!token) return;
    const [propName, localName] = token.split(":").map((t) => t.trim());
    locals[localName || propName] = slotProps[propName];
  });
  return locals;
}

function renderNode(
  node: TrameJsonNode,
  scope: Scope,
  trame: TrameInstance,
  key: string,
): ReactNode {
  const dirs = node.dirs || {};

  if (dirs.for) {
    const { item, index, extra, source } = dirs.for;
    const items = evalExpr(source, scope) || [];
    const entries = Array.isArray(items) ? items : Object.entries(items);
    return entries.map((value, i) => {
      const locals = { [item]: value };
      if (index) locals[index] = i;
      if (extra) locals[extra] = i;
      const childScope = createScope(trame, locals, scope);
      const restDirs = { ...dirs };
      delete restDirs.for;
      const child = { ...node, dirs: restDirs };
      return renderNode(child, childScope, trame, `${key}-${i}`);
    });
  }

  const component = registry.resolve(node.tag);
  const isDom = !component;
  const type = component || node.tag;
  const props = buildProps(node, scope, isDom, trame);
  props.key = props.key !== undefined ? props.key : key;

  let children;
  if (props.children !== undefined) {
    children = props.children; // v-text
    delete props.children;
  } else if (props.dangerouslySetInnerHTML) {
    children = undefined;
  } else if (!isDom) {
    // Scoped slot support: the component decides when/with which variables
    // its children render (e.g. TrameGetter exposes { value, update }).
    const slotMapping = dirs.slot?.expr;
    const slot: SlotFn = (slotProps = {}) =>
      renderChildren(
        node.children,
        createScope(trame, mapSlotLocals(slotMapping, slotProps), scope),
        trame,
      );
    props.slot = slot;
    children = slotMapping ? undefined : slot();
  } else {
    children = renderChildren(node.children, scope, trame);
  }

  if (children === undefined || (Array.isArray(children) && !children.length)) {
    return React.createElement(type, props);
  }
  return React.createElement(type, props, children);
}

export function renderChildren(
  children: TrameJsonChild[] | undefined,
  scope: Scope,
  trame: TrameInstance,
): ReactNode[] {
  if (!children) return [];
  const output: ReactNode[] = [];
  let lastIfValue: boolean | null = null; // tracks v-if/v-else-if/v-else chain

  children.forEach((child, i) => {
    if (typeof child === "string") {
      output.push(child);
      lastIfValue = null;
      return;
    }
    if ("expr" in child && !("tag" in child)) {
      const value = evalExpr(child.expr, scope);
      output.push(value === undefined || value === null ? "" : String(value));
      lastIfValue = null;
      return;
    }

    const dirs = (child as TrameJsonNode).dirs || {};
    if (dirs.if !== undefined) {
      lastIfValue = !!evalExpr(dirs.if, scope);
      if (!lastIfValue) return;
    } else if (dirs.elseIf !== undefined) {
      if (lastIfValue) return;
      lastIfValue = !!evalExpr(dirs.elseIf, scope);
      if (!lastIfValue) return;
    } else if (dirs.else) {
      if (lastIfValue) return;
      lastIfValue = null;
    } else {
      lastIfValue = null;
    }

    const rendered = renderNode(child as TrameJsonNode, scope, trame, `n${i}`);
    if (Array.isArray(rendered)) {
      output.push(...rendered);
    } else {
      output.push(rendered);
    }
  });

  return output;
}

export default function TrameNode({
  node,
  trame,
  scope,
}: {
  node: TrameJsonNode;
  trame: TrameInstance;
  scope?: Scope;
}) {
  const rootScope = scope || createScope(trame);
  const result = renderNode(node, rootScope, trame, "root");
  return Array.isArray(result) ? <>{result}</> : result;
}
