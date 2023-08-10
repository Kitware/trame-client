from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html

server = get_server()

# Test to dynamically add a fake directive
html.Div.register_directive("v_seb_directive")

with DivLayout(server) as layout:
    with html.Div(v_seb_directive=True):
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
