# Rethinking Text Interpolation for trame's React `client_type`

> **Status: design exploration.** Revisits
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md) section 3, which
> originally proposed reusing Vue's `{{ }}` mustache syntax and splitting it into
> DOM-shaped children at Python serialization time. This document asks whether
> that was actually the right call for a React `client_type`, or just an
> unexamined carry-over from the Vue path. **Scoped to `client_type="react"`
> only** — the Vue path keeps `{{ }}` exactly as-is; Vue's own runtime compiler
> is what makes that syntax work there, and nothing about it needs to change.

## 1. What does React itself do here?

Nothing special, and that's the point. JSX never introduced a text-templating
mini-language, because it never needed one — children are just a list, and a
list can already mix literal strings with expressions:

```jsx
<div>count = {count}</div>
<div>Reset count to {defaultValue} then double it to {2 * defaultValue}</div>
```

`{count}` isn't a string-embedded marker being parsed out of `"count = {count}"`
— it's a separate child in the JSX children array, sitting right next to the
literal string `"count = "`. There is no equivalent in React to Vue's `{{ }}`
because there's no problem left for it to solve once you can just write another
child.

This means trame's `{{ }}` convention isn't "the React way, spelled slightly
differently" — it's a Vue-specific solution (string templates, compiled at
runtime) applied to a design (the JSON tree) that doesn't actually have the
constraint that made `{{ }}` necessary in the first place.

## 2. Options considered

### (a) Keep `{{ }}`, split it in Python (status quo)

What `vue-vs-react-with-trame.md` section 3 already proposes: parse
`"count = {{ count }}"` with a regex at serialization time into
`["count = ", { "js": "count" }]`.

- Works, and was already designed. But it's stringly-typed (a typo inside the
  mustache, e.g. `{{ cuont }}`, is invisible to any tooling until it fails at
  runtime), needs an escaping story for literal `{{`/`}}` in real text, and
  requires a regex-based parser to exist and be maintained at all — solving a
  problem React's own data model doesn't actually have.

### (b) Python f-strings

Tempting at first glance — `f"count = {count}"` looks exactly like what we
want, and it's already native Python syntax with full IDE/lint support.

- **Doesn't work.** An f-string evaluates immediately, at the point the Python
  code runs, using whatever `count` is bound to *in Python* at that moment. It
  bakes in a snapshot value and produces a plain `str` — there's no way for it
  to stay bound to the *client-side* state key over time. Using an f-string
  here would silently produce a UI that never updates, which is worse than a
  syntax problem — it's a correctness trap. Rejected.

### (c) Single-brace `.format()`-style placeholders

A cosmetic variant of (a): `"count = {count}"`, parsed by trame instead of by
Python's own `str.format`.

- Doesn't address any of (a)'s actual problems — still a string convention
  trame has to parse, still no tooling support, still needs an escaping story.
  Changing the delimiter doesn't change the underlying philosophy mismatch.
  Rejected for the same reasons as (a).

### (d) Children are just a list; dynamic parts are a typed marker object

Mirror JSX directly: a literal string is a literal string, and a dynamic part
is its own explicit item in the children list — not a substring inside one.

```python
html.Div(["count = ", react.Bind("count")])
html.Div([
    "Reset count to ", react.Bind("default_value"),
    " then double it to ", react.Bind("double_default"),
])
```

Note the list/tuple wrapping: `AbstractElement.__init__` (`widgets/core.py`)
takes a single `children` argument — a plain value is treated as one child,
and a list/tuple is what lets you pass several. This isn't `*args`-style
variadic children; the whole sequence has to be handed over as one argument.

This is the recommendation. See below for why.

## 3. Why (d) fits better

- **No parser needed at all.** Python's own argument/list syntax already does
  the splitting `{{ }}` needed a regex for. There's nothing to write, maintain,
  or get subtly wrong with escaping.
- **No escaping problem.** A plain string child is *always* literal text.
  `html.Div("Use {{ this }} syntax literally")` just displays that text — no
  `v-pre`-style opt-out needed, because there was never any parsing to opt out
  of.
- **Typos become visible.** `react.Bind("cuont")` is a real Python value that
  can eventually be linted/checked against known state keys; a typo buried
  inside a mustache string cannot be, short of parsing every string children at
  lint time.
- **Reuses `react.Bind` as-is — no new class needed.** `react.Bind` already
  exists (`vue-vs-react-with-trame.md`, `react-scoped-slots.md`) for exactly
  "a value that should reactively reflect a state expression," currently used
  for prop values like `value=react.Bind("count", count=2)`. A child position
  and a prop-value position both bottom out in the same serialized leaf shape,
  `{ "js": "count" }` — so the same class does both jobs. This also resolves a
  real inconsistency the status quo had: props already used typed objects
  (`react.Bind`, `react.Callback`, `react.Slot`) to express dynamism, while
  children were still stuck on a stringly-typed convention borrowed from Vue.
  `react.Bind` in children brings the whole design onto one consistent idiom.

### Serialized shape: unchanged

This is a Python-authoring change, not a wire-format change — the JSON tree
still looks exactly like `vue-vs-react-with-trame.md` section 3 already
specified:

```json
{ "tag": "div", "children": ["count = ", { "js": "count" }] }
```

The only difference is *how* Python arrives at that array: previously, a
regex split one string apart; now, the caller already handed the widget an
already-split list, and each `react.Bind` instance serializes directly to its
`{ "js": ... }` leaf — nothing left to parse client-side or server-side.

## 4. Trade-off worth naming

Interleaving many small pieces reads a little more verbosely in Python than
one mustache-laden string for long, heavily-interpolated sentences:

```python
html.Div([
    "Reset count to ", react.Bind("default_value"),
    " then double it to ", react.Bind("double_default"),
    ", or leave it at ", react.Bind("count"),
])
```

vs. the single-string Vue equivalent:

```python
html.Div("Reset count to {{ default_value }} then double it to {{ double_default }}, or leave it at {{ count }}")
```

This is a real ergonomic cost for prose-heavy text, but it's the same
trade-off JSX itself already accepts for the same reason — and it's the
trade-off that buys typo-visibility and removes an entire parser from the
design.

## 5. Open questions

- Should there be a lighter-weight alias/shorthand for the extremely common
  single-binding case (`html.Div(["count = ", react.Bind("count")])`) to reduce
  friction versus the old one-liner, without reintroducing string parsing?
- Does this change anything about how `react.For`'s loop variable (`{{ item }}`
  today) gets referenced in children — presumably it becomes
  `react.Bind("item")` resolved against the loop's local scope, consistent with
  everything above, but worth confirming against `react-scoped-slots.md`'s
  scope-chain design.
