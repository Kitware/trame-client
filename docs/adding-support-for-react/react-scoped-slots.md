# Scoped Slots: Vue → React Translation for trame

> **Status: design exploration.** Follow-on from
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md), section 6, item 5
> ("the hardest semantic gap"). Nothing described here exists in the codebase yet.
> Scoped out for now: this only covers the mechanism itself, not any specific
> widget library port (see the parent doc's note on deferring the widget
> ecosystem).

## 1. What a Vue scoped slot actually is

A normal Vue slot just projects markup from parent to child — the parent decides
*what* renders, the child decides *where*. A **scoped** slot goes one step
further: the child also hands data back to that markup, computed from something
only the child knows about (its internal iteration, its internal state, ...).

Vuetify's data table is the canonical example. Internally, for every row it
renders, it exposes a slot together with the row's data:

```html
<!-- (conceptual) inside VDataTable's own template -->
<slot name="item.name" :item="item">{{ item.name }}</slot>
```

The consumer supplies the slot content using `trame`'s existing `Template`
widget (`src/trame_client/widgets/core.py`), which maps a `v_slot_item_name=`
kwarg to Vue's `v-slot:item.name="{ item }"` syntax:

```python
with VDataTable(items=("items", data)):
    with Template(v_slot_item_name="{ item }"):
        html.Strong("{{ item.name }}")
```

The critical detail: `item` is **not** a trame state key. It's a local variable
that only exists while `VDataTable` is rendering that particular row, and a
different `item` value is injected on every iteration. Python never sees or
needs to understand `item` — the whole `"{ item }"` destructuring string is just
forwarded as-is for Vue's compiler to interpret.

## 2. Why nothing already designed covers this

[`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md) already has a
concept of "extra local scope" — `react.For(items=..., name="item")` introduces
`item` as a loop variable, resolved via a scope chain instead of flat global
state (section 4). Scoped slots need the *same underlying mechanism*, but
**triggered by a different party**:

| | Who owns the loop/iteration | Who introduces the scope variable |
| --- | --- | --- |
| `react.For` | trame's own generic renderer | trame's own generic renderer |
| Scoped slot | An arbitrary third-party widget (`VDataTable`) | The widget's own React implementation, at a time and with values only it knows |

`react.For` can extend scope itself because it *is* the loop. A scoped slot's
content has to be handed to the widget as something the widget can invoke
*whenever it wants, with whatever data it wants* — which is a fundamentally
different shape of problem: not "loop over a known array," but "expose an
extension point that some other component controls."

## 3. The React idiom this maps to: render props

React has no built-in "slot" concept, but it has had a well-established pattern
for exactly this problem since long before hooks existed: **render props** (a
prop whose value is a function, invoked by the component that owns it, with
that component's own data as arguments).

```jsx
// Hand-written React, for comparison — not what Python would generate
<DataTable
  items={items}
  renderItemName={(item) => <strong>{item.name}</strong>}
/>
```

```jsx
function DataTable({ items, renderItemName }) {
  return (
    <table>
      <tbody>
        {items.map((item) => (
          <tr key={item.id}>
            <td>{renderItemName(item)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

`DataTable` calls `renderItemName(item)` itself, once per row, exactly when it
knows what `item` is — that call site is the React equivalent of Vue's
`<slot name="item.name" :item="item" />`.

The catch for trame: **a Python process cannot ship a real JavaScript closure.**
Vue sidesteps this because its compiler turns the `Template`/`v-slot` markup
into an actual function at runtime, client-side, from a string. React has no
such compiler. So the render-prop function has to be *synthesized on the
client* from data, not shipped as a value.

## 4. Proposed design: `react.Slot` + a generic slot renderer

### Python-facing API

A new structural widget, `react.Slot`, analogous to `Template`/`v_slot` but
explicit about the parameter names the slot will receive:

```python
with react.Slot(params=["item"]) as renderItemName:
    html.Strong("{{ item.name }}")
VDataTable(items=react.Bind("items"), renderItemName=renderItemName)
```

`params=["item"]` is the React-side equivalent of Vue's `"{ item }"`
destructuring string — except spelled out explicitly, since there's no compiler
available client-side to parse a destructuring pattern out of an opaque string.

The object bound by `as renderItemName` is the `react.Slot` instance itself
(`__enter__` returning `self`, same as `VirtualNode`/`AbstractElement` already
do) — it's recognized by type during prop serialization exactly like
`react.Bind`/`react.Callback` instances already are. Because it's defined outside
`VDataTable`'s own `with` block, `react.Slot` needs `connect_parent=False`
(already a supported `AbstractElement.__init__` option) so it isn't *also*
auto-attached as a child of whatever layout context happens to be open at the
point it's defined — its only attachment point is the `renderItemName=` prop it
gets explicitly passed to.

### Serialized shape

A `react.Slot` value serializes like any other special prop value — no separate
`slots` map, no name-string namespace. It's just one more recognized shape a
prop value can take, alongside `{ "js": ... }` and `{ "callback": ... }`:

```json
{
  "tag": "VDataTable",
  "props": {
    "items": { "js": "items" },
    "renderItemName": {
      "slot": {
        "params": ["item"],
        "children": [
          { "tag": "strong", "children": [{ "js": "item.name" }] }
        ]
      }
    }
  }
}
```

### Client-side: turning slot data into a real render prop

This is the missing generic piece — but it plugs into machinery that already
has to exist anyway. `TrameNode`'s generic prop-resolution pass already turns a
`{ "js": ... }` value into a plain value and a `{ "callback": ... }` value into
a plain function *before* a widget's `props` are ever assembled (section 3 of
the parent doc). `{ "slot": ... }` is a third case handled the same way:

```jsx
function resolveProp(value, scope) {
  if (value?.js !== undefined) return evaluate(value.js, scope);
  if (value?.callback !== undefined) return makeCallback(value.callback, scope);
  if (value?.slot !== undefined) {
    const { params, children } = value.slot;
    return (scopeValues) => (
      <TrameNode
        nodes={children}
        // extend the active scope chain with the widget-supplied values,
        // keyed by the declared `params` - the same scope-chain mechanism
        // react.For already needs for its loop variable
        scope={extendScope(scope, params, Object.values(scopeValues))}
      />
    );
  }
  return value;
}
```

Because resolution happens generically before the widget ever sees its props,
`VDataTable`'s own React implementation needs **no special-casing at all** —
`renderItemName` just arrives as an ordinary callable, indistinguishable from a
render prop someone wrote by hand:

```jsx
function VDataTable({ items, renderItemName }) {
  return (
    <table>
      <tbody>
        {items.map((item) => (
          <tr key={item.id}>
            <td>
              {renderItemName ? renderItemName({ item }) : item.name}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

This is a further point in favor of `renderItemName=` being a plain prop rather
than a separately-namespaced `slots` value: the widget author writes the exact
same code they'd write for hand-authored React, with zero trame-specific
plumbing visible inside the component itself.

## 5. Summary

- Vue scoped slot = "child hands data to markup the parent supplied."
- React equivalent = render props: a function prop, called by the child, with
  the child's own data as arguments.
- trame can't ship a real function from Python, so `react.Slot` ships **data**
  (`{ params, children }`) as the value of an ordinary prop, and the same
  generic prop-resolution pass that already turns `{ "js": ... }` into a value
  and `{ "callback": ... }` into a function turns `{ "slot": ... }` into a
  callable — no separate `slots` namespace, and no special-casing required
  inside the widget's own React implementation.
- This reuses the scope-chain concept `react.For` already needs — the only new
  idea is that the scope extension can be triggered by an arbitrary widget's own
  render logic, not just trame's built-in loop construct.
- `react.Slot` itself is not a new mechanism so much as `VirtualNode`
  (`widgets/core.py`) applied to a new attachment point: capture children now,
  hand off a reference, attach it elsewhere (as a prop value instead of as
  layout content).

## 6. Open questions

- **Multiple/renamed params.** `params=["item", "index"]` composes naturally
  with the scheme above, but nested scoped slots (a slot inside a slot, each
  introducing its own variables) need the scope chain to nest correctly rather
  than flatten — not yet worked out.
- **Default slot content.** Vue's `<slot>...</slot>` can have fallback content
  when the parent doesn't provide that slot (`item.name` falling back to
  `{{ item.name }}` in the example in section 1). The design above has no
  fallback path yet — if `renderItemName` simply isn't passed, the prop is
  `undefined`, pushing the fallback-rendering responsibility onto each widget
  author individually (as shown in the `VDataTable` example) rather than
  providing it for free.
- **Unnamed/default slot.** Most widgets also have an unscoped default slot
  (children with no `v-slot:` at all). That's just `props.children` in React —
  no new mechanism needed — but it's worth stating explicitly so `react.Slot`
  doesn't get reached for the common case where a plain scope-free slot would
  do.
- **Freshly-minted functions on every render.** Because `resolveProp` builds a
  new closure for `{ "slot": ... }` (and `{ "callback": ... }`) each time it
  runs, `renderItemName` is a new function identity on every re-render unless
  the resolution pass memoizes per-node — the same fine-grained-reactivity
  concern already flagged in the parent doc (section 6, item 7), just visible
  here as a concrete case: an unmemoized render prop can defeat `React.memo` on
  whatever the widget renders with it.
