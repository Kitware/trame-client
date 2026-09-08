"""
The trame widget tree, shared by every `client_type`.

`ElementContextManager`/`HTML_CTX` and `VirtualNode` are framework-agnostic:
they only manage the python-side parent/child stack used by the
`with widget:` context-manager idiom.

`AbstractElement` is the base every trame widget (across the whole trame
ecosystem) is built on, so it stays defined here rather than moving behind a
per-`client_type` subclass. What *is* isolated per `client_type` is how its
python kwargs get turned into client-side output: at construction time,
`AbstractElement` picks a rendering implementation based on
`self.server.client_type` (`vue.HtmlElement` for `"vue2"`/`"vue3"`, and in the
future `react.HtmlElement` for `"react"`) and stores it as `self._impl`. Every
other method (`attrs()`, `events()`, `html`, `hide()`, `ttsSensitive()`, ...)
just delegates to it, so adding a new `client_type` only means adding a new
sibling module with its own `HtmlElement` implementation - `AbstractElement`
itself never needs to change.

`self.props`/`self.events` are aliases onto `self._impl.props`/`self._impl.events`
- the preferred way for a widget to declare its properties:
`self.props += [...]` / `self.events += [...]`. `_attr_names`/`_event_names`
are kept working as the exact same aliases purely for backward compatibility:
every widget package across the trame ecosystem already declares its
properties with `self._attr_names += [...]` / `self._event_names += [...]`
inside its own `__init__`, so those names have to keep resolving to whatever
the active implementation considers its props/events.
"""

from trame_common.obj.component import TrameComponent

from ..utils.formatter import to_pretty_html

VUE_CLIENT_TYPES = {"vue2", "vue3"}

# Vue-only widgets (Template, Transition, ...) re-exported here for backward
# compatibility: they've always been imported from `trame_client.widgets.core`
# across the trame ecosystem. Resolved lazily (PEP 562) to avoid a circular
# import at module-load time between `core` and `vue`.
_VUE_WIDGET_EXPORTS = {
    "Template",
    "Component",
    "Transition",
    "TransitionGroup",
    "KeepAlive",
    "Teleport",
    "Suspense",
}


def __getattr__(name):
    if name in _VUE_WIDGET_EXPORTS:
        from . import vue

        return getattr(vue, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


class ElementContextManager:
    def __init__(self):
        self.element_stack = []
        self._server = None

    def enter(self, elem):
        self._server = elem.server
        self.element_stack.append(elem)

    def exit(self, elem):
        if len(self.element_stack) and elem == self.element_stack[-1]:
            self.element_stack.pop()

        if len(self.element_stack):
            self._server = self.element_stack[-1].server

    def add_child(self, elem, connect_parent=True):
        if len(self.element_stack):
            if elem.server is None:
                elem.set_server(self.element_stack[-1].server)
            if connect_parent:
                self.element_stack[-1].add_child(elem)

        if elem.server is None:
            elem.set_server(self._server)

        if elem.server is None:
            print(f"No server available for element {elem._elem_name}")


HTML_CTX = ElementContextManager()


class VirtualNode:
    """
    A VirtualNode element allow to logically define UI element that
    can be filled or used in an independent order and yet update
    dynamically the layout upon change.
    """

    def __init__(self, trame_server=None, **_):
        self._server = trame_server
        self._children = []
        self._layouts = set()

    @property
    def server(self):
        """Return the associated server"""
        return self._server

    def set_server(self, v):
        """Update the associated server"""
        self._server = v

    def add_child(self, child):
        """
        Add a component to this component's children

        :param child: The component to add as a child
        :type child: str | AbstractElement
        """
        self._children.append(child)
        return self

    def add_children(self, children):
        """
        Add components to this component's children.
        The provided children is expected to be a list.

        :param children: The list of components to add to the children
        :type children: list
        """
        self._children += children
        return self

    @property
    def children(self):
        """
        Children components
        """
        return self._children

    def clear(self):
        """
        Remove all children
        """
        self._children.clear()
        return self

    @property
    def html(self):
        """
        Return a string representation of the HTML component
        """
        out_buffer = []
        try:
            for elem in self._children:
                if isinstance(elem, str):
                    out_buffer.append(elem)
                else:
                    out_buffer.append(elem.html)
        except Exception as e:
            print(e)

        return "\n".join(out_buffer)

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        HTML_CTX.enter(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        HTML_CTX.exit(self)
        self.flush_content()

    # -------------------------------------------------------------------------
    # Layout handling
    # -------------------------------------------------------------------------

    def clear_layouts(self):
        """Remove any reference to previously registered layout"""
        self._layouts.clear()
        return self

    def flush_content(self):
        """Push VirtualNode content to registered layouts"""
        for layout in self._layouts:
            layout.flush_content()
        return self

    def __call__(self, layout=None, **kwargs):
        if layout is not None:
            self._layouts.add(layout)
            self._server = layout.server

        HTML_CTX.add_child(self)


def _get_impl_class(client_type):
    if client_type in VUE_CLIENT_TYPES:
        from . import vue

        return vue.HtmlElement
    elif client_type == "react":
        from . import react

        return react.HtmlElement

    raise TypeError(f"Unsupported client_type={client_type!r}")


class AbstractElement(TrameComponent):
    """
    A widget which can integrate with the rest of trame

    See Vue docs |vue_doc_link| for more info

    .. |vue_doc_link| raw:: html

        <a href="https://vuejs.org/v2/guide/instance.html" target="_blank">here</a>

    .. |mdn_doc_link| raw:: html

        <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" target="_blank">here</a>

    .. |mdn_event_link| raw:: html

        <a href="https://developer.mozilla.org/en-US/docs/Web/API/Element#mouse_events">here</a>

    :param name: The name of the element, like 'div' for a ``<div/>`` element
    :type name: str
    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param __properties: Provide more attribute names that should be handle
    :param __events: Provide more event names that should be handle

    Html attributes - See |mdn_doc_link| for more info

    :param id: See |mdn_doc_link| for more info
    :param classes: Match the HTML `class` attribute. See |mdn_doc_link| for more info
    :param style: See |mdn_doc_link| for more info

    Vue attributes - See |vue_doc_link| for more info

    :param ref: See |vue_doc_link| for more info
    :param v_model: See |vue_doc_link| for more info
    :param v_if: See |vue_doc_link| for more info
    :param v_show: See |vue_doc_link| for more info
    :param v_for: See |vue_doc_link| for more info
    :param key: See |vue_doc_link| for more info

    Events - See |mdn_event_link| for more info

    :param click: See |mdn_event_link| for more info
    :param mousedown: See |mdn_event_link| for more info
    :param mouseup: See |mdn_event_link| for more info
    :param mouseenter: See |mdn_event_link| for more info
    :param mouseleave: See |mdn_event_link| for more info
    :param contextmenu: See |mdn_event_link| for more info

    Raw attributes (Vue only)

    :param raw_attrs: List of string that will be added as-is in the generated template

    >>> print(html.Template(raw_attrs=["v-slot:item.1", 'class="bg-red"', '@click.stop="a=2"']))
    ... <Template v-slot:item.1 class="bg-red" @click.stop="a=2" />

    Context Name:

    :param ctx_name: name to attach instance to server.context if provided

    DOM hierarchy handling:

    :param connect_parent: True by default which means any widget instantiation will connect
                           to the context manager widget that the current instance directly belong to.
                           In some specific case, it could be useful to disable that behavior by
                           setting it to False.
    """

    _next_id = 1

    def __init__(
        self,
        _elem_name,
        children=None,
        ctx_name=None,
        connect_parent=True,
        literal_children=False,
        **kwargs,
    ):
        AbstractElement._next_id += 1
        self._id = AbstractElement._next_id
        self._server = kwargs.get("trame_server")
        self._elem_name = _elem_name
        self._attributes = {}
        self._children = []

        if children:
            if isinstance(children, (list, tuple)):
                self._children.extend(children)
            else:
                self._children.append(children)

        # Add ourself to context if any (resolves self._server from the
        # enclosing context if it wasn't provided explicitly)
        HTML_CTX.add_child(self, connect_parent)

        # Client_type specific implementation (vue.HtmlElement, react.HtmlElement, ...)
        self._impl = _get_impl_class(self.server.client_type)(self, kwargs)
        self._impl.literal_children = literal_children

        super().__init__(self._server, ctx_name=ctx_name)

    # -------------------------------------------------------------------------
    # Static helper for widgets
    # -------------------------------------------------------------------------

    @staticmethod
    def register_directive(py_name, js_name=None):
        from . import vue

        vue.register_directive(py_name, js_name)

    # -------------------------------------------------------------------------
    # App associated to HTML element
    # -------------------------------------------------------------------------

    def set_server(self, v):
        """Update the associated server"""
        self._server = v

    # -------------------------------------------------------------------------
    # Building API
    # -------------------------------------------------------------------------

    def __getitem__(self, name):
        return self._impl.get(name)

    def __setitem__(self, name, value):
        if name in self._impl.allowed_keys:
            self._impl.set(name, value)
        else:
            print(f"Attribute {name} is not defined for {self._elem_name}")

    def __getattr__(self, name):
        # self.props/self.events: aliases onto self._impl.props/self._impl.events.
        # _attr_names/_event_names are the same aliases, kept for widgets
        # across the trame ecosystem that declare their properties with
        # `self._attr_names += [...]` / `self._event_names += [...]`.
        if name in {"props", "_attr_names"}:
            return self._impl.props
        if name in {"events", "_event_names"}:
            return self._impl.events
        if name == "literal_children":
            # Only meaningful for client_type="react" (react.HtmlElement) -
            # absent under vue, where this whole indirection doesn't apply.
            return getattr(self._impl, "literal_children", False)

        if name[0] == "_":
            raise AttributeError()

        if self._impl.has(name):
            return self._impl.get(name)

        print(f"{self._elem_name}.{name} is missing")

    def __setattr__(self, name, value):
        # Backward-compat aliases (see __getattr__ above)
        if name in {"props", "_attr_names"}:
            self._impl.props = value
        elif name in {"events", "_event_names"}:
            self._impl.events = value
        elif name == "literal_children":
            self._impl.literal_children = value
        elif name[0] == "_":
            self.__dict__[name] = value
        elif name == "children":
            self._children = value
        elif name in self._impl.allowed_keys:
            self._impl.set(name, value)
        else:
            super().__setattr__(name, value)

    # -------------------------------------------------------------------------
    # helpers
    # -------------------------------------------------------------------------

    def ttsSensitive(self):
        """
        Calling this function on an element will make it fully recreate itself
        every time the layout update. Internally it is managed by adding a `key=`
        attribute which use a layout timestamp.

        This is especially useful for component that manage other elements outside
        of themself like VSelect in Vuetify.
        """
        self._impl.tts_sensitive()
        return self

    def clear(self):
        """
        Remove all children
        """
        self._children.clear()
        return self

    def hide(self):
        """
        Hide element while keeping it in the DOM. (display: none)
        """
        self._impl.hide()

    def add_child(self, child):
        """
        Add a component to this component's children

        :param child: The component to add as a child
        :type child: str | AbstractElement
        """
        self._children.append(child)

    def add_children(self, children):
        """
        Add components to this component's children.
        The provided children is expected to be a list.

        :param children: The list of components to add to the children
        :type children: list
        """
        self._children += children

    @property
    def children(self):
        """
        Children components
        """
        return self._children

    def set_text(self, value):
        """
        Replace children with a single text child element

        :param value: The text for the new text child element
        :type value: str
        """
        self.clear()
        self._children.append(value)

    @property
    def skipped_attributes(self):
        """
        Return the attribute names that are skipped from the HTML representation.
        This can represent miss match property/event names or missing mapping.
        """
        return self._impl.skipped_attributes

    @property
    def html(self):
        """
        Return a string representation of the HTML component
        """
        return self._impl.render()

    def __repr__(self):
        return to_pretty_html(self.html)

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        HTML_CTX.enter(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        HTML_CTX.exit(self)

        # flush defaults to state to enable valid translation
        self.html


class HtmlElement(AbstractElement):
    MODULE = None

    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if HtmlElement.MODULE and self.server:
            self.server.enable_module(HtmlElement.MODULE)
