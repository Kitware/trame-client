from trame.app import get_server
from trame.widgets import client, html
from trame.ui.html import DivLayout

server = get_server(client_type="react")
state = server.state


@state.change("main_size")
def size_changed(main_size, **kwargs):
    print(f"main_size={main_size}")


with DivLayout(server) as layout:
    layout.root.style = "height: 100vh; margin: 0; padding: 0;"
    with client.SizeObserver("main_size"):
        html.Div("{{ JSON.stringify(main_size?.size) }}")


if __name__ == "__main__":
    server.start()
