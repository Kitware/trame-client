# trame react client

Native React client for trame (`client_type="react"`). Renders the JSON
component tree produced by `trame_client/utils/react.py` with
`React.createElement` — no Vue, no iframe.

## Build the web client

```bash
npm install
npm run build   # outputs to ../src/trame_client/module/react-www
```

## Develop

```bash
npm run test    # vitest renderer/unit tests
npm run lint    # eslint + prettier
npm run debug   # build with sourcemaps
```

## Architecture

- `src/renderer/` - JSON tree -> React elements (expression evaluation against
  the trame shared state, `r_*` structural directives, scoped slots)
- `src/registry.js` - tag -> React component map; widget libraries register
  through `plugin.install(registry)` (declared via the `react_use` module key)
- `src/components/` - built-in trame components (TrameApp, TrameTemplate,
  TrameGetter, ...)
- `src/core/` - framework-agnostic wslink client, shared state mirror and
  attachment decorators (shared lineage with vue2-app/vue3-app)

Widget library bundles must build with `react`/`react-dom` as externals; the
client exposes the page's single React instance as `window.React` /
`window.ReactDOM`.
