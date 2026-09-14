from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html, react

from trame_client.utils.testing import enable_testing
from trame_client.widgets.core import VirtualNode

server = get_server(client_type="react")
state = server.state

state.count = 1

# React analogue of `examples/vue2/dynamic_template.py`: a VirtualNode is
# cleared and refilled, then re-flushed into the layout template.
dynamic = VirtualNode(server)


def update_ui():
    state.count += 1
    with dynamic.clear():
        html.Div(f"Static text {state.count}", classes="staticDiv")
        html.Div(["count = ", react.Bind("count")], classes="countDiv")


with DivLayout(server) as layout:
    html.Button(
        "Update template",
        classes="updateBtn",
        on_click=react.Callback(update_ui),
    )
    html.Button(
        "count++",
        classes="plusBtn",
        on_click=react.Callback("count++"),
    )
    dynamic(layout)

update_ui()

enable_testing(server, "count")
server.start()
