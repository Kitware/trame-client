from trame.app import get_server
from trame_client.widgets import client, html
from trame_client.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = enable_testing(get_server(client_type="vue3"), "message")
state, ctrl = server.state, server.controller


def revert_message():
    state.message = state.message[::-1]


with DivLayout(server) as layout:
    eval_js = client.JSEval(
        event=("message", "hello world"),
        exec="window.document.querySelector('.jsAlert').innerHTML = $event",
    )
    ctrl.exec = eval_js.exec
    html.Div("{{ message }}")
    html.Div("Alert", classes="jsAlert")
    html.Button("Exec", click=ctrl.exec, classes="alertMsg")
    html.Button("Exec with arg", click=(ctrl.exec, "['Yes me']"), classes="alertMe")
    html.Button("Change message", click=revert_message, classes="swapMsg")

server.start()
