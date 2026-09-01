# Vue.js vs React: High-Level Comparison

## Templating Philosophy

- **Vue**: HTML-based templates with directives (`v-if`, `v-for`, `v-bind`). Looks close to plain HTML/CSS/JS, separated into `.vue` single-file components (template/script/style blocks). Lower barrier for people coming from traditional web dev.
- **React**: JSX — HTML-like syntax embedded directly in JavaScript. Everything is "just JS," so logic and markup live together. Steeper initial learning curve (mixing markup in JS feels odd at first) but more expressive once you're used to it.

## Reactivity Model

- **Vue**: Reactivity is built into the framework via a proxy-based system (`ref`/`reactive`). You mutate data and the view updates automatically — closer to a "magic" data-binding feel.
- **React**: Explicit state via hooks (`useState`, `useEffect`). Nothing is reactive by default — you must call `setState` to trigger re-renders, and re-renders re-run the whole function component. More explicit/functional mental model, but more foot-guns around stale closures and dependency arrays.

## Component Style

- **Vue**: Options API (older, more structured/beginner-friendly) or Composition API (newer, hooks-like, more flexible). Two ways to write components can be a source of fragmentation in a codebase.
- **React**: Function components + hooks is now the single standard way. More consistency across the ecosystem, but hooks rules (no conditional hooks, dependency arrays) trip up newcomers.

## Ecosystem & Tooling

- **Vue**: More "batteries included" — Vue Router, Pinia/Vuex, and build tooling are official, curated, and integrate tightly.
- **React**: More "bring your own" — routing, state management, and even data fetching are third-party choices (React Router, Redux/Zustand/Jotai, React Query). More flexibility, more decision fatigue.

## Learning Curve & Adoption

- **Vue**: Generally considered easier to pick up initially, great docs, gentle progression.
- **React**: Larger job market, ecosystem, and community; more transferable skill (concepts carry to React Native, Next.js, etc.).

## Performance

- Both are comparably fast for most apps. Vue's fine-grained reactivity can avoid unnecessary re-renders more automatically; React relies on the developer (or compiler tooling like the React Compiler) to avoid wasted re-renders.

## Code Example: Props, Events, and Directives Side-by-Side

The example below is the same small component (a labeled counter with a toggle and a filtered list) written both ways, to show how Vue directives map onto plain JS/JSX patterns in React.

### Vue (Composition API, `<script setup>`)

```vue
<script setup>
import { ref, computed } from 'vue'

// --- props ---
const props = defineProps({
  items: { type: Array, required: true },
})

// --- events (emits) ---
const emit = defineEmits(['count-changed'])

const count = ref(0)
const showDetails = ref(false)
const filter = ref('')

function increment() {
  count.value++
  emit('count-changed', count.value)
}

const filteredItems = computed(() =>
  props.items.filter((item) => item.includes(filter.value))
)
</script>

<template>
  <!-- v-model: two-way binding on the input -->
  <input v-model="filter" placeholder="Filter items..." />

  <button @click="increment">Count: {{ count }}</button>

  <!-- v-if: conditional rendering -->
  <p v-if="showDetails">Details are visible</p>
  <button @click="showDetails = !showDetails">Toggle details</button>

  <!-- v-for: list rendering -->
  <ul>
    <li v-for="item in filteredItems" :key="item">{{ item }}</li>
  </ul>
</template>
```

### React (function component + hooks)

```jsx
import { useState, useMemo } from 'react';

// --- props: plain function arguments (destructured object) ---
// --- events: passed in as a callback prop, e.g. onCountChanged ---
function Counter({ items, onCountChanged }) {
  const [count, setCount] = useState(0);
  const [showDetails, setShowDetails] = useState(false);
  const [filter, setFilter] = useState('');

  function increment() {
    const next = count + 1;
    setCount(next);
    onCountChanged?.(next); // calling the callback prop == emitting an event
  }

  const filteredItems = useMemo(
    () => items.filter((item) => item.includes(filter)),
    [items, filter]
  );

  return (
    <>
      {/* v-model equivalent: controlled input (value + onChange) */}
      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="Filter items..."
      />

      <button onClick={increment}>Count: {count}</button>

      {/* v-if equivalent: JS conditional (&&, ternary, or early return) */}
      {showDetails && <p>Details are visible</p>}
      <button onClick={() => setShowDetails(!showDetails)}>
        Toggle details
      </button>

      {/* v-for equivalent: Array.prototype.map with a key prop */}
      <ul>
        {filteredItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );
}

// Parent usage — passing a prop and listening to the "event"
<Counter items={myItems} onCountChanged={(n) => console.log('count is', n)} />
```

### Key takeaways from the example

| Concept | Vue | React |
| --- | --- | --- |
| Props | `defineProps` | Function arguments (destructured object) |
| Events | `defineEmits` + `emit('name', payload)` | A callback prop (e.g. `onCountChanged`) passed down and called directly |
| `v-if` | Directive on the element | Plain JS: `&&`, ternary, or early `return null` |
| `v-for` | Directive with `:key` | `array.map()` returning JSX, with a `key` prop |
| `v-model` | Directive providing automatic two-way binding | Manual "controlled component": `value` + `onChange` |
| State updates | Mutate `ref`/`reactive` directly | Must call the setter function (`setCount`), never mutate directly |

The overarching pattern: Vue directives are declarative shorthand baked into the template compiler, while React expresses the same ideas as ordinary JavaScript expressions inside JSX — nothing "magic," but more boilerplate for things like two-way binding.
