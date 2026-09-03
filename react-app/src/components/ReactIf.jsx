import TrameNode from "./TrameNode.jsx";

// Plain presentational component - `value` arrives already resolved (via
// useResolvedNode in the parent TrameNodeOne), so it needs no hooks of its own.
export default function ReactIf({ value, rawChildren, scope }) {
  return value ? <TrameNode nodes={rawChildren} scope={scope} /> : null;
}
