// Object.create-based prototype chain: JS property lookup along a prototype
// chain already implements "nearest enclosing scope wins, else fall through"
// for free, and composes directly with the Proxy in expr.js (the proxy wraps
// the chain head; `target[prop]` triggers the walk automatically). Nesting
// (For inside For, Slot inside For) is just another Object.create(currentFrame)
// call - no special nesting logic required.

const STATE_FACADE = { __isStateFacade: true };

export function extendScope(parentScope, names, values) {
  const frame = Object.create(parentScope ?? STATE_FACADE);
  names.forEach((name, i) => {
    frame[name] = values[i];
  });
  return frame;
}

function isFacadeMarker(obj) {
  return !!obj && Object.prototype.hasOwnProperty.call(obj, "__isStateFacade");
}

// scope's own chain was already built against the static STATE_FACADE marker
// at extendScope() time, not a live trameState-backed proxy, so this walks
// the chain re-rooting the terminal marker onto a fresh, live facade - every
// intermediate For/Slot frame is preserved along the way (unlike a flat
// `Object.assign(Object.create(facade), scope)`, which would only copy the
// OUTERMOST frame's own properties and silently lose everything an enclosing
// For/Slot introduced further up the chain).
export function buildMergedScope(scope, trameState) {
  const facade = new Proxy(STATE_FACADE, {
    // Only claims identifiers that are actually trame state keys, so a
    // Callback's `count = ...` writes back to trame state and a Bind's bare
    // `count` reads it - while still letting `with` fall through to the
    // REAL global scope for anything else (Number, Math, ...): if `has`
    // claimed every identifier unconditionally, `with` would never even
    // consult the outer scope, and `Number(...)` would read as
    // `trameState.get("Number")` (undefined) instead of the global function.
    has: (_t, prop) =>
      prop === "__isStateFacade" || trameState.get(String(prop)) !== undefined,
    get: (_t, prop) =>
      prop === "__isStateFacade" ? true : trameState.get(String(prop)),
    set: (_t, prop, value) => {
      trameState.set(String(prop), value);
      return true;
    },
  });

  if (!scope) return facade;

  // Object.assign would route through facade's `set` trap instead of
  // defining an own property (target starts out empty, so the assignment
  // finds no own property and walks up to facade's inherited setter) -
  // defineProperty bypasses the prototype chain entirely, so each frame's
  // own bindings actually land on the rebuilt object instead of leaking
  // into trame state.
  const rebase = (frame) => {
    const parent = Object.getPrototypeOf(frame);
    const rebasedParent = isFacadeMarker(parent) ? facade : rebase(parent);
    const next = Object.create(rebasedParent);
    Object.keys(frame).forEach((key) => {
      Object.defineProperty(
        next,
        key,
        Object.getOwnPropertyDescriptor(frame, key),
      );
    });
    return next;
  };
  return rebase(scope);
}

// Distinguishes "resolved from a For/Slot-introduced local variable" (not
// tracked - shadowing, not state) from "resolved from trame state" (tracked,
// becomes a state.watch dependency). Stops exactly at the facade/sentinel
// frame itself (checked via hasOwnProperty, since every frame *inherits*
// `__isStateFacade` from that terminal marker - a plain truthy check would
// short-circuit on the very first frame, defeating the whole walk).
export function hasOwnLocal(frame, prop) {
  let f = frame;
  while (f && !Object.prototype.hasOwnProperty.call(f, "__isStateFacade")) {
    if (Object.prototype.hasOwnProperty.call(f, prop)) return true;
    f = Object.getPrototypeOf(f);
  }
  return false;
}
