from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
server.state.count = 1

with DivLayout(server):
    html.Div(
        "{{ count }}",
        classes="countValue",
        style="padding: 20px; background: red;",
    )
    html.Button("Add to count", classes="plusButton", click="count++")

enable_testing(server, "count")
server.start()
