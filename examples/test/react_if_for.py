from trame.app import get_server
from trame.widgets import html, react
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
server.state.count = 2
server.state.todos = ["Write docs", "Review PR", "Ship it"]


def reset(value=2):
    server.state.count = value


def clear_todos():
    server.state.todos = []


with DivLayout(server) as layout:
    html.Div([react.Bind("count")], classes="countValue")
    html.Input(
        type="range",
        min=0,
        max=10,
        step=1,
        classes="countSlider",
        value=react.Bind("count"),
        on_change=react.Callback("count = Number(e.target.value)"),
    )
    html.Button("Reset", classes="resetButton", on_click=react.Callback(reset))
    html.Button(
        "Clear todos", classes="clearButton", on_click=react.Callback(clear_todos)
    )
    with react.If(value="todos.length > 0"):
        with html.Ul(classes="todoList"):
            with react.For(items="todos", name="todo"):
                html.Li(
                    [react.Bind("todo")], classes="todoItem", key=react.Bind("todo")
                )
    with react.If(value="todos.length === 0"):
        html.Div("No todos left", classes="emptyMsg")

enable_testing(server, "count", "todos")
server.start()
