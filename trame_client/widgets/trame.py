from .core import AbstractElement

__all__ = [
    "Connect",
    "Loading",
    "ServerTemplate",
    "StateResolver",
]

# -----------------------------------------------------------------------------
# TrameApp
# -----------------------------------------------------------------------------
# SKIP: built-in client not to be use within a server template

# -----------------------------------------------------------------------------
# TrameConnect
# -----------------------------------------------------------------------------
class Connect(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("trame-connect", children, **kwargs)
        self._attr_names += [
            "name",
            "config",
            ("use_url", "useUrl"),
        ]
        self._event_names += [
            ("trame_template_change", "trameTemplateChange"),
            ("state_change", "stateChange"),
        ]


# -----------------------------------------------------------------------------
# TrameLoading
# -----------------------------------------------------------------------------
class Loading(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("trame-loading", children, **kwargs)
        self._attr_names += [
            "message",
        ]


# -----------------------------------------------------------------------------
# TrameServerTemplate
# -----------------------------------------------------------------------------
class ServerTemplate(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("trame-server-template", children, **kwargs)
        self._attr_names += [
            ("name", "templateName"),
            ("use_url", "useUrl"),
            ("url_key", "urlKey"),
        ]


# -----------------------------------------------------------------------------
# TrameStateResolver
# -----------------------------------------------------------------------------
class StateResolver(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("trame-state-resolver", children, **kwargs)
        self._attr_names += [
            "names",
        ]
