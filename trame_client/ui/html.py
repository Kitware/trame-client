from .core import AbstractLayout
from ..widgets.html import Div


class DivLayout(AbstractLayout):
    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(
            _server, Div(trame_server=_server), template_name=template_name, **kwargs
        )
