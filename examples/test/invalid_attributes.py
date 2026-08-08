# run it with --debug
from trame.app import get_server
from trame.widgets import html

print(
    html.Div(
        trame_server=get_server(),
        a="Wrong",
        title="ok",
        another_wrong="wrong attr",
        made="up",
        clickable="clicked",
        __properties=["made"],
        __events=["clickable"],
    ).html
)

print(
    html.Span(
        trame_server=get_server(),
        title="all good",
    ).html
)
