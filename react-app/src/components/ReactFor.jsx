import TrameNode from "./TrameNode.jsx";
import { extendScope } from "../runtime/scope";

// Plain presentational component - `items` arrives already resolved (via
// useResolvedNode in the parent TrameNodeOne), so it needs no hooks of its own.
// Uses the array index as its own React key (no other generically-available
// stable identity - react.For doesn't mandate items carry an id). A widget
// author wanting stable row identity across reordering puts an explicit
// `key=` on the element(s) inside the For body, honored one level down by
// computeNodeKey inside the nested <TrameNode>.
export default function ReactFor({ items, name, rawChildren, scope }) {
  return (items ?? []).map((item, index) => (
    <TrameNode
      key={index}
      nodes={rawChildren}
      scope={extendScope(scope, [name], [item])}
    />
  ));
}
