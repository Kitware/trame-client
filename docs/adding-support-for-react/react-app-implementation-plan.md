# `react-app/` — React client for `client_type="react"`

> **Status: implementation plan, not yet built.** Written after
> `src/trame_client/widgets/react.py`, `widgets/core.py`'s `client_type`
> dispatch, and `widgets/generator.py`'s React-flavored prop generation were
> already implemented and committed (covered by `tests/test_react.py`).
> `module/__init__.py`'s `client_type == "react"` branch is still a no-op
> because no client bundle exists yet — this document designs that missing
> piece. Cross-referenced against the design docs in this directory
> (`react-getting-started.md`, `react-refs.md`, `react-scoped-slots.md`,
> `react-text-interpolation.md`, `vue-vs-react-with-trame.md`) and against the
> existing `vue3-app/` and `js-lib/` implementations it's meant to mirror.

## Context

`trame-client` currently ships two Vue-based clients (`vue2-app`, `vue3-app`, built into `src/trame_client/module/{vue2,vue3}-www` and served by `module/vue2.py`/`module/vue3.py`). The Python side has been extending support for a third, `client_type="react"`: `src/trame_client/widgets/react.py` (a full `AbstractElement._impl` implementation producing a serializable `{tag, props, children}` JSON tree instead of a Vue template string), `widgets/core.py` (dispatches `_impl` by `client_type`), and `widgets/generator.py` (emits React-flavored camelCase prop names for every generated `html.*` element) are already implemented, committed on this branch, and covered by `tests/test_react.py`. `module/__init__.py`'s `client_type == "react"` branch is still a no-op (`pass`) because **no client bundle exists yet** — there is no `react-app/` to build one.

This plan designs that missing piece: a Vite/React app, structurally mirroring `vue3-app/`, that (a) connects to the trame server using `js-lib` (published as `@kitware/trame`, already a complete, framework-agnostic reimplementation of the connect/state/wslink layer — do not duplicate it, the way `vue3-app` still duplicates its own older copy of that logic), and (b) walks the JSON tree `react.py` produces via a generic `<TrameNode>` renderer, per the design worked out in `docs/adding-support-for-react/`.

**Scope, per discussion with the user:** core primitive layer only — the app shell, `<TrameNode>`, `Bind`/`Callback`/`If`/`For`/`Slot`/`ref` resolution, and just enough of `widgets/trame.py`'s helper widgets to boot (`ServerTemplate`, `Loading`). The wider widget ecosystem and the rest of `widgets/trame.py` (`Getter`, `DeepReactive`, `Handler`, `Style`, `Script`, `ClientTriggers`, `SizeObserver`, `LifeCycleMonitor`, `ClientStateChange`) stay Vue-only for now — several of them currently poke raw Vue `v-slot`/`v-bind` strings directly and aren't react-compatible; fixing that is explicitly deferred, noted as follow-up.

**Reactivity, per discussion with the user:** no new state-management dependency (no Redux/Zustand/Jotai/Valtio). Build on React's `useSyncExternalStore` wired to js-lib's `State.watch(keys, fn)` (already a dynamic per-key subscription primitive), plus a small home-grown expression evaluator that auto-discovers which state keys/scope vars each `{js: ...}` expression actually reads (Valtio-style dependency tracking via a `Proxy`, but self-contained).

---

## 1. Scaffold

```
react-app/
  package.json
  vite.config.js
  index.html
  src/
    main.jsx
    style.css
    setup.js              # page-resource loading, ported from vue3-app/src/core/trame/setup.js
    messageChannel.js      # verbatim port of vue3-app/src/messageChannel.js
    components/
      TrameApp.jsx
      TrameTemplate.jsx
      TrameLoading.jsx
      TrameReconnect.jsx
      TrameNode.jsx
      ReactIf.jsx
      ReactFor.jsx
    runtime/
      trameContext.js     # React context wrapping {trame, getRefCallback}
      scope.js             # scope-chain (extendScope, buildMergedScope, hasOwnLocal)
      expr.js               # compile cache + Proxy dependency tracking (evalTracked)
      resolveNode.js         # useResolvedNode: the one hook-call-site per TrameNodeOne
      refs.js                 # callback-ref registry
      tags.js                  # tag -> component registry (resolveTag/registerTag)
  tests/  (vitest, mirrors js-lib/tests/ conventions)
```

### `package.json`

```json
{
  "name": "trame-app-react",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "vite build --emptyOutDir",
    "debug": "vite build --sourcemap -m dev",
    "dev": "vite",
    "test": "vitest run"
  },
  "dependencies": {
    "@kitware/trame": "file:../js-lib",
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.0",
    "@testing-library/react": "^16.0.0",
    "jsdom": "^27.4.0",
    "vite": "^8.0.11",
    "vitest": "^4.1.11"
  }
}
```

- **React 19**: `react-refs.md` §2 relies on function components taking `ref` as an ordinary prop with no `forwardRef` boilerplate.
- **`@kitware/trame: file:../js-lib`**: no npm-workspace tooling exists in this repo (confirmed — no root `package.json`, no `pnpm-workspace.yaml`); `file:` is the simplest way to consume the in-repo js-lib during co-development, and resolves through js-lib's real `dist/` build (its `package.json` `main`/`module`/`types` point at `dist/trame.umd.js`/`dist/trame.mjs`/`dist/main.d.ts`) — **so `js-lib` must be built (`npm ci && npm run build`) before `react-app` is `npm ci`'d/built.**
- **One required, additive change to js-lib**: `js-lib/src/main.ts` currently only exports `Trame` (default) + types. `react-app` also needs `configDecorator`/`createClient` (from `js-lib/src/wslink/index.ts`) and `extractURLParameters` (from `js-lib/src/URLExtract.ts`) — neither is re-exported today. Add them as named exports from `main.ts`. This is additive (no signature changes to anything existing), and is the only js-lib change this plan requires.

### `vite.config.js`

```js
import react from "@vitejs/plugin-react";

export default {
  base: "./",
  plugins: [react()],
  build: {
    outDir: "../src/trame_client/module/react-www",
  },
};
```

Mirrors `vue3-app/vite.config.js` exactly, plus the JSX plugin (for react-app's *own* components — unrelated to the "no compiler ships for the widget tree" decision: `TrameNode` still calls `React.createElement` directly for the dynamic tree since `tag` is a runtime string, never JSX).

### `index.html`

Same shape as `vue3-app/index.html` (meta tags, `data-app-name`/`data-launcher-retry` dataset attrs consumed by `configDecorator`, `#app` div, the `loading.tpl`-fetch-and-inline-before-connect trick), minus `<script src="vue.global.js">` (no global Vue runtime), with `<script type="module" src="/src/main.jsx"></script>`.

### `src/main.jsx`

Bootstrap sequence ported from `vue3-app/src/main.js`, rebased directly onto js-lib's `Trame` class (no `core/trame`/`core/wslink` duplication):

1. Cross-origin-safe `window.parent.trameJupyter.init` check (verbatim).
2. `const trame = new Trame(window.WSLINK)`; `configDecorator({application: "trame", useUrl: true})`.
3. URL-param cleanup (verbatim port of the `paramsToClean` block).
4. `await trame.connect(config)` — on failure, render `<TrameReconnect>`/`<TrameLoading>` directly via `createRoot(...).render(...)` instead of Vue's pre-mount state-key-write trick (React doesn't need a template round-trip through state to render arbitrary content before the app tree exists — simpler than the Vue original, not a gap).
5. `console.error` override forwarding to `trame.client.getRemote().Trame.sendError(...)` (verbatim).
6. `handlePageResources(trame.state.get())` from `./setup.js` — styles/scripts/module_scripts/favicon/title only (see §9, `trame__vue_use` has no React equivalent and is dropped).
7. `createRoot(document.getElementById("app")).render(<TrameApp trame={trame} />)`.
8. Bottom-of-file service-worker (`enableSharedArrayBufferServiceWorker`) and `wsChannel`/`MessageChannel` proxy bootstrapping — verbatim port of the corresponding block in `vue3-app/src/main.js`.

### `src/setup.js`, `src/messageChannel.js`

Ports of `vue3-app/src/core/trame/setup.js` and `vue3-app/src/messageChannel.js` — both are framework-agnostic DOM/browser code with no Vue dependency; copy near-verbatim. `setup.js` drops the `trame__vue_use` → `state.trame__vue_use.map(...)` tail of `handlePageResources` (no plugin-registration concept in React).

---

## 2. `<TrameNode>` — the generic JSON-tree renderer

`src/components/TrameNode.jsx` is two components:

```jsx
export default function TrameNode({ nodes, scope }) {
  if (nodes == null) return null;
  const trame = useTrame();
  const list = Array.isArray(nodes) ? nodes : [nodes];
  return list.map((node, i) => (
    <TrameNodeOne key={computeNodeKey(node, scope, trame, i)} node={node} scope={scope} />
  ));
}

function TrameNodeOne({ node, scope }) {
  if (typeof node === "string") return node;
  if (isBindLeaf(node)) return <ExprLeaf jsExpression={node.js} scope={scope} />;
  if (!node || node.tag === undefined) return null;

  const Component = resolveTag(node.tag);
  const { props } = useResolvedNode(node, scope);   // the ONE hook-call-site, see §2.2

  if (isStructuralTag(node.tag)) {
    return createElement(Component, { ...props, rawChildren: node.children, scope });
  }
  const children = node.children?.length
    ? createElement(TrameNode, { nodes: node.children, scope })
    : undefined;
  return createElement(Component, props, children);
}
```

- **`computeNodeKey`** (plain function, no hooks): if `node?.props?.key` is a `{js: expr}` leaf, evaluate it synchronously (via `evalTracked`, no subscription — the enclosing `TrameNode` already re-renders whenever its own reactive inputs change, so a fresh read here is always current); if it's a plain scalar, use it directly; otherwise fall back to the array index `i`. This has to happen at the *parent's* `.map()` step, not inside `TrameNodeOne`, because React needs an element's `key` before that element is even created/mounted.
- **Structural tags** (`ReactIf`, `ReactFor`) get their raw, unresolved `children` + the current `scope` passed as ordinary props (`rawChildren`, `scope`) instead of a pre-built `<TrameNode>` — they need to control *whether* and *with what extended scope* their children render, which a pre-resolved child element can't express. Every other tag (DOM host tags, and any future custom-widget tag) gets its children pre-wrapped in a nested `<TrameNode>`, exactly like any other prop.
- **`key=`** needs no special-casing beyond `computeNodeKey` above: React's `createElement` already strips a `key` found in the props object before handing `props` to the component, so `key` also going through the normal reactive-prop path in `useResolvedNode` (§2.2) alongside everything else is harmless, if slightly redundant.

### 2.1 Prop-resolution order

By **prop key** first, then by **value shape**, matching `react-refs.md` §5 / `react-scoped-slots.md` §4 exactly:

1. `key === "ref"` → dispatch to the ref-callback registry (§5). `ref`'s value is *always* a plain string (a name to register under), never wrapped — checked by key, not shape.
2. Everything else, checked by value shape: `"js" in value` → reactive expression; `"callback" in value` → event handler; `"slot" in value` → render-prop generator; otherwise → plain passthrough.

### 2.2 `useResolvedNode` — one hook-call-site per node (`runtime/resolveNode.js`)

A naive design calls a hook (`useTrameExpr`, `useMemo` for each callback, ...) once per prop while iterating `Object.entries(node.props)` — that's a **Rules-of-Hooks violation risk** (hook-call count/order would depend on how many reactive/callback props a given node happens to have) and needlessly creates one `useSyncExternalStore` subscription per reactive prop instead of one per node. Instead, `useResolvedNode(node, scope)` is a **single hook**, always called the same way regardless of node shape, that internally batches all of a node's reactive props into one subscription:

```js
export function useResolvedNode(node, scope) {
  const trame = useTrame();

  // Pure, non-hook classification of node.props — cheap object walk.
  const { reactive, callbacks, slots, ref, static_ } = classifyProps(node.props);

  // One subscription for the whole node's reactive props (Bind-valued
  // props, including a Bind-valued `key`), keyed on the UNION of every
  // state key any of them actually reads.
  const trackedKeys = useMemo(() => {
    const merged = buildMergedScope(scope, trame.state);
    const keys = new Set();
    reactive.forEach(([, expr]) => evalTracked(expr, merged).keys.forEach((k) => keys.add(k)));
    return [...keys];
  }, [reactive, scope, trame.state]);

  const reactiveValues = useSyncExternalStore(
    (onChange) => trame.state.watch(trackedKeys, onChange),
    () => Object.fromEntries(
      reactive.map(([key, expr]) => [key, evalTracked(expr, buildMergedScope(scope, trame.state)).value]),
    ),
  );

  // One memo for all callback props, content-keyed (not identity-keyed) so
  // a re-render doesn't mint fresh handler functions unless the underlying
  // js/trigger/args/modifiers actually changed (see §2.3, §6).
  const callbackDepKey = callbacks.map(([k, v]) => k + JSON.stringify(v)).join("|");
  const callbackValues = useMemo(
    () => Object.fromEntries(callbacks.map(([key, spec]) => [key, makeCallbackHandler(spec, scope, trame)])),
    [callbackDepKey, scope, trame],
  );

  // Slots: no subscription needed - just capture children/scope, cheap to rebuild.
  const slotValues = Object.fromEntries(slots.map(([key, spec]) => [key, makeSlotRenderProp(spec, scope)]));

  const props = { ...Object.fromEntries(static_), ...reactiveValues, ...callbackValues, ...slotValues };
  if (ref) props.ref = getRefCallback(ref);
  return { props };
}
```

This gives a **fixed hook sequence** (`useTrame`/context read → `useMemo` → `useSyncExternalStore` → `useMemo`) per `TrameNodeOne` instance, independent of how many props of which kind that node has — safe under the Rules of Hooks, and far cheaper than one subscription per reactive prop.

### 2.3 Reactive expression evaluator (`runtime/expr.js`)

```js
const compiledCache = new Map(); // expression string -> Function, never evicted (finite, server-authored set)

export function compile(jsExpression) {
  let fn = compiledCache.get(jsExpression);
  if (!fn) {
    // eslint-disable-next-line no-new-func -- same trust model Vue's compiled
    // templates already accept: expression strings are server/app-author-controlled.
    fn = new Function("scope", `with (scope) { return (${jsExpression}); }`);
    compiledCache.set(jsExpression, fn);
  }
  return fn;
}

export function evalTracked(jsExpression, mergedScope) {
  const tracked = new Set();
  const proxy = new Proxy(mergedScope, {
    has() { return true; }, // force every free identifier through `get`, see below
    get(target, prop) {
      if (typeof prop === "string" && !hasOwnLocal(target, prop)) tracked.add(prop);
      return target[prop];
    },
  });
  return { value: compile(jsExpression)(proxy), keys: [...tracked] };
}
```

- `with (scope) { ... }` inside a `Function`-constructed body works even though the calling module is strict (bodies created via the `Function` constructor are *not* strict by default) — this is what lets a bare identifier like `count` in a Python-authored expression resolve against an arbitrary runtime object without the caller having named it as a parameter.
- `with` probes the scope's `has` trap for every free identifier before falling through to outer/global scope; returning `true` unconditionally forces every identifier through `get`, which is where tracking happens.
- `hasOwnLocal` (§3) distinguishes "resolved from a `For`/`Slot`-introduced local variable" (not tracked — shadowing, not state) from "resolved from trame state" (tracked, becomes a `state.watch` dependency).
- **Cost**: two evaluations of a small cached `Function` over a small object per render pass (one via `useMemo` to compute `trackedKeys`, one inside `getSnapshot`) — required because `useSyncExternalStore`'s `getSnapshot` must be a pure function of only its own closure, not of a value computed earlier in the same render.
- **Resubscription semantics**: `state.watch(keys, fn)`'s dependency list is fixed for the life of one subscription, so an expression like `state[mode === "a" ? "x" : "y"]` correctly triggers a new subscription (via `trackedKeys` changing identity in the `useMemo`) when `mode` flips — matches how Valtio's own dependency tracking behaves, not a shortcut.

### 2.4 Scope chain (`runtime/scope.js`)

Chosen shape: **`Object.create`-based prototype chain**, not an explicit array — JS property lookup along a prototype chain already implements "nearest enclosing scope wins, else fall through" for free, and composes directly with the `Proxy` in §2.3 (the proxy wraps the chain head; `target[prop]` triggers the walk automatically). Nesting (`For` inside `For`, `Slot` inside `For`) is just another `Object.create(currentFrame)` call — no special nesting logic (resolves the "nested scoped slots" open question in `react-scoped-slots.md` §6 for the common case).

```js
export function extendScope(parentScope, names, values) {
  const frame = Object.create(parentScope ?? STATE_FACADE);
  names.forEach((name, i) => { frame[name] = values[i]; });
  return frame;
}

const STATE_FACADE = { __isStateFacade: true };

export function buildMergedScope(scope, trameState) {
  const facade = new Proxy(STATE_FACADE, {
    get: (_t, prop) => (prop === "__isStateFacade" ? true : trameState.get(String(prop))),
  });
  return scope ? Object.assign(Object.create(facade), scope) : facade;
  // (see note below on why this needs one more pass than a naive "just set
  // scope's ultimate prototype to facade" — scope's own chain was already
  // built against a static STATE_FACADE marker at extendScope() time, not a
  // live trameState-backed proxy, so buildMergedScope re-roots it per call.)
}

function hasOwnLocal(frame, prop) {
  while (frame && !frame.__isStateFacade) {
    if (Object.prototype.hasOwnProperty.call(frame, prop)) return true;
    frame = Object.getPrototypeOf(frame);
  }
  return false;
}
```

This is the single fiddliest piece in the whole plan — worth deliberate unit tests (§10): a loop variable or slot param shadowing a same-named state key must never be recorded as a `state.watch` dependency.

---

## 3. `ReactIf` / `ReactFor` (`components/ReactIf.jsx`, `components/ReactFor.jsx`)

Both are plain presentational components — `value`/`items` arrive already resolved (via `useResolvedNode` in the parent `TrameNodeOne`, §2.2), so neither needs its own hooks:

```jsx
export default function ReactIf({ value, rawChildren, scope }) {
  return value ? <TrameNode nodes={rawChildren} scope={scope} /> : null;
}
```

```jsx
export default function ReactFor({ items, name, rawChildren, scope }) {
  return (items ?? []).map((item, index) => (
    <TrameNode key={index} nodes={rawChildren} scope={extendScope(scope, [name], [item])} />
  ));
}
```

`ReactFor` uses the array index as its own React key (no other generically-available stable identity — `react.For` doesn't mandate items carry an id). A widget author wanting stable row identity across reordering puts an explicit `key=` on the element(s) inside the `For` body, which is honored one level down by `computeNodeKey` (§2) inside the nested `<TrameNode>` — not by `ReactFor`'s own `.map()`. Per-row fine-grained memoization beyond this is out of scope (§10).

---

## 4. Callback resolution (`makeCallbackHandler`, part of `runtime/resolveNode.js`)

```js
const MODIFIER_HANDLERS = { prevent: (e) => e.preventDefault(), stop: (e) => e.stopPropagation() };

function makeCallbackHandler({ callback, modifiers }, scope, trame) {
  return (event) => {
    modifiers?.forEach((m) => MODIFIER_HANDLERS[m]?.(event));
    const merged = buildMergedScope(extendScope(scope, ["$event"], [event]), trame.state);
    if ("js" in callback) {
      compile(callback.js)(merged);
      return;
    }
    const args = callback.args ? compile(callback.args.js)(merged) : [];
    const kwargs = callback.kwargs ? compile(callback.kwargs.js)(merged) : {};
    trame.trigger(callback.trigger, args, kwargs);
  };
}
```

- The DOM event is exposed as an ordinary scope binding under the name `$event` (matching `react.py`/`react-getting-started.md`'s convention exactly, e.g. `onChange=react.Callback("count = Number($event.target.value)")`), via the same `extendScope` mechanism as loop vars.
- `callback.args`/`callback.kwargs` are themselves `{js: "..."}`-wrapped expression strings (per `react.py`'s `Callback.to_json`), evaluated fresh **at call time** against the scope captured when the handler was created — correct, since Python's `args`/`kwargs` are meant to be re-evaluated per call, not memoized as a static value.
- **Memoization**: `useResolvedNode` (§2.2) already memoizes the whole `callbacks` map per node via one `useMemo` keyed on a content hash (`key + JSON.stringify(spec)`) plus `scope`/`trame` identity — avoids minting a fresh function every render (the "freshly-minted functions" problem flagged in `react-scoped-slots.md` §6 / `react-fine-grained-reactivity.md` §1) while still correctly re-minting when `scope` changes (e.g., each `For` row is a distinct component instance via `key`, so this mostly guards the same instance's scope value changing across renders without a full remount).

---

## 5. Ref callback registry (`runtime/refs.js`)

Direct transcription of `react-refs.md` §5, instantiated once per `trame` instance (since `trame.refs` — from `js-lib/src/trame.ts` — is per-connection: a fresh `Trame()` on reconnect gets a fresh `refs` map):

```js
export function createRefRegistry(trame) {
  const cache = new Map();
  return function getRefCallback(name) {
    if (!cache.has(name)) {
      cache.set(name, (el) => {
        if (el) trame.refs[name] = el;
        else { delete trame.refs[name]; cache.delete(name); }
      });
    }
    return cache.get(name);
  };
}
```

Exposed via `TrameContext` (`runtime/trameContext.js`, `createContext({trame, getRefCallback})`) alongside `trame` itself, so `useResolvedNode` can call it for `ref=` props (§2.1).

---

## 6. Tag registry (`runtime/tags.js`)

```js
const registry = { ReactIf, ReactFor };
export function registerTag(name, Component) { registry[name] = Component; }
export function isStructuralTag(tag) { return tag === "ReactIf" || tag === "ReactFor"; }
export function resolveTag(tag) {
  if (tag in registry) return registry[tag];
  if (/^[a-z]/.test(tag)) return tag; // lower-case first char => real DOM host tag
  console.warn(`TrameNode: unknown tag "${tag}", rendering nothing`);
  return () => null;
}
```

`tags.js` never imports from `components/` (avoids an import cycle with `TrameNode.jsx`); `TrameApp.jsx` calls `registerTag("trame-loading", TrameLoading)` / `registerTag("trame-template", TrameTemplate)` once at module load, before first render. This flat registry **is** the extension point a future custom-widget ecosystem would grow into — no dynamic registration API beyond `registerTag` is designed now, since there's nothing real yet to register against it (§10).

---

## 7. App shell

### `components/TrameApp.jsx`

Responsibilities ported from `vue3-app/src/components/TrameApp.js`, **minus** per-`trame__template_*`-name dynamic-component registration (no Vue-style "register a component by string name" system to feed — `TrameTemplate` just reads its state key directly and hands the dict to `TrameNode`). Keeps: connection-ready gating, `onClose`/reconnect-driven re-render (`refreshTS`), the `beforeunload` → `lifeCycleUpdate("client_exited")` hookup, `client_unmounted` on unmount.

### `components/TrameTemplate.jsx`

Direct analog of `vue3-app/src/components/TrameTemplate.js`'s default export (not its separate `setup()` helper, which exists only to build a Vue-instance-reactive API object for Vue's template compiler — no equivalent need here, since `TrameNode` reads `trame.state`/scope directly):

```jsx
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
```

Simpler than the Vue original precisely because there's no dynamic-component-by-name indirection to replicate — `AbstractLayout.flush_content()` (`src/trame_client/ui/core.py`) already puts the JSON tree dict directly into that state key (confirmed via `tests/test_react.py`: `root.html` is a `dict`).

### `components/TrameLoading.jsx`, `components/TrameReconnect.jsx`

Near-verbatim ports of `vue3-app/src/components/TrameLoading.js` / `TrameReconnect.js` — same markup/CSS classes (`trame__loader`/`trame__message`, copy the relevant rules from `vue3-app/src/style.css` into `react-app/src/style.css`), swapping `onMounted`/`onBeforeUnmount`/`inject("trame")` for `useEffect`/`useTrame()`.

---

## 8. Python-side wiring

### `src/trame_client/module/react.py` (new)

```python
from pathlib import Path

www = str(Path(__file__).with_name("react-www").resolve())
```

Exact mirror of `module/vue3.py`.

### `src/trame_client/module/__init__.py`

Replace the current no-op branch:

```python
    elif client_type == "react":
        from . import react

        server.enable_module(react)
        setup_handler_module(server)
```

(`setup_handler_module` — already defined in this file — wires up `trame__scripts`/`trame__module_scripts` serving for user-provided external scripts; included for parity since `react-app/src/setup.js` already handles those state keys, §1.)

### Build tooling

- `noxfile.py`: `VUE_APPS` (currently `{"vue2-app": ..., "vue3-app": ...}`) gains `"react-app": Path("src/trame_client/module/react-www")`. Since `react-app` additionally depends on `js-lib`'s build output, add a step that builds `js-lib` first (`npm ci && npm run build` inside `js-lib/`, only if `js-lib/dist` doesn't already exist) before `_ensure_vue_apps_built` iterates into `react-app`.
- `pyproject.toml`: `[tool.hatch.build] include` currently lists `/src/trame_client/module/vue2-www/**` and `/src/trame_client/module/vue3-www/**` explicitly — add `/src/trame_client/module/react-www/**` alongside them.

---

## 9. Explicitly deferred / out of scope

- **Widget ecosystem port** (a Vuetify-equivalent, `VDataTable`, etc.) — `registerTag` (§6) is the only extension point; nothing real registers against it in this plan.
- **`widgets/trame.py` widgets beyond `Loading`/`ServerTemplate`**: `Getter`, `DeepReactive`, `Handler`, `Style`, `Script`, `ClientTriggers`, `SizeObserver`, `LifeCycleMonitor`, `ClientStateChange` stay Vue-only (several poke raw Vue `v-slot`/`v-bind` strings directly today and need Python-side rework first) — follow-up, not attempted here.
- **`trame__vue_use`** (Vue-plugin registration via `state.trame__vue_use`) — no React equivalent; silently dropped from `setup.js`.
- **Per-row `For` memoization beyond index-based `key`** — acceptable at this scope (§3).
- **A real component registry / dynamic tag resolution beyond the flat object in `tags.js`** — fine for two structural tags plus two lifecycle widgets; would need real design once actual custom widgets exist.
- **`react.py`/`widgets/core.py`'s existing contract is untouched** — nothing here proposes changing the already-committed Python tree-serialization code.
- **The one required js-lib change** (§1: additive named exports from `main.ts`) is the sole out-of-band dependency this plan has on code outside `react-app/` itself.

---

## 10. Verification

### Manual smoke test

1. `cd js-lib && npm ci && npm run build`
2. `cd react-app && npm ci && npm run build` → produces `src/trame_client/module/react-www`
3. New example, `examples/react/reactive_state.py`, mirroring `examples/vue3/reactive_state.py`'s style (`from trame.app import get_server`, `from trame.widgets import html, react`, `from trame.ui.html import DivLayout` — all confirmed real/working imports via `tests/test_react.py`, which already does `from trame.widgets import html, react`):

```python
from trame.app import get_server
from trame.widgets import html, react
from trame.ui.html import DivLayout

server = get_server(client_type="react")
state = server.state
state.count = 2
state.todos = ["Write docs", "Review PR", "Ship it"]


def reset(value=2):
    state.count = value


with DivLayout(server) as layout:
    html.Div(["count = ", react.Bind("count", count=2)])
    html.Input(
        type="range", min=0, max=10, step=1,
        value=react.Bind("count", count=2),
        onChange=react.Callback("count = Number($event.target.value)"),
    )
    html.Button("Reset", onClick=react.Callback(reset))
    with react.If(value="todos.length > 0"):
        with html.Ul():
            with react.For(items="todos", name="todo"):
                html.Li([react.Bind("todo")], key=react.Bind("todo"))

server.start()
```

4. `python examples/react/reactive_state.py`, open the browser. Checklist:
   - Page connects and renders (no stuck `TrameLoading`).
   - Dragging the range input updates the displayed count live; clicking Reset sets it back to 2.
   - The todo list renders from `For`, disappears if `todos` is emptied (via a second trigger, or manually through devtools) and the "empty" `If` branch would need adding to fully exercise both branches.
   - Add a temporary `console.log` in an unrelated sibling node to confirm it does *not* re-render when only `count` changes — validates fine-grained subscription (§2.2/§2.3) is actually narrow, not tree-wide.
   - `?reconnect=auto` after killing/restarting the server process exercises `TrameReconnect`.

### Automated tests

`js-lib/tests/` (vitest + `jsdom`, `describe`/`it`/`expect`, a `helpers/fakeClient.ts`-style fake) is the pattern to follow; add `react-app/vitest.config.js` in the same shape plus `@testing-library/react`. Priority coverage, given §2.4/§2.3 are the novel/fiddly pieces:

- `runtime/scope.test.js` — `extendScope` nesting (`For` inside `For`, `Slot` inside `For`) preserves shadowing; `hasOwnLocal` stops correctly at the state-facade sentinel.
- `runtime/expr.test.js` — same expression string reuses the cached `Function`; dependency tracking records only identifiers actually read (a ternary only tracks its taken branch); a scope-chain local shadowing a same-named state key is never tracked as a `state.watch` dependency (the critical regression case).
- `components/TrameNode.test.jsx` (`@testing-library/react` + a fake `trame`) — renders a `{tag:"div", props:{className:"x"}, children:["hi"]}` tree to the expected DOM; a `{"js":"count"}` child re-renders only when `count` changes (render-count spy); `ref="name"` populates `trame.refs.name` on mount, removes it on unmount.
- `components/ReactFor.test.jsx` — each row's scope correctly isolates its own loop variable (row *N* must not see row *N-1*'s value).
- `runtime/resolveNode.test.js` — `{callback:{trigger:"foo", args:{js:"[$event.target.value]"}}}` calls `trame.trigger("foo", [value], {})` with correctly-evaluated args; `modifiers:["prevent"]` calls `event.preventDefault()`.

No browser/e2e suite is proposed here beyond the manual smoke test — the repo's root `tests/` already has Playwright coverage for vue2/vue3 per `noxfile.py`; extending that to drive `react-app` once built is a natural, separate follow-up.

---

## Appendix: grounding notes from codebase review

Cross-checked against the actual repo state (2026-09-03, branch `add-react-support`) before implementation:

- `js-lib/src/main.ts` today exports only `Trame` (default) plus `TrameConnectConfig`/`Decorator`/`StateChangeEvent` types — confirms §1's "one required js-lib change" is real and additive. `js-lib/src/wslink/index.ts` exports a default object `{ configDecorator, createClient }` (not named exports) and `js-lib/src/URLExtract.ts` exports a default object `{ toNativeType, extractURLParameters }` — `main.ts`'s new named exports need to destructure these default exports, not just re-export a name that doesn't exist.
- `js-lib/src/trame.ts`'s `Trame` class already exposes `client`, `state`, `config`, `refs`, `connect()`, `trigger()`, `onClose()`, `onError()` exactly as this plan assumes; `state.watch(keys, fn)` (`js-lib/src/state.ts`) calls `fn` immediately with current values on subscribe, which `useSyncExternalStore` depends on for its synchronous initial snapshot.
- `js-lib/tests/helpers/fakeClient.ts` is a ready-made fake `vtkWSLinkClient` (`getState`, `updateState`, `trigger`, `subscribeToStateUpdate`, `subscribeToActions`, connect/disconnect/busy) — reuse this pattern (or the same helper via a relative import) for `react-app`'s own vitest suite rather than re-inventing a fake client.
- `tests/test_react.py` confirms the exact wire shapes this plan relies on: `{"js": ...}` leaves for `Bind`, `{"callback": {...}, "modifiers": [...]}` for `Callback` (with `trigger`/`args`/`kwargs` sub-keys when wrapping a Python callable), `{"tag": "ReactIf"/"ReactFor", "props": {...}, "children": [...]}` for structural nodes, and `{"slot": {"params": [...], "children": [...]}}` for `Slot`. It also confirms `key=` can itself be a `Bind` (`html.Li([...], key=react.Bind("todo"))` serializes to `"key": {"js": "todo"}`), validating §2's `computeNodeKey` needing to handle a `{js: ...}` leaf, not just plain scalars.
- `react-getting-started.md` and the `onChange=react.Callback("count = Number($event.target.value)")` examples confirm the DOM event is referenced as `$event` in author-facing JS expressions — §4 (`makeCallbackHandler`) binds the scope variable as `$event` accordingly.
- `widgets/core.py`'s `AbstractElement.__init__` dispatches `self._impl = _get_impl_class(self.server.client_type)(self, kwargs)`, and already has a `client_type == "react"` branch returning `react.HtmlElement` — so the Python side is fully wired up to produce trees for any widget once `self.server.client_type == "react"`; only the client bundle and `module/__init__.py`'s dispatch (§8) are missing.
- `widgets/trame.py`'s `Loading` (`_elem_name = "trame-loading"`, attr `message`) and `ServerTemplate` (`_elem_name = "trame-template"`, attrs `name`→`templateName`, `use_url`→`useUrl`, `url_key`→`urlKey`) both declare their attrs via `self._attr_names += [...]`, which `widgets/core.py`'s backward-compat aliasing routes to `self._impl.props` — i.e. `react.HtmlElement` (already implemented) picks these up automatically through the existing `props`/`SHARED_PROPS` mechanism; no Python-side change is needed for these two widgets, only client-side `TrameLoading`/`TrameTemplate` components registered under those exact tag strings (§6/§7).
- `noxfile.py`'s existing `VUE_APPS` dict and `_ensure_vue_apps_built` helper, and `pyproject.toml`'s `[tool.hatch.build] include` list, were read directly to confirm the exact edits described in §8 are additive (new dict entry / new glob line) rather than requiring restructuring.
