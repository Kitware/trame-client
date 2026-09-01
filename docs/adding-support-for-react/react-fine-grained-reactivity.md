# Fine-Grained Reactivity for trame's React `client_type`

> **Status: design exploration, just getting started.** Follow-on from
> [`vue-vs-react-with-trame.md`](./vue-vs-react-with-trame.md) (section 6, item 7)
> and [`react-scoped-slots.md`](./react-scoped-slots.md) (section 6, "Freshly-minted
> functions on every render"). Nothing here is decided yet — this is a working
> comparison to reason from, not a conclusion.

## 1. The problem

Vue's `client_type` gets fine-grained reactivity for free. `TrameTemplate.js`
wraps every trame state key in its own `customRef` (`toRef()`), so a binding
like `{{ count }}` only triggers a re-render of the exact spot in the template
that reads `count` — nothing else re-evaluates when `count` changes.

The React JSON-tree design (`vue-vs-react-with-trame.md`, section 2) has no such
guarantee by construction: `TrameNode` walks a plain JSON tree and calls
`state.get(key)` wherever a `{ "js": ... }` leaf needs a value. Unless something
scopes *which* component re-renders on *which* state key changing, any state
update risks re-rendering the whole tree — and the scoped-slots design compounds
this, since `resolveProp` mints a fresh render-prop closure on every render
unless the underlying state primitive itself is fine-grained enough to avoid
re-invoking components that don't need it.

So the real question isn't just "what store do we use" — it's "what store lets
a generic, dynamically-shaped `TrameNode` component subscribe to *exactly* the
state keys its own subtree binds, with no upfront knowledge of what those keys
are, since the tree comes from Python and can be anything."

## 2. Candidate libraries

| Library | Model | Fine-grained by default? | Notes |
| --- | --- | --- | --- |
| **Redux** (+ Redux Toolkit) | Single store, reducers/actions, selectors | No — needs manual selector + memoization (`reselect`) discipline | Still common in large/legacy codebases; heavier boilerplate than the alternatives below; no longer the default choice for new projects |
| **Zustand** | Single store (or several), plain functions to read/set | Opt-in via selectors — `useStore(s => s.count)` re-renders only if the selected value changes | The closest thing to "the mainstream default" today; very low boilerplate; fine-graininess is something *you* write per usage, not automatic |
| **Jotai** | Atomic — one `atom` per piece of state | Yes, per-atom, by construction | `useAtom(atom)` subscribes to exactly that atom; maps naturally onto trame state since it's already a flat dict of named keys — one atom per key |
| **Valtio** | Proxy-based — mutate a plain object directly, subscribe via `useSnapshot` | Yes, per-key-actually-read, by construction | Structurally the closest analog to Vue's own reactivity system (which is also proxy-based) — the same mental model trame's Vue path already exploits |
| **Recoil** | Atomic, same idea as Jotai | Yes, per-atom | Meta-authored; largely superseded by Jotai in new adoption; mentioned for completeness |

## 3. Why this matters more than usual here

In a normal React app, you know your component tree at build time, so you can
hand-write `useAtom(countAtom)` or `useStore(s => s.count)` exactly where
needed. trame's tree is **dynamic and server-driven** — `TrameNode` doesn't
know in advance which state keys a given JSON subtree will reference; it finds
out by walking `{ "js": "..." }` leaves at render time. Whatever store trame
picks has to support **subscribing to a key computed at runtime**, not just a
key known at author time. That's a real constraint: Zustand's typical selector
usage assumes you write `s => s.count` in source code; Jotai's `atom` family
pattern (`atomFamily(key => ...)`) is built for exactly this "atom per
dynamically-named key" case; Valtio's proxy just reacts to whatever properties
were actually read on a given render, so runtime-computed key names fall out
for free.

## 4. Open questions to work through next

- Does `atomFamily` (Jotai) or a Valtio proxy keyed by state name end up
  simpler to wire into the existing `trame.state.get/set` wire protocol
  (`_event_value_processing` in `widgets/core.py`, and the `toRef()` pattern in
  `TrameTemplate.js`) that both `client_type`s share underneath?
- How does whichever store is picked interact with `react.For`'s per-iteration
  local scope and `react.Slot`'s widget-supplied scope (`react-scoped-slots.md`)
  — those aren't global state keys at all, so they sit outside whatever
  store manages the `trame.state` proxy.
- What does list re-rendering look like under `react.For` for a large array —
  does the chosen store help avoid re-rendering every row when only one row's
  backing data changes, or is that a separate problem the store doesn't solve?
