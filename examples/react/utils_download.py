from trame.app import TrameApp
from trame.widgets import html, react
from trame.ui.html import DivLayout


class UtilsDownloadReact(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")

        self.state.content = "Hello from trame!"

        with DivLayout(self.server) as self.ui:
            html.Textarea(
                value=react.Bind("content"),
                on_change=react.Callback("content = $event.target.value"),
                rows=5,
                style={"width": "100%"},
            )
            html.Button(
                "Download as .txt",
                on_click=react.Callback(
                    "trame.utils.download('trame-export.txt', content, 'text/plain')"
                ),
            )


def main():
    app = UtilsDownloadReact()
    app.server.start()


if __name__ == "__main__":
    main()
