from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout

server = get_server()
state, ctrl = server.state, server.controller

server.client_type = "vue2"  # default until trame>=3.x

state.count = 2
state.double = 4


@state.change("count")
def update_count(count, **kwargs):
    state.double = 2 * int(count)


with DivLayout(server) as layout:
    html.Div("count = {{ count }}")
    html.Div("2 x count = {{ double }}")
    html.Input(
        type="range",
        min=0,
        max=10,
        step=1,
        v_model="count",
    )

server.start()
