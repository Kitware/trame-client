# Vue for trame Developers Coming from React

> **Status: this describes real, already-shipped behavior.** Unlike the
> `react.*` companion docs (which are design exploration for a `client_type`
> that doesn't exist yet), `client_type="vue3"` is real and has been trame's
> primary client for a long time (`src/trame_client/widgets/core.py`). This
> guide is a practical mapping from React concepts you already know to the
> Vue-based syntax trame actually uses today — useful if you're a React
> developer picking up an existing trame + Vue codebase, or evaluating trame
> for the first time with a React background.
>
> If you'd rather trame worked the other way — React syntax instead of Vue —
> see [`react-getting-started.md`](./react-getting-started.md) (a proposed,
> not-yet-built `client_type="react"`). For the reverse mapping (Vue → React),
> see [`react-for-vue-developers.md`](./react-for-vue-developers.md). For the
> design rationale comparing the two approaches in depth, see
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md).

## Displaying a value that changes over time

In JSX, a dynamic value is just an expression in curly braces, sitting next to
literal text as another child. trame's Vue path uses mustache interpolation
instead — a `{{ expr }}` marker embedded directly inside a string:

```jsx
// React (conceptually)
<div>count = {count}</div>
```

```python
# trame + Vue
html.Div("count = {{ count }}")
```

Unlike JSX, the expression lives *inside* the string rather than as a separate
child — trame's Vue path parses `{{ }}` out of whatever string children you
pass, so `"count = {{ count }}"` is a single argument, not a list.

## Binding a value to a prop / controlled input

In React, a controlled input is always two explicit props: `value` and
`onChange`. Vue's `v-model` directive bundles both into one — trame exposes it
as a single kwarg, with an optional default via tuple:

```jsx
// React (conceptually)
<input
  type="range" min={0} max={10} step={1}
  value={count}
  onChange={(e) => setCount(Number(e.target.value))}
/>
```

```python
# trame + Vue
html.Input(
    type="range", min=0, max=10, step=1,
    v_model_number=("count", 2),  # ("state key", default value)
)
```

You don't write the change handler yourself — `v_model_number` (the `.number`
modifier casts the input's string value to a number) wires the input's value
both ways automatically. Other modifiers exist too: `v_model_lazy` (update on
`change` instead of every keystroke), `v_model_trim`.

## Handling events and calling Python

```jsx
// React (conceptually)
<button onClick={() => reset()}>Reset</button>
<button onClick={() => reset(4)}>Reset to 4</button>
<input onDoubleClick={(e) => { e.preventDefault(); setCount(2 * count); }} />
```

```python
# trame + Vue
html.Button("Reset", click=self.reset)
html.Button("Reset to 4", click=(self.reset, "[4]", "{}"))
html.Input(v_on_dblclick_prevent="count = 2 * count")
```

A bare Python callable (`click=self.reset`) becomes a server round-trip
(`trigger(...)` under the hood) with no arguments. A `(callable, args_js,
kwargs_js)` tuple passes arguments along with that trip. Event modifiers
(React's manual `e.preventDefault()`, `e.stopPropagation()`, ...) become a
suffix on the kwarg name itself: `v_on_<event>_<modifier>`.

## Rendering content conditionally

In JSX, conditionals are just JavaScript (`&&`, a ternary, or an early
return). Vue expresses them as a template attribute instead:

```jsx
// React (conceptually)
{count > 5 && <div>Count is high</div>}
```

```python
# trame + Vue
html.Div("Count is high", v_if="count > 5")
```

`v_if` takes a JS-ish expression string, evaluated against trame state by
Vue's own template compiler — there's no need to compute the boolean in Python
first, though you certainly can if the condition gets complex.

## Rendering a list of items

```jsx
// React (conceptually)
<ul>
  {items.map((item) => (
    <li key={item.id}>{item.name}</li>
  ))}
</ul>
```

```python
# trame + Vue
with html.Ul():
    html.Li("{{ item.name }}", v_for="item in items", key="item.id")
```

Same requirement as React — list items need a stable, unique `key` — but
instead of `Array.prototype.map` in your own code, the iteration itself is
declared as a `v_for="item in items"` attribute, and `item` becomes available
inside that element's children/attributes as if it were state.

## Render props / scoped content

React's answer to "let a child component hand data back into content the
caller provides" is a render prop — a function passed as a prop, called by
the child with its own data. Vue's answer is a **scoped slot**:

```jsx
// React (conceptually)
<DataTable
  items={items}
  renderItemName={(item) => <strong>{item.name}</strong>}
/>
```

```python
# trame + Vue
with VDataTable(items=("items", data)):
    with Template(v_slot_item_name="{ item }"):
        html.Strong("{{ item.name }}")
```

`Template(v_slot_item_name="{ item }")` is the Vue equivalent of the render
prop's function signature — `"{ item }"` is a destructuring pattern Vue's
compiler parses out of the string, introducing `item` as a local variable
available only inside that `Template` block, supplied by `VDataTable` itself
(not global state). This only works for widgets that have registered
`"item.<name>"` as a known scoped-slot name — the same way a React component
has to define which render props it accepts.

## Refs and imperative calls

Same idea as React's `useRef`/`useImperativeHandle`, and the same syntax
regardless of client type:

```jsx
// React (conceptually)
const inputRef = useRef(null);
<input ref={inputRef} />;
inputRef.current.focus();
```

```python
# trame + Vue (also identical for client_type="react")
html.Input(ref="my_input")
self.server.js_call("my_input", "focus")
```

`ref="name"` registers the element (or component instance) under that name;
`server.js_call(name, method, *args)` calls a method on whatever's registered
there.

## Cheat sheet

| React (conceptually) | trame + Vue |
| --- | --- |
| `{count}` as a child | `"{{ count }}"` embedded in a string child |
| `value={x} onChange={...}` | `v_model_number=("x", default)` |
| `onClick={() => fn()}` | `click=self.fn` |
| `onClick={() => fn(4)}` | `click=(self.fn, "[4]", "{}")` |
| `onDoubleClick={(e) => { e.preventDefault(); ... }}` | `v_on_dblclick_prevent="..."` |
| `{cond && <div>...</div>}` | `html.Div(..., v_if="cond")` |
| `items.map((item) => <li key={item.id}>...)` | `html.Li(..., v_for="item in items", key="item.id")` |
| render prop (`renderItemName={(item) => ...}`) | `Template(v_slot_item_name="{ item }")` |
| `useRef` / `useImperativeHandle` | `ref="name"` + `self.server.js_call("name", "method", *args)` |
