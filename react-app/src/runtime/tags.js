// Flat tag -> component registry. Never imports from `components/` (that
// would create an import cycle with TrameNode.jsx, which imports this module
// to resolve tags) - callers register their own components via registerTag()
// at module load time instead (see components/TrameApp.jsx).
const registry = {};

export function registerTag(name, Component) {
  registry[name] = Component;
}

export function isStructuralTag(tag) {
  return tag === "ReactIf" || tag === "ReactFor";
}

export function resolveTag(tag) {
  if (tag in registry) return registry[tag];
  if (/^[a-z]/.test(tag)) return tag; // lower-case first char => real DOM host tag
  console.warn(`TrameNode: unknown tag "${tag}", rendering nothing`);
  return () => null;
}
