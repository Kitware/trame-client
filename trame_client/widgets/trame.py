from .core import AbstractElement

__all__ = [
    "Loading",
    "ServerTemplate",
    "Style",
    "JSEval",
    "Getter",
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

    def __init__(self, css_content=None, **kwargs):
        super().__init__("trame-style", **kwargs)
        self._key = f"trame__inline_style_{self._id}"
        self._attributes["_css"] = f':css="{self._key}"'
        self.server.state.setdefault(self._key, css_content)

    def update(self, css_content):
        """Update style content"""
        self.server.state[self._key] = css_content

    @property
    def var_name(self):
        """Name the the state variable used by this widget"""
        return self._key


# -----------------------------------------------------------------------------
# TrameGetter
# -----------------------------------------------------------------------------
class Getter(AbstractElement):
    """Provide means to extract a reactive state variable from its name"""

    def __init__(self, children=None, value_name=None, **kwargs):
        super().__init__("trame-getter", **kwargs)
        self._attr_names += [
            "name",
        ]
        if value_name:
            self._attributes["slot"] = f'v-slot="{{ value: {value_name} }}"'
        else:
            self._attributes["slot"] = 'v-slot="{ value }"'
