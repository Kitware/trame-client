from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
state = server.state

state.count = 2
state.double = 4


@state.change("count")
def update_count(count, **kwargs):
    state.double = 2 * int(count)


with DivLayout(server):
    html.Div("count = {{ count }}", classes="countValue")
    html.Div("2 x count = {{ double }}", classes="doubleValue")
    html.Input(
        type="range",
        min=0,
        max=10,
        step=1,
        r_model_number="count",
        __properties=[("r_model_number", "v-model.number")],
    )

enable_testing(server, "count", "double")
server.start()
