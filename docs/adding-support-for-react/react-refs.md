# Refs and Imperative Method Calls in trame's React `client_type`

> **Status: design exploration, just getting started.** Follow-on from
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 6, item 4
> ("Refs"). Nothing here is decided yet.

## 1. Can you call methods on a React component?

Two different cases, with very different answers:

- **Plain DOM elements** (`<input ref={r}>`, `<canvas ref={r}>`, ...) — yes,
  trivially. `ref.current` is the actual DOM node, so the full native element
  API is available with no extra work (`.focus()`, `.scrollIntoView()`,
  `.value`, ...).
- **Custom components** — no, not by default. Function components have no
  instance at all; `<MyWidget ref={r} />` yields `null` (and a dev warning)
  unless the component explicitly opts in.

## 2. The recommended pattern: `useImperativeHandle`

A component that wants to expose a callable API declares exactly what
`ref.current` will be:

```jsx
function MyChart({ ref, ...props }) {
  const canvasRef = useRef(null);

  useImperativeHandle(ref, () => ({
    resetZoom() {
      /* ... */
    },
    exportPNG() {
      return canvasRef.current.toDataURL();
    },
  }));

  return <canvas ref={canvasRef} {...props} />;
}
```

```jsx
// parent
const chartRef = useRef(null);
<MyChart ref={chartRef} />;
chartRef.current.resetZoom();
```

Notes:

- Pre-React 19, the component had to be wrapped in
  `forwardRef((props, ref) => ...)` to even receive `ref` as an argument.
  React 19 allows function components to accept `ref` as an ordinary prop
  directly (as above); `forwardRef` still works but is being phased out.
- React's own guidance is that the exposed handle should be **deliberately
  minimal and intentional** — a curated set of methods, not "everything the
  component happens to have internally." This is closer to Vue 3's
  `<script setup>` + `defineExpose()` model than to Vue 2's implicit "expose
  all of `this`."

## 3. Implication for trame's `ref=` design

Vue's `client_type` today is permissive: `AbstractElement.html` patches any
`ref=` attribute for vue3 into `:ref="(el) => trame.refs[name] = el"`
(`widgets/core.py`), and whatever ends up in `trame.refs[name]` — a DOM node or
a component's public instance — is fair game to call methods on from Python
(via `ctrl`/`js_call`-style triggers). Nothing about *what* gets exposed is
decided by the widget author at the point of authoring the ref; it's decided
implicitly by however much Vue's reactivity/instance system exposes.

React's model flips that: exposing anything beyond a raw DOM node requires the
**widget author** to explicitly write a `useImperativeHandle` call declaring
the public surface. That means, unlike the Vue path, a `client_type="react"`
widget isn't automatically "ref-able" with an arbitrary method surface — each
widget that wants to support calling methods on it needs to be written with
that in mind.

## 4. Resolved: a plain side map, decoupled from state

- **No standardized handle shape.** Each widget author decides what (if
  anything) it exposes via `useImperativeHandle`, exactly as loosely as Vue
  treats this today. trame imposes no fixed contract on the methods a ref
  must/can have.
- **Python doesn't need to distinguish the two cases.** `trame.refs[name]` is
  populated uniformly whether the registered value is a raw DOM node or a
  component's hand-written imperative handle — from Python's side, `ref=name`
  is just a string, and calling `refs[name].some_method(...)` works the same
  way regardless of which kind of object ended up under that name.
- **Refs are a side channel, not part of state.** `trame.refs` is a plain
  mutable map that lives outside React's render cycle entirely — it is not
  wired into whatever store [`react-fine-grained-reactivity.md`](./react-fine-grained-reactivity.md)
  settles on, and calling a method on a ref is a one-off imperative action with
  no round-trip into trame state, no reactivity concerns, and no interaction
  with React's render scheduling. This mirrors how Vue's `trame.refs` already
  behaves — it's an escape hatch, deliberately outside the reactive system.

## 5. Serialized shape and the `TrameNode` implementation

### Python side: no change

`ref` is already a plain shared attribute (`SHARED_ATTRIBUTES` in
`widgets/core.py`) — `html.Input(ref="my_input")` works identically for both
`client_type`s. There's nothing new to design on the Python-facing API; this
section is purely about serialization and the client runtime.

### Serialized shape: `ref` stays a plain string, keyed by prop name

Unlike `value`/`onChange`/other prop values (`vue-vs-react-with-trame.md`
section 3, `react-scoped-slots.md` section 4), `ref` doesn't need a wrapper
object like `{ "js": ... }` or `{ "callback": ... }` to disambiguate what kind
of value it is. There's nothing to disambiguate — a `ref` prop's value is
*always* "a name to register under," never a literal DOM attribute or a bound
expression, since React doesn't support passing a plain string as `ref`
either. So resolution here is dispatched by **prop key**, not by inspecting the
value's shape:

```json
{
  "tag": "input",
  "props": {
    "type": "text",
    "ref": "my_input"
  }
}
```

### `TrameNode` impact

The generic prop-resolution pass (section 3/4 of the other docs) gains one
more case, checked by key instead of by value shape:

```jsx
function resolveProps(rawProps, scope) {
  const resolved = {};
  for (const [key, value] of Object.entries(rawProps ?? {})) {
    if (key === "ref") {
      resolved.ref = getRefCallback(value); // value is the plain ref name
      continue;
    }
    resolved[key] = resolveProp(value, scope); // js / callback / slot / plain
  }
  return resolved;
}

// one stable callback per ref name, cached across renders
const refCallbacks = new Map();
function getRefCallback(name) {
  if (!refCallbacks.has(name)) {
    refCallbacks.set(name, (el) => {
      if (el) {
        trame.refs[name] = el;
      } else {
        delete trame.refs[name];
        refCallbacks.delete(name); // free to re-mint if this name resurfaces later
      }
    });
  }
  return refCallbacks.get(name);
}
```

### Why a callback ref, not `useRef`

This isn't a stand-in for `useRef` — it's the only option that actually works
here. React accepts two kinds of value for a `ref` prop: a ref *object* from
`useRef()` (React sets `.current` for you), or a plain callback *function*
(React calls it with the element on mount, `null` on unmount). Both are
first-class, documented mechanisms.

`useRef()` is a hook, so it's bound by the rules of hooks: called
unconditionally, the same number of times, in the same order, on every render
of a given component instance. `TrameNode` can't satisfy that — the set of ref
names to attach comes from a **dynamic, server-sent tree** that can differ
between renders (a widget might gain or lose a `ref=` between one state update
and the next, with an arbitrary name each time). There's no fixed number of
`useRef()` calls that could cover "however many differently-named refs this
particular render happens to contain" — the same dynamic-key problem already
called out for state atoms in `react-fine-grained-reactivity.md` (section 3).
A callback ref has no such restriction, since it's just a function value, not a
hook — constructible for any number of dynamically named targets, which is why
it's the right fit rather than an approximation of `useRef`. (Contrast this
with section 2's example, where `useRef` was used validly in hand-authored code
consuming one specific, statically-known widget — a different situation from
`TrameNode`'s arbitrary, dynamically-shaped tree.)

Two more things worth calling out:

- **Works identically for DOM elements and custom widgets.** `TrameNode`
  doesn't need to know or care which case it's attaching to — a host tag like
  `"input"` hands the callback the raw DOM node, a custom widget hands it
  whatever `useImperativeHandle` produced (or nothing, if the widget didn't
  opt in). Matches section 4: the map is populated uniformly either way.
- **The callback must be stable across renders, or React churns it.** If
  `getRefCallback` minted a fresh closure every render (the same "freshly-minted
  functions" issue flagged in `react-scoped-slots.md` section 6 and
  `react-fine-grained-reactivity.md`), React would treat every render as "ref
  changed" — detaching the old one (calling it with `null`) and attaching the
  new one — even though the target element never changed. Caching one callback
  per ref name avoids that churn. `el === null` on the cached callback still
  correctly signals real unmount/detachment, which is when `trame.refs[name]`
  should actually be cleared (and now, the cache entry along with it).
