from .core import AbstractElement

__all__ = [
    "Loading",
    "ServerTemplate",
    "Script",
    "Style",
    "JSEval",
    "Getter",
    "ClientStateChange",
    "ClientTriggers",
    "DeepReactive",
    "LifeCycleMonitor",
    "SizeObserver",
]


# -----------------------------------------------------------------------------
# TrameLoading
# -----------------------------------------------------------------------------
class Loading(AbstractElement):
    """
    Three circle spinning with a message

    :param message: Content of the message
    :type name: str
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-loading", children, **kwargs)
        self._attr_names += [
            "message",
        ]


# -----------------------------------------------------------------------------
# TrameServerTemplate
# -----------------------------------------------------------------------------
class ServerTemplate(AbstractElement):
    """
    Template content presentation

    :param name: Name of the template to display. (default: 'main')
    :type name: str

    :param use_url: If true, will use the `{url_key}=` from the url to override
                    the `name=` attribute.
    :type use_url: bool

    :param url_key: Name of the key to extract from url for use_url. (default: 'ui')
    :type url_key: str
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-template", children, **kwargs)
        self._attr_names += [
            ("name", "templateName"),
            ("use_url", "useUrl"),
            ("url_key", "urlKey"),
        ]


# -----------------------------------------------------------------------------
# TrameExec
# -----------------------------------------------------------------------------
class JSEval(AbstractElement):
    """Provide means to execute JS code"""

    _next_id = 0

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-exec", children, **kwargs)
        JSEval._next_id += 1
        self.__ref = kwargs.get("ref", f"trame_exec_ref_{JSEval._next_id}")
        self._attributes["ref"] = f'ref="{self.__ref}"'
        self._attr_names += [
            "event",
        ]
        self._event_names += [
            "exec",
        ]

    def exec(self, event=None):
        if event is None:
            self.server.js_call(self.__ref, "exec")
        else:
            self.server.js_call(self.__ref, "exec", event)


# -----------------------------------------------------------------------------
# TrameStyle
# -----------------------------------------------------------------------------
class Style(AbstractElement):
    """Provide means to inject global CSS rules"""

    _next_id = 0

    def __init__(self, css_content=None, **kwargs):
        Style._next_id += 1
        super().__init__("trame-style", **kwargs)
        self._key = f"trame__inline_style_{Style._next_id}"
        self._attributes["_css"] = f':css="{self._key}"'
        self.server.root_server.state.setdefault(self._key, css_content)

    def update(self, css_content):
        """Update style content"""
        self.server.root_server.state[self._key] = css_content

    @property
    def var_name(self):
        """Name the the state variable used by this widget"""
        return self._key


# -----------------------------------------------------------------------------
# TrameScript
# -----------------------------------------------------------------------------
class Script(AbstractElement):
    """Provide means to inject a global script tag"""

    _next_id = 0

    def __init__(self, script_content=None, **kwargs):
        Script._next_id += 1
        super().__init__("trame-script", **kwargs)
        self._key = f"trame__inline_script_{Script._next_id}"
        self._attributes["_script"] = f':script="{self._key}"'
        self.server.root_server.state.setdefault(self._key, script_content)
        self._attr_names += [
            "module",  # type="module" or "text/javascript"
            "async",
            "crossorigin",
            "defer",
            "integrity",
            "nomodule",
            "referrerpolicy",
            "src",
        ]

    def update(self, script_content):
        """Update style content"""
        self.server.root_server.state[self._key] = script_content

    @property
    def var_name(self):
        """Name the the state variable used by this widget"""
        return self._key


# -----------------------------------------------------------------------------
# TrameGetter
# -----------------------------------------------------------------------------
class Getter(AbstractElement):
    """Provide means to extract a reactive state variable from its name

    :param name: Name of the state variable to extract. This can be an expression too.

    :param value_name: Name of the JavaScript variable name (default: "value")
    :type value_name: str

    :param key_name: Name for the JavaScript variable that will hold the evaluate expression of the "name" property.

    :param update_nested_name: Method name if you aim to update the nested structure.

    :param update_name: Method name if you aim to update the full value.
    """

    def __init__(
        self,
        children=None,
        value_name=None,
        key_name=None,
        update_nested_name=None,
        update_name=None,
        **kwargs,
    ):
        super().__init__("trame-getter", **kwargs)
        self._attr_names += [
            "name",
        ]
        extracts = []
        if key_name:
            extracts.append(f"keyName: {key_name}")

        if update_nested_name:
            extracts.append(f"updateNested: {update_nested_name}")

        if update_name:
            extracts.append(f"update: {update_name}")

        if value_name:
            extracts.append(f"value: {value_name}")
        else:
            extracts.append("value")

        self._attributes["slot"] = f'v-slot="{{ { ", ".join(extracts) } }}"'


# -----------------------------------------------------------------------------
# TrameClientStateChange
# -----------------------------------------------------------------------------
class ClientStateChange(AbstractElement):
    """
    Allow the client side to trigger an event when a state element changes.

    :param value: Name of the state variable to monitor
    :type value: str
    :param immediate: Trigger change right away rather than at nextTick (default: False)
    :type immediate: bool
    :param trigger_on_create: If set to true, the change event will be triggered when the client start. (default: False)
    :type trigger_on_create: bool
    :param change: Event triggered when state[value] change
    :type change: Function or JS expression (event)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-client-state-change", children, **kwargs)
        self._attr_names += [
            ("value", ":value"),
            "immediate",
            ("trigger_on_create", "triggerChangeOnCreate"),
        ]
        self._event_names += ["change"]


# -----------------------------------------------------------------------------
# TrameClientTriggers
# -----------------------------------------------------------------------------
class ClientTriggers(AbstractElement):
    """
    Allow to trigger an event on the client side

    :param ref: Identifier for the client side DOM elem
    :param **kwargs: List of events to registers with their callbacks

    Built-in events are:
       - mounted
       - created
       - before_destroy
       - before_unmount
       - exit
    """

    def __init__(self, ref="trame_triggers", children=None, **kwargs):
        self.__name = ref
        super().__init__("trame-client-triggers", children=None, ref=ref, **kwargs)
        self._attr_names += ["ref"]
        self._event_names += [
            ("before_destroy", "beforeDestroy"),
            ("before_unmount", "beforeUnmount"),
        ]
        self._event_names += list(kwargs.keys())

    def call(self, method, *args):
        """
        Perform the call on the client

        :param method: Key used in the kwargs at construction time
        """
        self.server.js_call(self.__name, "emit", method, *args)


# -----------------------------------------------------------------------------
# TrameDeepReactive
# -----------------------------------------------------------------------------
class DeepReactive(AbstractElement):
    """Create a deeply reactive state from state variable name.
    The provided name can not be reactive.
    It needs to be statically defined in Python like in the example blow.

    This component only works with client_type="vue3".

       with DeepReactive(my_nested_var):
          html.Input(v_model=my_nested_var.txt_1)
          html.Input(v_model=my_nested_var.txt_2)
    """

    def __init__(
        self,
        name=None,
        children=None,
        **kwargs,
    ):
        super().__init__("trame-deep-reactive", children, name=name, **kwargs)
        self._attr_names += [
            "name",
        ]

        self._attributes["slot"] = f'v-slot="{{ value: {name} }}"'


# -----------------------------------------------------------------------------
# TrameLifeCycleMonitor
# -----------------------------------------------------------------------------
class LifeCycleMonitor(AbstractElement):
    """
    LifeCycleMonitor is a debug purpose tool to validate a sub-tree get the proper
    expected life cycle event.

    This component allow to print into the client side console when any of the
    monitored event happen.

    :param name: User specific text to easily identify which component the event
                was coming from.
    :param type: console[type](...) so you can use 'log', 'error', 'info', 'warn'
    :param value: Another value that is printed when an event occur
    :param events: List of events to monitor such as created, beforeMount,
        mounted, beforeUpdate, updated, beforeDestroy, destroyed
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-life-cycle-monitor", children, **kwargs)
        self._attr_names += [
            "name",
            "type",
            "value",
            "events",
        ]
        self._event_names += [
            "created",
            ("before_mount", "beforeMount"),
            "mounted",
            ("before_update", "beforeUpdate"),
            "updated",
            ("before_destroy", "beforeDestroy"),
            "destroyed",
        ]


# -----------------------------------------------------------------------------
# TrameSizeObserver
# -----------------------------------------------------------------------------
class SizeObserver(AbstractElement):
    """
    SizeObserver allow to monitor the space available in the UI and bind that
    information onto a state variable.

    :param _name: Name of the state variable to bound the component size to
    """

    def __init__(self, _name, **kwargs):
        super().__init__("trame-size-observer", **kwargs)
        self._attr_names += [
            "name",
        ]
        self.server.state[_name] = None
        self.name = self.server.translator.translate_key(_name)
