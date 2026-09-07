from trame.app import TrameApp
from trame.widgets import html, react
from trame.ui.html import DivLayout


class DynamicStyleReact(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")

        with DivLayout(self.server) as self.ui:
            html.Div(
                "Dynamic style",
                style={
                    "fontWeight": "bold",
                    "color": react.Bind("color", color="red"),
                },
            )
            html.Input(
                value=react.Bind("color", color="red"),
                on_change=react.Callback("color = $event.target.value"),
            )


def main():
    app = DynamicStyleReact()
    app.server.start()


if __name__ == "__main__":
    main()
