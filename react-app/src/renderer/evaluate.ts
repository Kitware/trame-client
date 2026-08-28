// Expression evaluation against the trame shared state.
//
// Expressions are the same JS snippets trame apps already use with the Vue
// clients ("count > 3", "count++", "trigger('name', [count])"). They are
// compiled once (cached) and invoked with a `with()` scope proxy backed by
// trame.state, so bare identifiers resolve to state variables.

import type { Scope, TrameInstance } from "../types";

type CompiledFn = ((scope: Scope, $event?: unknown) => unknown) | null;

const EXPR_CACHE = new Map<string, CompiledFn>();
const STMT_CACHE = new Map<string, CompiledFn>();

function compile(
  body: string,
  cache: Map<string, CompiledFn>,
  wrap: (body: string) => string,
): CompiledFn {
  let fn = cache.get(body);
  if (fn === undefined) {
    try {
      // eslint-disable-next-line no-new-func
      fn = new Function("$scope", "$event", wrap(body)) as CompiledFn;
    } catch (e) {
      console.error(`trame: failed to compile expression "${body}"`, e);
      fn = null;
    }
    cache.set(body, fn);
  }
  return fn;
}

export function createScope(
  trame: TrameInstance,
  extra: Record<string, unknown> = {},
  parent: Scope | null = null,
): Scope {
  const locals: Record<string, any> = { ...extra };
  const scope = new Proxy(locals, {
    has(target, key) {
      // claim every identifier so `with()` never falls through to globals
      // implicitly — EXCEPT the handler arguments, which must resolve to the
      // compiled function parameters ($event) instead of this scope.
      return key !== "$event";
    },
    get(target, key: string | symbol) {
      if (key === Symbol.unscopables) return undefined;
      if (typeof key === "symbol") return (target as any)[key];
      if (key in target) return target[key];
      if (parent) {
        const value = parent[key];
        if (value !== undefined) return value;
      }
      const state = trame?.state?.get?.();
      if (state && Object.prototype.hasOwnProperty.call(state, key)) {
        return state[key];
      }
      // scope API + escape hatches
      switch (key) {
        case "trame":
          return trame;
        case "window":
          return window;
        case "utils":
          return trame?.utils;
        case "trigger":
          return (name: string, args?: unknown[], kwargs?: Record<string, unknown>) =>
            trame.trigger(name, args, kwargs);
        case "set":
          return (name: string, value: unknown) => trame.state.set(name, value);
        case "get":
          return (name?: string) => trame.state.get(name);
        case "setAll":
          return (obj: Record<string, unknown>) => trame.state.update(obj);
        case "flushState":
          return (...keys: unknown[]) => trame.state.flush(...keys);
        default:
          // globals (Math, JSON, console, ...)
          return (globalThis as any)[key];
      }
    },
    set(target, key: string, value: unknown) {
      if (key in target) {
        target[key] = value;
      } else {
        trame.state.set(key, value);
      }
      return true;
    },
  });
  return scope;
}

export function evalExpr(expr: string, scope: Scope, $event?: unknown) {
  const fn = compile(expr, EXPR_CACHE, (b) => `with($scope){return(${b});}`);
  if (!fn) return undefined;
  try {
    return fn(scope, $event);
  } catch (e) {
    console.error(`trame: error evaluating "${expr}"`, e);
    return undefined;
  }
}

export function execStatement(body: string, scope: Scope, $event?: unknown) {
  // event handlers may be statements ("count++; other = 1") or expressions
  let fn = compile(body, EXPR_CACHE, (b) => `with($scope){return(${b});}`);
  if (!fn) {
    fn = compile(body, STMT_CACHE, (b) => `with($scope){${b}}`);
  }
  if (!fn) return undefined;
  try {
    return fn(scope, $event);
  } catch (e) {
    console.error(`trame: error executing "${body}"`, e);
    return undefined;
  }
}
