from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.count = 1


@ctrl.set("update_ui")
def update_ui():
    state.count += 1
    with DivLayout(server):
        html.Div(f"Static text {state.count}")
        html.Div("count = {{ count }}")
        html.Div("tts = {{ tts }}")
        html.Button("Update template", click=ctrl.update_ui)
        html.Button("count++", click="count++")


update_ui()
server.start()
