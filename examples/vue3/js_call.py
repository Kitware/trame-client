from trame.app import get_server
from trame.widgets import client, html
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller


def revert_message():
    state.message = state.message[::-1]


with DivLayout(server) as layout:
    eval_js = client.JSEval(
        event=("message", "hello world"),
        exec="window.alert($event)",
    )
    ctrl.exec = eval_js.exec
    html.Div("{{ message }}")
    html.Button("Exec", click=ctrl.exec)
    html.Button("Exec with arg", click=(ctrl.exec, "['Yes me']"))
    html.Button("Change message", click=revert_message)

    # print(layout.html)

server.start()
