from trame.app import TrameApp
from trame.widgets import html, react, client
from trame.ui.html import DivLayout
from trame.decorators import change


class TestReact(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")

        self.state.todos = ["Write docs", "Review PR", "Ship it"]

        with DivLayout(self.server) as self.ui:
            html.Div(["count = ", react.Bind("count", count=2)])
            html.Input(
                type="range",
                min=0,
                max=10,
                step=1,
                value=react.Bind("count", count=2),
                on_change=react.Callback("count = Number(e.target.value)"),
            )
            html.Button("Reset", on_click=react.Callback(self.reset))
            html.Input(
                value=react.Bind("text", text="Hello world"),
                on_change=react.Callback("text = e.target.value"),
            )
            html.Button("Add todo", on_click=react.Callback(self.add_todo, "[text]"))

            with react.If(value="todos.length > 0"):
                with html.Ul():
                    with react.For(items="todos", name="todo"):
                        html.Li([react.Bind("todo")], key=react.Bind("todo"))

            with react.If(value="todos.length == 0"):
                html.Div("No todos...")

            html.Hr()
            client.ServerTemplate(name="subview")
            html.Hr()

            html.A("Go to view 2", href="/?ui=view2")

        with DivLayout(self.server, template_name="view2"):
            html.Div("Yes it is still me")
            html.A("Go home", href="/")

        with DivLayout(self.server, template_name="subview"):
            html.Div("From a SubView")
            with html.Ul():
                for i in range(10):
                    html.Li(f"Sub view item {i}")

    def reset(self, value=2):
        self.state.count = value

    def add_todo(self, value):
        self.state.todos.append(value)
        self.state.dirty("todos")
        self.state.count += 1

    @change("count")
    def _on_count(self, count, **_):
        while len(self.state.todos) > count:
            self.state.todos.pop()
        while len(self.state.todos) < count:
            self.state.todos.append(f"Item {len(self.state.todos)}")

        self.state.dirty("todos")


def main():
    app = TestReact()
    app.server.start()


if __name__ == "__main__":
    main()
