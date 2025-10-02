import sys
import logging

from trame_client.utils.defaults import TrameDefault
from trame_client.utils.formatter import to_pretty_html
from trame_common.obj.component import TrameComponent

AVAILABLE_DIRECTIVES = [
    ("v_text", "v-text"),
    ("v_html", "v-html"),
    ("v_show", "v-show"),
    ("v_if", "v-if"),
    ("v_else", "v-else"),
    ("v_else_if", "v-else-if"),
    ("v_for", "v-for"),
    ("v_on", "v-on"),
    ("v_bind", "v-bind"),
    ("v_model", "v-model"),
    ("v_model_lazy", "v-model.lazy"),
    ("v_model_number", "v-model.number"),
    ("v_model_trim", "v-model.trim"),
    ("v_slot", "v-slot"),
    ("v_pre", "v-pre"),
    ("v_once", "v-once"),
    ("v_memo", "v-memo"),
    ("v_cloak", "v-cloak"),
]
KEY_ALIAS = [
    "enter",
    "tab",
    "delete",
    "esc",
    "space",
    "left",
    "up",
    "right",
    "down",
]
KEY_MODIFIER = ["ctrl", "alt", "shift", "meta"]
MOUSE_BUTTONS = ["left", "right", "middle"]
V_ON_MODIFIER = [
    "stop",
    "prevent",
    "capture",
    "self",
    "once",
    "left",
    "right",
    "middle",
    "passive",
]  # *KEY_ALIAS
V_ON_TYPE_MOUSE = [
    "click",
    "contextmenu",
    "dblclick",
    "mousedown",
    "mouseenter",
    "mouseleave",
    "mousemove",
    "mouseup",
    "mouseout",
    "mouseover",
]
V_ON_TYPE_KEYBOARD = [
    "keydown",
    "keyup",
    "keypress",
]
V_ON_TYPE_FORM = [
    "submit",
    "input",
    "change",
    "focus",
    "blur",
]
V_ON_TYPE_TOUCH = [
    "touchstart",
    "touchmove",
    "touchend",
    "touchcancel",
]
V_ON_TYPE_UI = [
    "scroll",
    "resize",
    "select",
]
V_ON_TYPE_ANIM = [
    "animationstart",
    "animationend",
    "animationiteration",
]
V_ON_TYPE_TRANSITION = [
    "transitionstart",
    "transitionend",
    "transitioncancel",
]

V_MODEL_MODIFIER = {"lazy", "number", "trim"}

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
]

# !all modifiers should go through v_on_click_left_stop...
SHARED_EVENTS = [
    *V_ON_TYPE_MOUSE,
    *V_ON_TYPE_KEYBOARD,
    *V_ON_TYPE_FORM,
    *V_ON_TYPE_TOUCH,
    *V_ON_TYPE_ANIM,
    *V_ON_TYPE_TRANSITION,
    # -------------------------------------------------------------------------
    # Should not enable by default as they tend to conflict with widget
    # properties. Use v_on_{}= to enable any missing mapping.
    # -------------------------------------------------------------------------
    # *V_ON_TYPE_UI,
]

logger = logging.getLogger(__name__)


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


def _event_value_processing(server, js_key, value):
    if isinstance(value, str):
        translated_value = server.state.translator.translate_js_expression(
            server.state, value
        )
        return f'{js_key}="{translated_value}"'
    elif callable(value):
        trigger_name = server.trigger_name(value)
        return f"{js_key}=\"trigger('{trigger_name}')\""
    elif isinstance(value, tuple):
        trigger_name = value[0]
        if callable(trigger_name):
            trigger_name = server.trigger_name(trigger_name)
        if len(value) == 1:
            return f"{js_key}=\"trigger('{trigger_name}')\""
        if len(value) == 2:
            translated_value = server.state.translator.translate_js_expression(
                server.state, value[1]
            )
            return f"{js_key}=\"trigger('{trigger_name}', {translated_value})\""
        if len(value) == 3:
            translated_value = server.state.translator.translate_js_expression(
                server.state, value[1]
            )
            # We don't want to translate kwargs as we may change keys rather than just values
            return f"{js_key}=\"trigger('{trigger_name}', {translated_value}, {value[2]})\""
    return False


class AbstractElement(TrameComponent):
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

    Raw attributes

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
    _debug = "--debug" in sys.argv or "-d" in sys.argv

    def __init__(
        self,
        _elem_name,
        children=None,
        raw_attrs=None,
        ctx_name=None,
        connect_parent=True,
        **kwargs,
    ):
        AbstractElement._next_id += 1
        self._id = AbstractElement._next_id
        self._server = kwargs.get("trame_server")
        self._elem_name = _elem_name
        self._allowed_keys = set()
        self._attr_names = (
            kwargs.get("__properties", []) + SHARED_ATTRIBUTES + AVAILABLE_DIRECTIVES
        )
        self._event_names = kwargs.get("__events", []) + SHARED_EVENTS

        style = kwargs.get("style", None)
        if type(style) is dict:
            kwargs["style"] = " ".join([f"{k}: {v};" for k, v in style.items()])

        self._attributes = {}
        self._py_attr = kwargs
        self._children = []

        # Handle raw attributes if provided
        if raw_attrs:
            for idx, raw_value in enumerate(raw_attrs):
                self._attributes[f"_raw_{idx}"] = raw_value

        if children:
            if isinstance(children, (list, tuple)):
                self._children.extend(children)
            else:
                self._children.append(children)

        # Add ourself to context if any
        HTML_CTX.add_child(self, connect_parent)

        super().__init__(self._server, ctx_name=ctx_name)

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
    # Static helper for widgets
    # -------------------------------------------------------------------------

    @staticmethod
    def register_directive(py_name, js_name=None):
        global AVAILABLE_DIRECTIVES
        if js_name is None:
            AVAILABLE_DIRECTIVES.append(py_name)
        else:
            AVAILABLE_DIRECTIVES.append((py_name, js_name))

    # -------------------------------------------------------------------------
    # App associated to HTML element
    # -------------------------------------------------------------------------

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
            if value is None:
                self._py_attr.pop(name, value)
                self._attributes.pop(name, value)
            else:
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
            if value is None:
                self._py_attr.pop(name, value)
                self._attributes.pop(name, value)
            else:
                self._py_attr[name] = value

        else:
            super().__setattr__(name, value)

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
        directives = [
            name
            for name in self._py_attr.keys()
            if name.startswith("v_model_") or name.startswith("v_bind_")
        ]
        for _name in [*directives, *names]:
            js_key = None
            name = _name
            if isinstance(_name, (list, tuple)):
                name = _name[0]
                js_key = _name[1]

            if name in self._py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                value = self._py_attr[name]

                # smart key handling
                if name.startswith("v_model_"):
                    model_name, *modifiers = name.split("_")[2:]
                    if model_name in V_MODEL_MODIFIER and len(modifiers) == 0:
                        js_key = f"v-model.{model_name}"
                    else:
                        js_key = f"v-model:{model_name}{'.' if len(modifiers) else ''}{'.'.join(modifiers)}"
                elif name.startswith("v_bind_"):
                    prop_name, *modifiers = name.split("_")[2:]
                    js_key = f":{prop_name}{'.' if len(modifiers) else ''}{'.'.join(modifiers)}"

                if value is None:
                    continue

                logger.info("js_key = %s", js_key)

                if isinstance(value, (tuple, list)):
                    if len(value) > 1:
                        if isinstance(value[1], TrameDefault):
                            value[1].set_defaults(self.server)
                        else:
                            self.server.state.setdefault(value[0], value[1])

                    logger.info("before: %s = %s", js_key, value[0])
                    if isinstance(value[0], str):
                        translated_value = (
                            self.server.state.translator.translate_js_expression(
                                self.server.state, value[0]
                            )
                        )
                    else:
                        translated_value = str(value[0])
                        if AbstractElement._debug:
                            logger.warning(
                                'Warning: <%s %s="..." /> is set with an (%s)',
                                self._elem_name,
                                js_key,
                                type(value[0]),
                            )

                    logger.info("after: %s = %s", js_key, translated_value)
                    if js_key.startswith("v-"):
                        self._attributes[name] = f'{js_key}="{translated_value}"'
                    elif js_key.startswith(":"):
                        self._attributes[name] = f'{js_key}="{translated_value}"'
                    else:
                        self._attributes[name] = f':{js_key}="{translated_value}"'
                elif isinstance(value, bool):
                    if value:
                        self._attributes[name] = js_key
                    else:
                        self._attributes[name] = f':{js_key}="false"'
                elif isinstance(value, str):
                    if js_key.startswith("v-") or js_key.startswith(":"):
                        logger.info("before: %s = %s", js_key, value)
                        value = self.server.state.translator.translate_js_expression(
                            self.server.state, value
                        )
                        logger.info("after: %s = %s", js_key, value)

                    self._attributes[name] = f'{js_key}="{value}"'
                elif isinstance(value, (int, float)):
                    self._attributes[name] = f'{js_key}="{value}"'
                else:
                    print(
                        "Error: Don't know how to handle attribute name "
                        f"'{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
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
        processed_event = set()
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

                attribute = _event_value_processing(self.server, js_key, value)
                if attribute is None:
                    # no match
                    pass
                elif isinstance(attribute, str):
                    self._attributes[name] = attribute
                    processed_event.add(name)
                else:
                    print(
                        "Error: Don't know how to handle event name "
                        f"'{name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )

        # process v_on_....
        for key_name in self._py_attr:
            if key_name in processed_event:
                continue

            if key_name.startswith("v_on_"):
                tokens = key_name.split("_")[2:]
                js_key = f"@{'.'.join(tokens)}"
                value = self._py_attr[key_name]

                if value is None:
                    continue

                attribute = _event_value_processing(self.server, js_key, value)
                if attribute is None:
                    # no match
                    pass
                elif isinstance(attribute, str):
                    self._attributes[key_name] = attribute
                else:
                    print(
                        "Error: Don't know how to handle event name "
                        f"'{key_name}' with value '{value}' in {self.__class__}::{self._elem_name}"
                    )

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

            # Patch ref to use trame registration
            if (
                self.server.client_type == "vue3"
                and "ref" in self._attributes
                and self._attributes["ref"].startswith("ref=")
            ):
                ref_name = self._attributes["ref"][5:-1]
                self._attributes["ref"] = (
                    f''':ref="(el) => trame.refs['{ref_name}'] = el"'''
                )

            # Compute HTML str
            if len(self._children):
                out_buffer = []
                out_buffer.append(f"<{self._elem_name} {self._attr_str()}>")
                for child in self._children:
                    if isinstance(child, str):
                        translated_value = (
                            self.server.state.translator.translate_vue_templating(
                                self.server.state, child
                            )
                        )
                        out_buffer.append(translated_value)
                    else:
                        out_buffer.append(child.html)
                out_buffer.append(f"</{self._elem_name}>")
                return "\n".join(out_buffer)
            else:
                return f"<{self._elem_name} {self._attr_str()} />"
        except Exception as e:
            logger.error(e)
            return f"<{self._elem_name} html-error />"

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


class HtmlElement(AbstractElement):
    MODULE = None

    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if HtmlElement.MODULE and self.server:
            self.server.enable_module(HtmlElement.MODULE)


# -----------------------------------------------------------------------------
# Vue based components
# -----------------------------------------------------------------------------


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


# -----------------------------------------------------------------------------


class Component(AbstractElement):
    """
    Vue.js dynamic component element.

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param is_name: name of the component to map
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("component", children, **kwargs)
        self._attr_names += [
            ("is_name", "is"),
        ]


# -----------------------------------------------------------------------------


class Transition(AbstractElement):
    """
    Vue.js Transition component element.
    Provides animated transition effects to a single element or component.

    Properties:

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param name: Used to automatically generate transition CSS class names.
        e.g. `name: 'fade'` will auto expand to `.fade-enter`,
        `.fade-enter-active`, etc.
    :param css: Whether to apply CSS transition classes. (Default: true)
    :param type: Specifies the type of transition events to wait for to
        determine transition end timing. Default behavior is auto detecting
        the type that has longer duration. (transition, animation)
    :param duraction: Specifies explicit durations of the transition.
        Default behavior is wait for the first `transitionend` or
        `animationend` event on the root transition element.
    :param mode: Controls the timing sequence of leaving/entering transitions.
        Default behavior is simultaneous. ('in-out' | 'out-in' | 'default')
    :param appear: Whether to apply transition on initial render.
        (default: false)
    :param enter_from_class: Props for customizing transition classes.
    :param enter_active_class: Props for customizing transition classes.
    :param enter_to_class: Props for customizing transition classes.
    :param appear_from_class: Props for customizing transition classes.
    :param appear_active_class: Props for customizing transition classes.
    :param appear_to_class: Props for customizing transition classes.
    :param leave_from_class: Props for customizing transition classes.
    :param leave_active_class: Props for customizing transition classes.
    :param leave_to_class: Props for customizing transition classes.

    Events:

    :param before_enter:
    :param before_leave:
    :param enter:
    :param leave:
    :param appear:
    :param after_enter:
    :param after_leave:
    :param after_appear:
    :param enter_cancelled:
    :param leave_cancelled:
    :param appear_cancelled:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("transition", children, **kwargs)
        self._attr_names += [
            "name",
            "css",
            "type",
            "duraction",
            "mode",
            "appear",
            ("enter_from_class", "enterFromClass"),
            ("enter_active_class", "enterActiveClass"),
            ("enter_to_class", "enterToClass"),
            ("appear_from_class", "appearFromClass"),
            ("appear_active_class", "appearActiveClass"),
            ("appear_to_class", "appearToClass"),
            ("leave_from_class", "leaveFromClass"),
            ("leave_active_class", "leaveActiveClass"),
            ("leave_to_class", "leaveToClass"),
        ]
        self._event_names += [
            ("before_enter", "before-enter"),
            ("before_leave", "before-leave"),
            ("enter", "enter"),
            ("leave", "leave"),
            ("appear", "appear"),
            ("after_enter", "after-enter"),
            ("after_leave", "after-leave"),
            ("after_appear", "after-appear"),
            ("enter_cancelled", "enter-cancelled"),
            ("leave_cancelled", "leave-cancelled"),
            ("appear_cancelled", "appear-cancelled"),
        ]


# -----------------------------------------------------------------------------


class TransitionGroup(AbstractElement):
    """
    Vue.js TransitionGroup component element.
    Provides transition effects for multiple elements or components in a list.

    Properties:

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None

    Events:

    :param before_enter:
    :param before_leave:
    :param enter:
    :param leave:
    :param appear:
    :param after_enter:
    :param after_leave:
    :param after_appear:
    :param enter_cancelled:
    :param leave_cancelled:
    :param appear_cancelled:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("transition-group", children, **kwargs)
        self._attr_names += [
            "tag",
            ("move_class", "moveClass"),
        ]
        self._event_names += [
            ("before_enter", "before-enter"),
            ("before_leave", "before-leave"),
            ("enter", "enter"),
            ("leave", "leave"),
            ("appear", "appear"),
            ("after_enter", "after-enter"),
            ("after_leave", "after-leave"),
            ("after_appear", "after-appear"),
            ("enter_cancelled", "enter-cancelled"),
            ("leave_cancelled", "leave-cancelled"),
            ("appear_cancelled", "appear-cancelled"),
        ]


# -----------------------------------------------------------------------------


class KeepAlive(AbstractElement):
    """
    Vue.js KeepAlive component element.
    Caches dynamically toggled components wrapped inside.

    Properties:

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param include: If specified, only components with names matched
        by `include` will be cached.
    :param exclude: Any component with a name matched by `exclude`
        will not be cached.
    :param max: The maximum number of component instances to cache.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("keep-alive", children, **kwargs)
        self._attr_names += [
            "include",
            "exclude",
            "max",
        ]


# -----------------------------------------------------------------------------


class Teleport(AbstractElement):
    """
    Vue.js Teleport component element.
    Renders its slot content to another part of the DOM.

    Properties:

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :param to: Required. Specify target container.
        Can either be a selector or an actual element.
    :param disabled: When `true`, the content will remain in its original
        location instead of moved into the target container.
        Can be changed dynamically.
    :param defer: When `true`, the Teleport will defer until other parts
        of the application have been mounted before resolving its target.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("teleport", children, **kwargs)
        self._attr_names += [
            "to",
            "disabled",
            "defer",
        ]


# -----------------------------------------------------------------------------


class Suspense(AbstractElement):
    """
    Vue.js Suspense component element.
    Used for orchestrating nested async dependencies in a component tree.

    Properties:

    :param children: The children nested within this element
    :type children:  str | list[trame.html.*] | trame.html.* | None
    :type timeout:
    :type suspensible:

    Events:

    :param resolve:
    :param pending:
    :param fallback:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("suspense", children, **kwargs)
        self._attr_names += [
            "timeout",
            "suspensible",
        ]
        self._event_names += [
            "resolve",
            "pending",
            "fallback",
        ]
