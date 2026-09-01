# Vue vs React `client_type` in trame: Syntax Exploration

> **Status: design exploration.** As of this writing, `trame-client` only implements
> `client_type = "vue2"` and `"vue3"` (see `src/trame_client/module/__init__.py` and
> `src/trame_client/widgets/core.py`). There is no `"react"` client type yet. This
> document explores what the Python-facing syntax and client-side architecture
> *could* look like if one were added, and where it necessarily has to diverge from
> the Vue implementation. It is meant to support planning, not to document shipped
> behavior.

## 1. How the Vue `client_type` actually works today

This part matters because it explains *why* a naive "just add a React renderer"
approach doesn't work.

`AbstractElement.html` (`src/trame_client/widgets/core.py`) doesn't build a DOM or a
virtual-DOM tree — it builds a **literal Vue template string**:

```python
html.Div("count = {{ count }}")
html.Input(type="range", min=0, max=10, step=1, v_model_number="count")
```

serializes to something like:

```html
<div>count = {{ count }}</div>
<input type="range" min="0" max="10" step="1" v-model.number="count" />
```

This string is shipped to the browser and registered as a dynamic Vue component
(see `vue3-app/src/components/TrameTemplate.js`), which Vue **compiles at runtime**
using its bundled template compiler. That's the load-bearing fact: Vue ships a
runtime template compiler, so arbitrary strings containing directives
(`v-if`, `v-for`, `v-model`, `v-bind`, `{{ mustache }}` interpolation) can be turned
into a working reactive render function *after* the page has already loaded, purely
from server-sent strings. State variables become `customRef`s (`toRef()` in
`TrameTemplate.js`) so any `{{ name }}` or `v-model="name"` in the string
automatically wires into the shared trame state store.

React has **no runtime JSX/template compiler** in its standard distribution. JSX is
normally compiled ahead-of-time (Babel/SWC) to `React.createElement(...)` calls.
There's no directive system (`v-if`, `v-for`, `v-model` are Vue-template concepts,
not HTML/React concepts) — conditionals and loops are just JavaScript. This is the
central design problem a `client_type = "react"` implementation has to solve.

## 2. The serializable widget tree strategy

Instead of a template-like string (the Vue approach), a React `client_type` emits
a **serializable widget tree (JSON)** that mirrors the real DOM: each node is a
`tag` + `props` + `children`. A small generic `<TrameNode>` React component walks
that tree at runtime and calls `React.createElement` directly — no compiler
needed at all. Conditionals, loops, and two-way binding become properties of the
tree/renderer rather than syntax embedded in a string.

This is a good idiomatic fit for React's data-driven mental model, and it's the
same pattern used by most "server-driven UI" systems, so the examples below build
on it throughout.

## 3. Syntax comparison

### Vue.js example

```python
from trame.app import TrameApp
from trame.widgets import html
from trame.ui.html import DivLayout
from trame.decorators import change

class VueImplementation(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="vue3")
        self._build_ui()

    @change("count")
    def update_count(count, **_):
        self.state.double = 2 * int(count)

    def reset(self, value=2):
        self.state.count = value
        
    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            html.Div("count = {{ count }}")
            html.Div("2 x count = {{ double }}")
            html.Input(
                type="range", min=0, max=10, step=1,
                v_model_number=("count", 2),
                v_on_dblclick_prevent="count = 2 * count"
            )
            html.Button(
                "Reset",
                click=self.reset,
            )
            html.Button(
                "Reset 4",
                click=(self.reset, "[4]", "{}"),
            )
```

### React example

```python
from trame.app import TrameApp
from trame.widgets import html
from trame.ui.html import DivLayout
from trame.decorators import change

class ReactImplementation(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")
        self._build_ui()

    @change("count")
    def update_count(count, **_):
        self.state.double = 2 * int(count)

    def reset(self, value=2):
        self.state.count = value
        
    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            html.Div("count = {{ count }}")
            html.Div("2 x count = {{ double }}")
            html.Input(
                type="range", min=0, max=10, step=1,
                value=react.Bind("count", count=2),
                onChange=react.Callback("count = Number(e.target.value)"),
                onDoubleClick=react.Callback("count = 2 * count", modifiers=["prevent"]),
            )
            html.Button(
                "Reset",
                onClick=react.Callback(self.reset)
            )
            html.Button(
                "Reset 4",
                onClick=react.Callback(self.reset, "[4]", "{}")
            )
```

Those examples will then update the template state variable with those values:

For vue

```html
<div>count = {{ count }}</div>
<div>2 x count = {{ double }}</div>
<input 
    type="range"
    min="0"
    max="10"
    step="1"
    v-model.number="count"
    v-on:dblclick.prevent="count = 2 * count"
/>
<button @click="trigger('trigger_1')">Reset</button>
<button @click="trigger('trigger_1', [4], {})">Reset 4</button>
```

For react

```json
[
  { "tag": "div", "children": ["count = ", { "js": "count" }] },
  { "tag": "div", "children": ["2 x count = ", { "js": "double" }] },
  {
    "tag": "input",
    "props": {
      "type": "range",
      "min": 0,
      "max": 10,
      "step": 1,
      "value": { "js": "count" },
      "onChange": { "callback": { "js": "count = Number(e.target.value)" } },
      "onDoubleClick": {
        "callback": { "js": "count = 2 * count" },
        "modifiers": ["prevent"]
      }
    }
  },
  {
    "tag": "button",
    "children": ["Reset"],
    "props": {
      "onClick": { "callback": { "trigger": "trigger_1" } }
    }
  },
  {
    "tag": "button",
    "children": ["Reset 4"],
    "props": {
      "onClick": {
        "callback": {
          "trigger": "trigger_1",
          "args": { "js": "[4]" },
          "kwargs": { "js": "{}" }
        }
      }
    }
  }
]
```

`react.Bind(js_expression, **state_defaults)` — the first, positional argument
is the JS expression to evaluate against the current scope; every keyword
argument sets a default on trame's shared state (`state.setdefault(key,
value)`, one call per kwarg), independent of what the expression itself
references. See `react-getting-started.md` section 4 for the full breakdown
and a multi-key example.

react.Callback is use to generate a JavaScript callback that will either evaluate a JavaScript function or make a call to a trame trigger function.


## 4. A concrete Python-facing API proposal: `react.If`, `react.For`, `react.Bind`

Rather than inventing a JSON-tree DSL from scratch (section 3), structural
directives can be modeled as **widgets** that reuse the same context-manager
pattern already used by `Template`/`VirtualNode` in `widgets/core.py` (pushing
onto `HTML_CTX` in `__enter__`/popping in `__exit__`). This keeps Python authoring
close to parity between `client_type="vue3"` and a future `client_type="react"`.

### `v-if` → `react.If`

```python
# internally "count > 5" will be wrapped with react.Bind("count > 5") as needed
with react.If(value="count > 5"):
    html.Div("Count is high")
```

vs. Vue:

```python
html.Div("Count is high", v_if="count > 5")
```

`react.If` isn't a real DOM tag — it's a structural marker. It wraps its children
and tells the client renderer "only mount this subtree while `value` is truthy,"
i.e. it moves the conditional from an *attribute* (Vue) to a *block* (React),
which matches how React actually expresses conditionals in JSX.

### `v-for` → `react.For`

```python
# react.Bind can be used or tagged internally for specific kwargs
with react.For(items="Object.keys(obj)", name="item"):
    html.Li("{{ item }}")
```

vs. Vue:

```python
html.Li("{{ item }}", v_for="item in Object.keys(obj)")
```

### `v-model` → `react.Bind` + `react.Callback`

```python
html.Input(
    value=react.Bind("count", count=2),
    onChange=react.Callback("count=Number(e.target.value)", modifiers=["prevent"])
)
```

vs. Vue:

```python
html.Input(v_model_number="count")
```

Vue's single `v-model` directive splits into two explicit pieces under React:
`react.Bind` supplies the controlled `value` (a JS expression — here just the
bare key `"count"` — serialized as the `{ "js": "count" }` leaf shown in
section 3, with `count=2` setting `state.setdefault("count", 2)` as a side
effect, independent of the expression itself), and `react.Callback` supplies
the `onChange` handler that writes back to state —
either a raw JS expression (as here) or a Python callable, optionally combined
with event `modifiers` (`prevent`, `stop`, ...) standing in for Vue's
`.prevent`/`.stop` modifiers. `react.Callback` isn't `v-model`-specific — it's
the same helper used for every other event prop (`onClick`, `onDoubleClick`,
...), so there's one unified mechanism for both directive-style two-way binding
and plain event wiring, rather than a dedicated `v-model` construct.

### Why this fits well

- Reuses the existing Python idiom (context managers for structure, kwargs for
  bindings) instead of introducing a parallel tree-building API just for React.
- Keeps the same "arbitrary JS expression string" escape hatch the Vue path
  already relies on (`v_if="count > 5"`, `v_bind_x="expr"` already flow through
  `translate_js_expression` in `widgets/core.py`) — nothing new at the Python
  level, only the client-side handling of that string changes.

### What it requires that doesn't exist yet

- **A client-side expression evaluator.** Under Vue, `v_if="count > 5"` works
  because Vue's compiler turns the string into real JS bound to the reactive
  scope. React ships no such compiler, so `react.If.value` and `react.For.items`
  would need trame's own small evaluator at runtime (e.g.
  `new Function(...stateKeys, 'return (' + expr + ')')(...stateValues)`) —
  effectively reimplementing in miniature what Vue's compiler currently does
  for free.
- **Mustache interpolation on non-state names.** `{{ item }}` inside `react.For`
  isn't a trame state key — it's a local loop variable introduced by
  `react.For(..., name="item")`. Since `{{ item }}` splits into the same
  `{ "js": "item" }` leaf described in section 3, this falls out for free as
  long as the runtime scope resolution checks the nearest enclosing `react.For`
  binding before falling back to global state — no separate mechanism needed,
  just a scope chain instead of a flat lookup.

## 5. What's structurally harder for React

- **Two-way binding (`v-model`)** has no first-class React equivalent — every
  instance has to be expanded into an explicit controlled `value`/`onChange` pair,
  which is more verbose per-widget than Vue's single directive.
- **Conditionals and loops** move from "syntax embedded in markup" (Vue) to "logic
  in the renderer / tree shape" (React) — there's no way to keep them as
  inline string directives without shipping a JSX compiler to the browser.
- **Arbitrary expressions** (e.g. `v-if="count > 5 && ready"`) are trivial for Vue's
  compiler to evaluate from a string, but a JSON-tree approach would need either a
  small expression-evaluator DSL or would have to push such logic to be computed
  server-side into a plain boolean state key before it reaches the client.

## 6. What's still missing for full parity

Sections 1-5 cover the **core primitive layer**: text binding, events/triggers,
and `v-if`/`v-for`/`v-model` equivalents. That layer is basically fully specified
at this point. But "the same way we use trame with Vue today" pulls in a lot more
than raw `html.Div`/`Input` usage, and none of the following is addressed yet —
ranked roughly by impact:

1. **The widget ecosystem — by far the biggest gap.** Most real trame apps aren't
   built from `html.*` primitives; they're built from trame-vuetify, trame-vtk,
   trame-plotly, trame-matplotlib, etc. Each of those ships an actual Vue
   component implementation today. Porting the core mechanism described in
   sections 1-5 doesn't get you a single `<v-btn>` or `<vtk-view>` in React — this
   dwarfs the work discussed so far.

2. **Custom-tag resolution.** The JSON tree assumes `tag` → `React.createElement(tag, ...)`,
   i.e. a literal DOM tag. But `<v-btn>`/`<vtk-view>` aren't DOM tags — Vue
   resolves them through a global component registry tied to the asset-loading
   system in `src/trame_client/module/__init__.py`. There's no documented React
   counterpart: a registry mapping widget names to actual React component
   references that `TrameNode` would need to check before falling back to
   `createElement(tag, ...)`.

3. **No client app shell exists yet.** There's no `react-app/` equivalent of
   `vue3-app/`. All the life-cycle glue currently living in
   `vue3-app/src/components/` (`TrameSizeObserver`, `TrameGetter`, `TrameScript`,
   `TrameExec`, `TrameReconnect`, `TrameClientStateChange`,
   `TrameLifeCycleMonitor`, ...) is built on Vue's `onMounted`/`onUpdated` hooks
   and needs a from-scratch React reimplementation using `useEffect`.

4. **Refs.** `AbstractElement.html` already special-cases `ref=` for vue3
   (patches it to `trame.refs[name] = el`), used by apps to imperatively reach
   into a rendered component. The JSON-tree schema has no `"ref"` field or
   callback-ref mechanism yet.

5. **Scoped slots — the hardest semantic gap.** Widget libraries lean on Vue's
   scoped slots (a child component, like a data table, handing per-row data back
   into the slot template it's given). `react.If`/`react.For`/`react.Bind` don't
   generalize to "a widget hands you extra scope at render time" — that's a
   fundamentally different mechanism than binding against known state keys,
   closer to React's "render props" pattern, and nothing designed so far covers
   it.

6. **The expression evaluator is still aspirational.** Section 4 says `react.If`/
   `react.For` "would need" one, but building it safely — sandboxing
   `new Function`, caching per unique expression string instead of re-parsing on
   every render, deciding the supported grammar — is real, unstarted work. Vue's
   compiler already solved this; a hand-rolled version doesn't inherit that
   hardening for free.

7. **Fine-grained reactivity/perf.** Vue's `customRef` gives cheap per-key
   updates (see `toRef()` in `TrameTemplate.js`). A React renderer walking a
   JSON tree needs each `TrameNode` to subscribe narrowly to only the state keys
   its own subtree binds, or state changes will over-render the whole tree —
   not addressed anywhere in this design yet.

**Recommendation:** treat items 1 and 5 as the real litmus test for this design.
Prototype one non-trivial third-party widget end-to-end — something with a
scoped slot, like a table row template — before investing further design time in
the core mechanism. That's where the JSON-tree schema is least proven, and if it
doesn't hold up there, it changes the schema everything else in this document
depends on.
