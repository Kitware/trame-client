from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.count = 1


@ctrl.set("update_ui")
def update_ui():
    state.count += 1
    with DivLayout(server):
        html.Div(f"Static text {state.count}", classes="staticDiv")
        html.Div("count = {{ count }}", classes="countDiv")
        html.Div("tts = {{ tts }}", classes="ttsDiv")
        html.Button("Update template", click=ctrl.update_ui, classes="updateBtn")
        html.Button("count++", click="count++", classes="plusBtn")


update_ui()
enable_testing(server, "count")
server.start()
