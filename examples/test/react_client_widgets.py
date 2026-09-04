from trame.app import get_server
from trame.widgets import html, client, react
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
server.state.mounted_count = 0


def on_mounted():
    server.state.mounted_count += 1


with DivLayout(server) as layout:
    client.Style("body { margin: 0; } .sizeBox { background: red; }")
    client.ClientTriggers(ref="triggers1", mounted=react.Callback(on_mounted))
    html.Div([react.Bind("mounted_count")], classes="mountedCount")
    with client.SizeObserver("box_size"):
        html.Div(classes="sizeBox", style={"width": "200px", "height": "100px"})

enable_testing(server, "mounted_count", "box_size")
server.start()
