"""
Vue2/Vue3 rendering implementation for `trame_client.widgets.core.AbstractElement`.

`AbstractElement.html` doesn't build a DOM or a virtual-DOM tree - it builds a
literal Vue template string (directives, `{{ mustache }}` interpolation, ...)
that is shipped to the browser and compiled at runtime by Vue's bundled
template compiler.

`HtmlElement` (this module) is that rendering implementation: `AbstractElement`
instantiates one per widget instance (as `self._impl`, see `core.py`) whenever
`self.server.client_type` is `"vue2"` or `"vue3"`, and delegates every kwargs
/rendering concern to it. A widget declares its Vue-specific properties via
`self.props`/`self.events` (aliases onto `self._impl.props`/`self._impl.events`,
see `core.py`), e.g.:

    if self.server.client_type in VUE_CLIENT_TYPES:
        self.props += ["title"]
        self.events += ["click"]

A sibling module (e.g. `react.py`, with its own `HtmlElement`) can implement
the same interface for another `client_type` without `AbstractElement` (or
this module) needing to change.
"""

import logging
import sys

from trame_client.utils.defaults import TrameDefault
from trame_client.widgets.core import AbstractElement

DEBUG = "--debug" in sys.argv or "-d" in sys.argv

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


def as_py_arg(iterable):
    if iterable is None:
        return None
    for item in iterable:
        if isinstance(item, str):
            yield item
        else:
            yield item[0]


def register_directive(py_name, js_name=None):
    if js_name is None:
        AVAILABLE_DIRECTIVES.append(py_name)
    else:
        AVAILABLE_DIRECTIVES.append((py_name, js_name))


class HtmlElement:
    """
    Vue2/Vue3 rendering implementation for a single `AbstractElement`
    instance (stored as `elem._impl`). Owns the python kwargs (`py_attr`),
    which of them are recognized (`props`/`events`, mutable so widgets can
    extend them), and the serialized Vue template attribute-string cache
    (`attributes`) used by `render()`.
    """

    def __init__(self, elem, kwargs):
        self._elem = elem

        style = kwargs.get("style", None)
        if type(style) is dict:
            kwargs["style"] = " ".join([f"{k}: {v};" for k, v in style.items()])

        self.props = (
            kwargs.get("__properties", []) + SHARED_ATTRIBUTES + AVAILABLE_DIRECTIVES
        )
        self.events = kwargs.get("__events", []) + SHARED_EVENTS

        self.py_attr = kwargs
        self.used_py_attr = {"trame_server", "__properties", "__events", "raw_attrs"}
        self._elem._attributes = {}

        raw_attrs = kwargs.get("raw_attrs")
        if raw_attrs:
            for idx, raw_value in enumerate(raw_attrs):
                self._elem._attributes[f"_raw_{idx}"] = raw_value

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
            self._elem._attributes.pop(name, value)
        else:
            self.py_attr[name] = value

    @property
    def skipped_attributes(self):
        """
        Return the attribute names that are skipped from the HTML representation.
        This can represent miss match property/event names or missing mapping.
        """
        return set(self.py_attr.keys()) - self.used_py_attr

    def _attr_str(self):
        return " ".join(self._elem._attributes.values())

    def _process_attrs(self, names):
        """
        Process the given attribute names into Vue template attribute
        strings, stored back into `self._elem._attributes`.
        """
        elem = self._elem
        directives = [
            name
            for name in self.py_attr.keys()
            if name.startswith("v_model_") or name.startswith("v_bind_")
        ]
        self.used_py_attr.update(as_py_arg(directives))
        self.used_py_attr.update(as_py_arg(names))
        for _name in [*directives, *names]:
            js_key = None
            name = _name
            if isinstance(_name, (list, tuple)):
                name = _name[0]
                js_key = _name[1]

            if name in self.py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                value = self.py_attr[name]

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
                            value[1].set_defaults(elem.server)
                        else:
                            elem.server.state.setdefault(value[0], value[1])

                    logger.info("before: %s = %s", js_key, value[0])
                    if isinstance(value[0], str):
                        translated_value = (
                            elem.server.state.translator.translate_js_expression(
                                elem.server.state, value[0]
                            )
                        )
                    else:
                        translated_value = str(value[0])
                        if DEBUG:
                            logger.warning(
                                'Warning: <%s %s="..." /> is set with an (%s)',
                                elem._elem_name,
                                js_key,
                                type(value[0]),
                            )

                    logger.info("after: %s = %s", js_key, translated_value)
                    if js_key.startswith("v-"):
                        self._elem._attributes[name] = f'{js_key}="{translated_value}"'
                    elif js_key.startswith(":"):
                        self._elem._attributes[name] = f'{js_key}="{translated_value}"'
                    else:
                        self._elem._attributes[name] = f':{js_key}="{translated_value}"'
                elif isinstance(value, bool):
                    if value:
                        self._elem._attributes[name] = js_key
                    else:
                        self._elem._attributes[name] = f':{js_key}="false"'
                elif isinstance(value, str):
                    if js_key.startswith("v-") or js_key.startswith(":"):
                        logger.info("before: %s = %s", js_key, value)
                        value = elem.server.state.translator.translate_js_expression(
                            elem.server.state, value
                        )
                        logger.info("after: %s = %s", js_key, value)

                    self._elem._attributes[name] = f'{js_key}="{value}"'
                elif isinstance(value, (int, float)):
                    self._elem._attributes[name] = f'{js_key}="{value}"'
                else:
                    print(
                        "Error: Don't know how to handle attribute name "
                        f"'{name}' with value '{value}' in {elem.__class__}::{elem._elem_name}"
                    )

    def _process_events(self, names):
        """
        Process the given event names into Vue template event-binding
        strings, stored back into `self._elem._attributes`.
        """
        elem = self._elem
        self.used_py_attr.update(as_py_arg(names))
        processed_event = set()
        for _name in names:
            js_key = None
            name = _name
            if isinstance(_name, tuple):
                name = _name[0]
                js_key = _name[1]
            if name in self.py_attr:
                if js_key is None:
                    js_key = py2js_key(name)
                js_key = f"@{js_key}"
                value = self.py_attr[name]

                if value is None:
                    continue

                attribute = _event_value_processing(elem.server, js_key, value)
                if attribute is None:
                    # no match
                    pass
                elif isinstance(attribute, str):
                    self._elem._attributes[name] = attribute
                    processed_event.add(name)
                else:
                    print(
                        "Error: Don't know how to handle event name "
                        f"'{name}' with value '{value}' in {elem.__class__}::{elem._elem_name}"
                    )

        # process v_on_....
        for key_name in self.py_attr:
            if key_name in processed_event:
                continue

            if key_name.startswith("v_on_"):
                tokens = key_name.split("_")[2:]
                js_key = f"@{'.'.join(tokens)}"
                value = self.py_attr[key_name]

                if value is None:
                    continue

                attribute = _event_value_processing(elem.server, js_key, value)
                if attribute is None:
                    # no match
                    pass
                elif isinstance(attribute, str):
                    self.used_py_attr.add(key_name)
                    self._elem._attributes[key_name] = attribute
                else:
                    print(
                        "Error: Don't know how to handle event name "
                        f"'{key_name}' with value '{value}' in {elem.__class__}::{elem._elem_name}"
                    )

    def render(self):
        """
        Return a Vue template string representation of the owning element,
        recursing into its children.
        """
        elem = self._elem
        try:
            # Build attributes
            self._process_attrs(self.props)
            self._process_events(self.events)

            if DEBUG and self.skipped_attributes:
                logger.warning(
                    "Warning: <%s %s /> attributes will be skipped",
                    elem._elem_name,
                    "=... ".join([*self.skipped_attributes, ""]),
                )

            # Patch ref to use trame registration
            if (
                elem.server.client_type == "vue3"
                and "ref" in self._elem._attributes
                and self._elem._attributes["ref"].startswith("ref=")
            ):
                ref_name = self._elem._attributes["ref"][5:-1]
                self._elem._attributes["ref"] = (
                    f''':ref="(el) => trame.refs['{ref_name}'] = el"'''
                )

            # Compute HTML str
            if len(elem._children):
                out_buffer = []
                out_buffer.append(f"<{elem._elem_name} {self._attr_str()}>")
                for child in elem._children:
                    if isinstance(child, str):
                        translated_value = (
                            elem.server.state.translator.translate_vue_templating(
                                elem.server.state, child
                            )
                        )
                        out_buffer.append(translated_value)
                    else:
                        out_buffer.append(child.html)
                out_buffer.append(f"</{elem._elem_name}>")
                return "\n".join(out_buffer)
            else:
                return f"<{elem._elem_name} {self._attr_str()} />"
        except Exception as e:
            logger.error(e)
            return f"<{elem._elem_name} html-error />"

    def tts_sensitive(self):
        self._elem._attributes["__tts"] = f':key="`w{self._elem._id}-${{tts}}`"'

    def hide(self):
        self._elem._attributes["__style"] = 'style="display: none"'


# -----------------------------------------------------------------------------
# Vue built-in components
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
        self.props += ["v_slot"]
        for slot_name in Template.slot_names:
            safe_name = slot_name.replace("-", "_").replace(".", "_")
            if "<name>" in safe_name:
                safe_header, safe_tail = safe_name.split("<name>")
                header, tail = slot_name.split("<name>")
                for key in kwargs:
                    if key.startswith(header):
                        dyna_name = key[len(header) : -len(tail)]
                        self.props.append(
                            (
                                f"v_slot_{safe_header}{dyna_name}{safe_tail}",
                                f"v-slot:{header}{dyna_name}{tail}",
                            )
                        )
            else:
                self.props.append((f"v_slot_{safe_name}", f"v-slot:{slot_name}"))


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
        self.props += [
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
        self.props += [
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
        self.events += [
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
        self.props += [
            "tag",
            ("move_class", "moveClass"),
        ]
        self.events += [
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
        self.props += [
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
        self.props += [
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
        self.props += [
            "timeout",
            "suspensible",
        ]
        self.events += [
            "resolve",
            "pending",
            "fallback",
        ]
