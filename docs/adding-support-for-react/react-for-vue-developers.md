# React for trame Developers Coming from Vue

> **Status: design exploration — nothing here is implemented yet.** This is a
> practical, syntax-first companion for people who already build trame apps
> with `client_type="vue3"` and want the direct translation to
> `client_type="react"`. If you have no Vue background, use
> [`react-getting-started.md`](./react-getting-started.md) instead — it
> teaches the React side on its own terms, with no Vue references at all. For
> the reverse mapping (React → Vue), see
> [`vue-for-react-developers.md`](./vue-for-react-developers.md) — note that
> one describes real, already-shipped behavior, since `client_type="vue3"`
> exists today and `client_type="react"` here does not. For the design
> rationale behind *why* each translation looks the way it does, see
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md).

## Dynamic text

Vue's `{{ }}` mustache syntax becomes its own item in the children list:

```python
# Vue
html.Div("count = {{ count }}")

# React
html.Div(["count = ", react.Bind("count")])
```

`html.Div` takes one `children` argument, not variadic `*args` — multiple
children (literal text and bindings both) go in a single list/tuple.

📖 [`react-text-interpolation.md`](./react-text-interpolation.md)

## Bound props and two-way binding

Vue's `v-model` (and its modifiers) is a single directive that implies both a
controlled value and a change handler. React has no equivalent directive, so
it splits into two explicit pieces:

```python
# Vue
html.Input(type="range", min=0, max=10, step=1, v_model_number=("count", 2))

# React
html.Input(
    type="range", min=0, max=10, step=1,
    value=react.Bind("count", count=2),
    onChange=react.Callback("count = Number($event.target.value)"),
)
```

📖 [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 4

## Events and triggers

```python
# Vue
html.Button("Reset", click=self.reset)
html.Button("Reset to 4", click=(self.reset, "[4]", "{}"))
html.Input(v_on_dblclick_prevent="count = 2 * count")

# React
html.Button("Reset", onClick=react.Callback(self.reset))
html.Button("Reset to 4", onClick=react.Callback(self.reset, "[4]", "{}"))
html.Input(
    onDoubleClick=react.Callback("count = 2 * count", modifiers=["prevent"])
)
```

Vue's `v_on_<event>_<modifier>=` naming convention becomes an explicit
`modifiers=[...]` list on `react.Callback`.

📖 [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 3

## Conditional rendering

Vue's `v_if=` is a per-element attribute; React expresses conditionals
structurally, as a wrapping block:

```python
# Vue
html.Div("Count is high", v_if="count > 5")

# React
with react.If(value="count > 5"):
    html.Div("Count is high")
```

📖 [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 4

## List rendering

```python
# Vue
with html.Ul():
    html.Li("{{ item.name }}", v_for="item in items", key="item.id")

# React
with html.Ul():
    with react.For(items="items", name="item"):
        html.Li(react.Bind("item.name"), key=react.Bind("item.id"))
```

Vue's implicit list diffing still requires a `key=`, same as React — the
difference is `v_for=` folds the loop into the element's own attributes,
while `react.For` wraps the templated child as its own block.

📖 [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 4

## Scoped slots

```python
# Vue
with VDataTable(items=("items", data)):
    with Template(v_slot_item_name="{ item }"):
        html.Strong("{{ item.name }}")

# React
with react.Slot(params=["item"]) as render_item_name:
    html.Strong([react.Bind("item.name")])

VDataTable(items=react.Bind("items"), renderItemName=render_item_name)
```

Vue's `v_slot_<name>="{ destructure }"` string becomes an explicit
`react.Slot(params=[...])` block, defined outside the widget's own `with`
block and passed in as an ordinary prop.

📖 [`react-scoped-slots.md`](./react-scoped-slots.md)

## Refs and imperative calls

No translation needed — this part of the API is identical for both
`client_type`s:

```python
html.Input(ref="my_input")
self.server.js_call("my_input", "focus")
```

📖 [`react-refs.md`](./react-refs.md)

## Cheat sheet

| Vue | React |
| --- | --- |
| `"{{ count }}"` in children | `react.Bind("count")` as its own child in a list |
| `v_if="expr"` | `with react.If(value="expr"):` |
| `v_for="item in items"` | `with react.For(items="items", name="item"):` |
| `v_model_number="count"` | `value=react.Bind("count")`, `onChange=react.Callback("count = Number($event.target.value)")` |
| `@click="trigger('fn')"` / `click=self.fn` | `onClick=react.Callback(self.fn)` |
| `click=(self.fn, "[4]", "{}")` | `onClick=react.Callback(self.fn, "[4]", "{}")` |
| `v_on_dblclick_prevent="expr"` | `onDoubleClick=react.Callback("expr", modifiers=["prevent"])` |
| `Template(v_slot_item_name="{ item }")` | `with react.Slot(params=["item"]) as x: ...` passed as `some_prop=x` |
| `ref="name"` | `ref="name"` (unchanged) |
| `self.server.js_call("name", "method", *args)` | unchanged |
