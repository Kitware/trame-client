from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

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
        v_model_number="count",
        __properties=[("v_model_number", "v-model.number")],
    )

server.start()
