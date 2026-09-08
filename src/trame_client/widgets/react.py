"""
React rendering implementation for `trame_client.widgets.core.AbstractElement`.

Unlike Vue, React ships no runtime template compiler, so `AbstractElement.html`
can't build a template string the way `vue.py` does (see that module's
docstring). Instead this implements the "serializable widget tree" design from
`docs/adding-support-for-react/`: each node serializes to a plain
JSON-compatible `dict` - `{"tag": ..., "props": {...}, "children": [...]}` -
that a client-side `TrameNode` component (not implemented here - there is no
React client bundle yet) would walk and turn into `React.createElement(...)`
calls directly, no compiler needed.

`HtmlElement` (this module) is the `client_type="react"` counterpart to
`vue.HtmlElement`: `AbstractElement` instantiates one per widget instance (as
`self._impl`, see `core.py`) whenever `self.server.client_type == "react"`.
A widget declares its React-specific properties the same way it would for Vue:

    if self.server.client_type in VUE_CLIENT_TYPES:
        self._impl.props += ["title"]
        self._impl.events += ["click"]
    elif self.server.client_type == "react":
        self._impl.props += ["title"]
        self._impl.events += [("on_click", "onClick")]

`props`/`events` entries are looked up by their *python* kwarg name and
serialize under their *react* prop name - a bare string means both are the
same (already camelCase, matching the JS side directly, e.g. `onClick=`), a
`(python_name, react_name)` tuple is for the rest (e.g. `("classes", "className")`).

Structural directives that Vue expresses as element attributes (`v-if`,
`v-for`) have no React equivalent as attributes - React expresses them as
control flow, so they're modeled here as their own tree nodes instead:
`If`, `For`. Two-way binding (`v-model`) has no single-directive React
equivalent either, so it's always spelled out as an explicit `value=`/`onChange=`
pair using `Bind`/`Callback`. Scoped slots become `Slot` (a render-prop
generator, see `react-scoped-slots.md`).

Everything under "What's still missing for full parity" in
`vue-vs-react-with-trame.md` (the widget ecosystem, a client-side expression
evaluator, fine-grained reactivity, ...) is client-runtime work with no
existing `react-app/` bundle to receive it - out of scope here. This module
only builds the Python-side tree/serialization; nothing consumes its output
yet, and `client_type="react"` still isn't wired into `trame_client.module`
(there is no built JS bundle to serve).

Where the docs give an exact wire shape (`Bind`, `Callback`, `ref`, `Slot`),
this follows it exactly. Where they explicitly leave the shape unresolved
(`If`/`For` - see `vue-vs-react-with-trame.md` section 6, items 1 and 6),
this picks a shape consistent with the rest of the schema (its own `"tag"`,
alongside real DOM tags) rather than inventing a second schema.
"""

from trame_client.utils.defaults import TrameDefault
from trame_client.widgets.core import HTML_CTX

__all__ = [
    "Bind",
    "Callback",
    "If",
    "For",
    "Slot",
]


# -----------------------------------------------------------------------------
# Value wrappers - Bind / Callback
# -----------------------------------------------------------------------------


class Bind:
    """
    react.Bind(js_expression, **state_defaults)

    A JavaScript expression string, evaluated client-side against the current
    scope (trame state, plus any `For`/`Slot` local scope in effect). A plain
    state key name (`"count"`) is itself a trivially valid expression.

    Every keyword argument sets a default on trame's shared state - one
    `state.setdefault(key, value)` call per kwarg - independent of what the
    expression itself references.

    Usable as a prop value (`value=react.Bind("count", count=2)`), directly
    inside a `children` list (`html.Div(["count = ", react.Bind("count")])`,
    see `react-text-interpolation.md`), or nested inside a dict-valued prop
    such as `style` (`style={"color": react.Bind("color", color="red")}`) -
    the surrounding dict's other entries stay static.
    """

    def __init__(self, js_expression, **state_defaults):
        self.js_expression = js_expression
        self.state_defaults = state_defaults

    def to_json(self, server):
        for key, value in self.state_defaults.items():
            if isinstance(value, TrameDefault):
                value.set_defaults(server)
            else:
                server.state.setdefault(key, value)

        return {"js": self.js_expression}


class Callback:
    """
    react.Callback(value, *args, modifiers=None)

    Wraps either a raw JS expression (evaluated client-side, `value` is a
    `str`) or a Python callable (invoked server-side through a trame
    trigger), optionally combined with event `modifiers` (`"prevent"`,
    `"stop"`, ...) standing in for Vue's `.prevent`/`.stop`.

    `*args` are extra JS-expression strings forwarded to the trigger call
    when `value` is callable - `Callback(self.reset, "[4]", "{}")` calls
    `self.reset(4)` server-side, mirroring Vue's `click=(self.reset, "[4]", "{}")`.
    """

    def __init__(self, value, args=None, kwargs=None, modifiers=None):
        self.value = value
        self.args = args
        self.kwargs = kwargs
        self.modifiers = list(modifiers) if modifiers else []

    def to_json(self, server):
        if callable(self.value):
            callback = {"trigger": server.trigger_name(self.value)}
            if self.args:
                callback["args"] = {"js": self.args}
            if self.kwargs:
                callback["kwargs"] = {"js": self.kwargs}
        else:
            callback = {"js": self.value}

        result = {"callback": callback}
        if self.modifiers:
            result["modifiers"] = self.modifiers

        return result


def _serialize_children(children, server):
    out_buffer = []
    for child in children:
        if isinstance(child, str):
            # No {{ mustache }} parsing for react: a plain string child is
            # always literal text (react-text-interpolation.md).
            out_buffer.append(child)
        elif isinstance(child, Bind):
            out_buffer.append(child.to_json(server))
        else:
            # `child.html` is a property (recursively rendering child's own
            # subtree) - `hasattr(child, "html")` would compute it once just
            # to answer the question, then a second time right after to use
            # it. That 2x-per-level doubling compounds multiplicatively with
            # tree depth (2**depth), so a single `getattr(..., None)` here is
            # what keeps a deeply nested tree linear instead of exponential.
            html = getattr(child, "html", None)
            out_buffer.append(child if html is None else html)
    return out_buffer


# -----------------------------------------------------------------------------
# Structural nodes - If / For / Slot
# -----------------------------------------------------------------------------


class _ReactNode:
    """
    Shared base for the structural widgets below (`If`, `For`, `Slot`): none
    of them render as a DOM tag, they only collect children and attach into
    the surrounding widget tree the same way `AbstractElement`/`VirtualNode`
    already do (`HTML_CTX`, `widgets/core.py`).
    """

    _elem_name = "react-node"

    def __init__(self, connect_parent=True, **kwargs):
        self._server = kwargs.get("trame_server")
        self._children = []

        # Resolves self._server from the enclosing context even when
        # connect_parent=False (see Slot below)
        HTML_CTX.add_child(self, connect_parent)

    @property
    def server(self):
        return self._server

    def set_server(self, v):
        self._server = v

    def add_child(self, child):
        self._children.append(child)

    def add_children(self, children):
        self._children += children

    @property
    def children(self):
        return self._children

    def __enter__(self):
        HTML_CTX.enter(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        HTML_CTX.exit(self)


class If(_ReactNode):
    """
    with react.If(value="count > 5"):
        html.Div("Count is high")

    Structural marker (not a real DOM tag): tells the client renderer to only
    mount its children while `value` is truthy. `value` is wrapped in `Bind`
    automatically unless already one.
    """

    _elem_name = "ReactIf"

    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.value = value if isinstance(value, Bind) else Bind(value)

    @property
    def html(self):
        return {
            "tag": self._elem_name,
            "props": {
                "value": self.value.to_json(self.server),
            },
            "children": _serialize_children(self._children, self.server),
        }


class For(_ReactNode):
    """
    with react.For(items="items", name="item"):
        html.Li(react.Bind("item"))

    Structural marker (not a real DOM tag): tells the client renderer to
    repeat its children once per entry of `items`, exposing each entry to
    that subtree's scope under `name`. `items` is wrapped in `Bind`
    automatically unless already one.
    """

    _elem_name = "ReactFor"

    def __init__(self, items, name, **kwargs):
        super().__init__(**kwargs)
        self.items = items if isinstance(items, Bind) else Bind(items)
        self.name = name

    @property
    def html(self):
        return {
            "tag": self._elem_name,
            "props": {
                "items": self.items.to_json(self.server),
                "name": self.name,
            },
            "children": _serialize_children(self._children, self.server),
        }


class Slot(_ReactNode):
    """
    with react.Slot(params=["item"]) as render_item_name:
        html.Strong(react.Bind("item.name"))

    VDataTable(items=react.Bind("items"), renderItemName=render_item_name)

    Captures children as reusable render-prop content, handed to a widget as
    an ordinary prop value rather than nested inside that widget's own `with`
    block - the React analogue of a Vue scoped slot (`react-scoped-slots.md`).
    `params` names the values the owning widget will pass back at call time
    (the React-side equivalent of Vue's `v-slot="{ item }"` destructuring).

    Defined outside the widget's own `with` block, so unlike `If`/`For` it
    defaults to `connect_parent=False`: it must not also get auto-attached as
    a child of whatever context happens to be open at the point it's defined.
    """

    _elem_name = "trame-slot"

    def __init__(self, params=None, connect_parent=False, **kwargs):
        super().__init__(connect_parent=connect_parent, **kwargs)
        self.params = list(params) if params else []

    def to_json(self, server):
        assert server == self.server
        return {
            "slot": {
                "params": self.params,
                "children": _serialize_children(self._children, self.server),
            }
        }


# -----------------------------------------------------------------------------
# HtmlElement - the client_type="react" AbstractElement._impl implementation
# -----------------------------------------------------------------------------

# Global HTML attributes / DOM events every react element recognizes by
# default, mirroring vue.SHARED_ATTRIBUTES/SHARED_EVENTS in spirit. A bare
# string means the python kwarg and the react prop share the same (already
# camelCase) name; a (python_name, react_name) tuple is for the rest - every
# SHARED_EVENTS entry is one of these, so Python callers use snake_case
# (onClick= becomes on_click=) while the wire/react prop name stays camelCase.
SHARED_PROPS = [
    ("classes", "className"),
    "id",
    "style",
    "title",
    "hidden",
    "lang",
    "dir",
    "draggable",
    "spellCheck",
    "contentEditable",
    "tabIndex",
    "ref",
    "key",
    "value",
]

SHARED_EVENTS = [
    ("on_click", "onClick"),
    ("on_double_click", "onDoubleClick"),
    ("on_context_menu", "onContextMenu"),
    ("on_mouse_down", "onMouseDown"),
    ("on_mouse_up", "onMouseUp"),
    ("on_mouse_enter", "onMouseEnter"),
    ("on_mouse_leave", "onMouseLeave"),
    ("on_mouse_move", "onMouseMove"),
    ("on_mouse_over", "onMouseOver"),
    ("on_mouse_out", "onMouseOut"),
    ("on_key_down", "onKeyDown"),
    ("on_key_up", "onKeyUp"),
    ("on_key_press", "onKeyPress"),
    ("on_submit", "onSubmit"),
    ("on_input", "onInput"),
    ("on_change", "onChange"),
    ("on_focus", "onFocus"),
    ("on_blur", "onBlur"),
    ("on_touch_start", "onTouchStart"),
    ("on_touch_move", "onTouchMove"),
    ("on_touch_end", "onTouchEnd"),
    ("on_touch_cancel", "onTouchCancel"),
]


class HtmlElement:
    """
    React rendering implementation for a single `AbstractElement` instance
    (stored as `elem._impl`). Owns the python kwargs (`py_attr`), which of
    them are recognized (`props`/`events`, mutable so widgets can extend
    them), and serializes them into the JSON tree shape described above.
    """

    def __init__(self, elem, kwargs):
        self._elem = elem
        self._hidden = False
        self._tts_sensitive = False
        self.literal_children = False

        self.props = kwargs.get("__properties", []) + SHARED_PROPS
        self.events = kwargs.get("__events", []) + SHARED_EVENTS

        self.py_attr = kwargs
        self.used_py_attr = {"trame_server", "__properties", "__events"}

    @property
    def allowed_keys(self):
        keys = set()
        for items in (self.props, self.events):
            for item in items:
                if isinstance(item, str):
                    keys.add(item)
                else:
                    keys.add(item[0])
        return keys

    def has(self, name):
        return name in self.py_attr

    def get(self, name):
        return self.py_attr[name]

    def set(self, name, value):
        if value is None:
            self.py_attr.pop(name, value)
        else:
            self.py_attr[name] = value

    @property
    def skipped_attributes(self):
        """
        Return the attribute names that are skipped from the tree
        representation. This can represent miss match property/event names
        or missing mapping.
        """
        return set(self.py_attr.keys()) - self.used_py_attr

    def _serialize_value(self, name, value, server):
        if isinstance(value, (Bind, Callback, Slot)):
            return value.to_json(server)
        if isinstance(value, dict):
            # A dict-valued prop (e.g. `style={"color": react.Bind(...)}`) may
            # mix plain values with `Bind`/`Callback` entries - recurse so the
            # client sees a plain object with per-key `{"js": ...}` markers
            # instead of an un-serialized Python object (react-app's
            # `classifyProps` resolves those nested markers individually).
            return {
                key: self._serialize_value(name, item, server)
                for key, item in value.items()
            }
        return value

    def render(self):
        """
        Return a JSON-serializable dict representation of the owning
        element, recursing into its children. There is no client bundle to
        consume this yet (see module docstring) - this only builds the tree.
        """
        elem = self._elem

        # Keyed by python name first (like vue.HtmlElement's `attributes`
        # dict), then flattened to react names below - not the other way
        # around. `widgets/html.py` (generated) bakes Vue-flavored
        # (py_name, js_key) hints (e.g. ("key", ":key")) into every element's
        # shared attribute list, redundantly with this module's own
        # SHARED_PROPS; resolving by react name first would let a later,
        # Vue-flavored duplicate for the same kwarg produce a second,
        # incorrect prop instead of overwriting the first.
        react_name_by_py_name = {}
        for name in (*self.props, *self.events):
            py_name, react_name = (
                (name, name) if isinstance(name, str) else (name[0], name[1])
            )
            react_name_by_py_name.setdefault(py_name, react_name)

        props = {}
        for py_name, react_name in react_name_by_py_name.items():
            if py_name not in self.py_attr:
                continue

            self.used_py_attr.add(py_name)
            value = self.py_attr[py_name]
            if value is None:
                continue

            props[react_name] = self._serialize_value(py_name, value, elem.server)

        if self._hidden:
            style = props.get("style")
            style = dict(style) if isinstance(style, dict) else {}
            style["display"] = "none"
            props["style"] = style

        result = {
            "tag": elem._elem_name,
            "props": props,
            "children": _serialize_children(elem._children, elem.server),
        }
        if self.literal_children:
            # See react-app/src/runtime/resolveLiteralChildren.js: some
            # components (MUI's Select/Tabs/RadioGroup/...) read
            # `child.props.value` / `child.props.children` straight off their
            # `children` array via `React.Children`, before anything renders
            # - the usual lazy per-node wrapper defeats that, since those
            # props would live on the wrapper instead of on a real element.
            result["literalChildren"] = True
        return result

    def hide(self):
        self._hidden = True

    def tts_sensitive(self):
        """No implementation for react"""
