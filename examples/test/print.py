from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html

server = get_server()

with DivLayout(server) as layout:
    with html.Div():
        with html.Div():
            with html.Div(
                style="border: 1px;",
                classes=("dynaClass", {}),
            ) as sub_container:
                html.Span("Hello")

            print("=" * 60)
            print("widget")
            print("=" * 60)
            print(sub_container)

            html.Span("world")
        html.Span("What's")
    html.Span("Up")

    print("=" * 60)
    print("Full layout")
    print("=" * 60)
    print(layout)
