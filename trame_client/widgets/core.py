SHARED_ATTRIBUTES = [
    "accesskey",
    "autocapitalize",
    "autofocus",
    ("classes", "class"),
    "contenteditable",
    "dir",
    "draggable",
    "enterkeyhint",
    "hidden",
    "id",
    "inputmode",
    "is",
    "itemid",
    "itemprop",
    "itemref",
    "itemscope",
    "itemtype",
    "lang",
    "nonce",
    "slot",
    "spellcheck",
    "style",
    "tabindex",
    "title",
    "translate",
    # --
    "ref",
    ["key", ":key"],
    ["v_on", "v-on"],
    ["v_bind", "v-bind"],
    "v_text",
    "v_html",
    "v_show",
    "v_if",
    "v_else",
    "v_else_if",
    "v_for",
    "v_model",
    "v_pre",
    "v_once",
]

SHARED_EVENTS = [
    "click",
    "mousedown",
    "mouseup",
    "mouseenter",
    "mouseleave",
    "contextmenu",
]


def py2js_key(key):
    return key.replace("_", "-")


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

    def add_child(self, elem):
        if len(self.element_stack):
            if elem.server is None:
                elem.set_server(self.element_stack[-1].server)
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


class AbstractElement:
    """
    A Vue component which can integrate with the rest of trame

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

    """

    _next_id = 1
    _debug = False

    def __init__(self, _elem_name, children=None, **kwargs):
        AbstractElement._next_id += 1
        self._id = AbstractElement._next_id
        self._server = kwargs.get("trame_server")
        self._elem_name = _elem_name
        self._allowed_keys = set()
        self._attr_names = kwargs.get("__properties", []) + SHARED_ATTRIBUTES
        self._event_names = kwargs.get("__events", []) + SHARED_EVENTS

        self._attributes = {}
        self._py_attr = kwargs
        self._children = []

        if children:
            if isinstance(children, (list, tuple)):
                self._children.extend(children)
            else:
                self._children.append(children)

        # Add ourself to context if any
        HTML_CTX.add_child(self)

    def _attr_str(self):
        return " ".join(self._attributes.values())

    def _update_allowed_keys(self):
        if hasattr(self, "_attr_names") and hasattr(self, "_event_names"):
            for items in [self._attr_names, self._event_names]:
                for item in items:
                    if isinstance(item, str):
                        self._allowed_keys.add(item)
                    else:
                        self._allowed_keys.add(item[0])

    # -------------------------------------------------------------------------
    # App associated to HTML element
    # -------------------------------------------------------------------------

    @property
    def server(self):
        """Return the associated server"""
        return self._server

    def set_server(self, v):
        """Update the associated server"""
        self._server = v

    # -------------------------------------------------------------------------
    # Buildin API
    # -------------------------------------------------------------------------

    def __getitem__(self, name):
        return self._py_attr[name]

    def __setitem__(self, name, value):
        if name in self._allowed_keys:
            self._py_attr[name] = value
        else:
            print(f"Attribute {name} is not defined for {self._elem_name}")

    def __getattr__(self, name):
        if name[0] == "_":
            raise AttributeError()

        if name in self._py_attr:
            return self._py_attr[name]

        print(f"{self._elem_name}.{name} is missing")

    def __setattr__(self, name, value):
        if name[0] == "_":
            self.__dict__[name] = value
        elif name == "children":
            self._children = value
        elif name in self._allowed_keys:
            self._py_attr[name] = value
        else:
            self.__dict__[name] = value

        if name in ["_attr_names", "_event_names"]:
            self._update_allowed_keys()

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
        self._attributes["__tts"] = f':key="`w{self._id}-${{tts}}`"'
        return self

    def attrs(self, *names):
        """
        Calling this function will process the provided attribute names and
        configure its internal so the matching HTML string could easily be
        generated later on.

        :param names: The names attribute to process
        :type names: *str
        """
        for _name in names:
            js_key = None
            name = _name
            if isinstance(_name, (list, tuple)):
                name = _name[0]
                js_key = _name[1]

            if name in self._py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                value = self._py_attr[name]

                if value is None:
                    continue

                if (
                    AbstractElement._debug
                    and js_key.startswith("v-")
                    and not isinstance(value, (tuple, list))
                ):
                    print(
                        f'Warning: A Vue directive is evaluating your expression and trame would expect a tuple instead of a plain type. <{self._elem_name} {js_key}="{value}" ... />'
                    )

                if isinstance(value, (tuple, list)):
                    if len(value) > 1:
                        self.server.state.setdefault(value[0], value[1])

                    if js_key.startswith("v-"):
                        self._attributes[name] = f'{js_key}="{value[0]}"'
                    elif js_key.startswith(":"):
                        self._attributes[name] = f'{js_key}="{value[0]}"'
                    else:
                        self._attributes[name] = f':{js_key}="{value[0]}"'
                elif isinstance(value, bool):
                    if value:
                        self._attributes[name] = js_key
                    else:
                        self._attributes[name] = f':{js_key}="false"'
                elif isinstance(value, (str, int, float)):
                    self._attributes[name] = f'{js_key}="{value}"'
                else:
                    print(
                        f"Error: Don't know how to handle attribute name '{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )

        return self

    def events(self, *names):
        """
        Calling this function will process the provided event names and
        configure its internal so the matching HTML string could easily be
        generated later on.

        :param names: The names events to process
        :type names: *str
        """
        for _name in names:
            js_key = None
            name = _name
            if isinstance(_name, tuple):
                name = _name[0]
                js_key = _name[1]
            if name in self._py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                js_key = f"@{js_key}"
                value = self._py_attr[name]

                if value is None:
                    continue

                if isinstance(value, str):
                    self._attributes[name] = f'{js_key}="{value}"'
                elif callable(value):
                    trigger_name = self.server.trigger_name(value)
                    self._attributes[name] = f"{js_key}=\"trigger('{trigger_name}')\""
                elif isinstance(value, tuple):
                    trigger_name = value[0]
                    if callable(trigger_name):
                        trigger_name = self.server.trigger_name(trigger_name)
                    if len(value) == 1:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}')\""
                    if len(value) == 2:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}', {value[1]})\""
                    if len(value) == 3:
                        self._attributes[
                            name
                        ] = f"{js_key}=\"trigger('{trigger_name}', {value[1]}, {value[2]})\""
                else:
                    print(
                        f"Error: Don't know how to handle event name '{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )
        return self

    def clear(self):
        """
        Remove all children
        """
        self._children.clear()

    def hide(self):
        """
        Hide element while keeping it in the DOM. (display: none)
        """
        self._attributes["__style"] = 'style="display: none"'

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
    def html(self):
        """
        Return a string representation of the HTML component
        """
        try:
            # Build attributes
            self.attrs(*self._attr_names)
            self.events(*self._event_names)

            # Compute HTML str
            if len(self._children):
                out_buffer = []
                out_buffer.append(f"<{self._elem_name} {self._attr_str()}>")
                for child in self._children:
                    if isinstance(child, str):
                        out_buffer.append(child)
                    else:
                        out_buffer.append(child.html)
                out_buffer.append(f"</{self._elem_name}>")
                return "\n".join(out_buffer)
            else:
                return f"<{self._elem_name} {self._attr_str()} />"
        except Exception as e:
            print(e)
            return f"<{self._elem_name} html-error />"

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        HTML_CTX.enter(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        HTML_CTX.exit(self)


class HtmlElement(AbstractElement):
    MODULE = None

    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if HtmlElement.MODULE and self.server:
            self.server.enable_module(HtmlElement.MODULE)


class Template(AbstractElement):
    """
    The standard html content template element. This is mostly used by |slot_doc_link|.

    .. |slot_doc_link| raw:: html

        <a href="https://vuejs.org/v2/guide/instance.html" target="_blank">vue's slot system</a>


    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param v_slot: The slot this template corresponds to
    """

    slot_names = set()

    def __init__(self, children=None, **kwargs):
        super().__init__("template", children, **kwargs)
        self._attr_names += ["v_slot"]
        for slot_name in Template.slot_names:
            safe_name = slot_name.replace("-", "_").replace(".", "_")
            if "<name>" in safe_name:
                safe_header, safe_tail = safe_name.split("<name>")
                header, tail = slot_name.split("<name>")
                for key in kwargs:
                    if key.startswith(header):
                        dyna_name = key[len(header) : -len(tail)]
                        self._attr_names.append(
                            (
                                f"v_slot_{safe_header}{dyna_name}{safe_tail}",
                                f"v-slot:{header}{dyna_name}{tail}",
                            )
                        )
            else:
                self._attr_names.append((f"v_slot_{safe_name}", f"v-slot:{slot_name}"))
