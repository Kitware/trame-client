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
    """
    Container managing the handshake and connection to a trame server

    :param name: Application name
    :type name: str

    :param config: Dict object capturing all the key/value pair needed to start
                   or configure the connection.
    :type name: {}

    :param use_url: Should we process the URL to extend the connection config
    :type use_url: bool

    :param trame_template_change: Event notification when a template has changed
    :param state_change: Event notification when something in the state has changed
    """

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
    """Provide means to extract sub-state for its slots"""

    def __init__(self, children=None, **kwargs):
        super().__init__("trame-state-resolver", children, **kwargs)
        self._attr_names += [
            "names",
        ]
