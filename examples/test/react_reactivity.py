from trame.app import get_server
from trame.widgets import html, react
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
server.state.count = 1

with DivLayout(server) as layout:
    html.Div(
        react.Bind("count"),
        classes="countValue",
        style={"padding": "20px", "background": "red"},
    )
    html.Button(
        "Add to count",
        classes="plusButton",
        on_click=react.Callback("count++"),
    )

enable_testing(server, "count")
server.start()
