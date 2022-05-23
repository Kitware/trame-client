from .core import AbstractLayout
from ..widgets.html import Div

__all__ = [
    "DivLayout",
]


class DivLayout(AbstractLayout):
    def __init__(self, _server, template_name="main", **kwargs):
        """
        Simple <div> element as a layout

        :param _server: Server to bound the layout to
        :param template_name: Name of the template (default: main)
        :param **kwargs: Optional arguments pass to the <Div> element
        """
        super().__init__(
            _server, Div(trame_server=_server), template_name=template_name, **kwargs
        )
