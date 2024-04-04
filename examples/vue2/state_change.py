import os
from trame.app import get_server
from trame.widgets import client, html
from trame.ui.html import DivLayout

server = get_server(client_type="vue2")


def a_changed():
    print(f"a={server.state.a}")


with DivLayout(server) as layout:
    html.Div("{{ a }}")
    html.Input(type="range", v_model=("a", 1))
    client.ClientStateChange(value="a", change=a_changed)


if __name__ == "__main__":
    server.start()
