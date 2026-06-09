from .core import AbstractLayout
from ..widgets.html import Div

__all__ = [
    "DivLayout",
]


class DivLayout(AbstractLayout):
    def __init__(
        self,
        _server,
        template_name="main",
        connect_parent=True,
        style=None,
        classes=None,
        **kwargs,
    ):
        """
        Simple <div> element as a layout

        :param _server: Server to bound the layout to
        :param template_name: Name of the template (default: main)
        :param connect_parent: Control registration to parent context manager
        :param style: Forwarded to root Div element
        :param classes: Forwarded to root Div element
        :param **kwargs: Optional arguments pass to the <Div> element
        """
        super().__init__(
            _server,
            Div(
                trame_server=_server,
                connect_parent=connect_parent,
                style=style,
                classes=classes,
            ),
            template_name=template_name,
            **kwargs,
        )
