from trame.app import get_server
from trame.widgets import html, client
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue2"
state, ctrl = server.state, server.controller


def revert_message():
    state.message = state.message[::-1]


# Default UI
with DivLayout(server):
    client.Style(".myRedBG { background: red; } body { margin: 0; }")
    client.ServerTemplate(
        name="loading",
        style="width: 50vw; height: 100vh; position: absolute; left: 0%;",
    )
    client.ServerTemplate(
        name="redSide",
        style="width: 50vw; height: 100vh; position: absolute; left: 50%;",
    )


# ?ui=loading
with DivLayout(server, template_name="loading"):
    client.Loading(message="Yes the loading guy...")

# ?ui=redSide
with DivLayout(server, template_name="redSide"):
    with html.Div(
        "The red side...", classes="myRedBG", style="width: 100%; height: 100%;"
    ):
        eval_js = client.JSEval(
            event=("message", "hello world"),
            exec="alert($event)",
        )
        ctrl.exec = eval_js.exec
        html.Div("{{ message }}")
        html.Button("Exec", click=ctrl.exec)
        html.Button("Exec with arg", click=(ctrl.exec, "['Yes me']"))
        html.Button("Change message", click=revert_message)

server.start()
