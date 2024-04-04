from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import client, html

server = get_server(client_type="vue2")


@server.state.change("first_size")
def on_size(first_size, **kwargs):
    print(first_size)


with DivLayout(server) as layout:
    layout.root.style = "height: 100vh; width: 100%; padding: 0; margin: 0;"

    with html.Div(
        style="width: 40vw; height: 40vh; border: solid 1px #333; margin: 25px;"
    ):
        with client.SizeObserver("first_size"):
            html.Div(
                "{{ first_size?.size.width.toFixed(1) }} x {{ first_size?.size.height.toFixed(1) }}",
                style="margin: 0 auto; height: 100%; text-align: middle;",
            )

    with html.Div(
        style="width: 20vw; height: 30vh; border: solid 1px #333; position: absolute; right: 10px; bottom: 10px"
    ):
        with client.SizeObserver("second_size"):
            html.Div(
                "{{ second_size?.size.width.toFixed(1) }} x {{ second_size?.size.height.toFixed(1) }}",
                style="margin: 0 auto; height: 100%; text-align: middle;",
            )


if __name__ == "__main__":
    server.start()
