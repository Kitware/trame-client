from trame.app import get_server
from trame.widgets import html, react

from trame_client.utils.defaults import TrameDefault
from trame_client.widgets.core import AbstractElement


def test_react_bind_and_callback():
    server = get_server("test_react_bind_and_callback", client_type="react")

    def reset(value=2):
        server.state.count = value

    with html.Div(trame_server=server) as root:
        html.Div(["count = ", react.Bind("count", count=2)])
        html.Input(
            type="range",
            min=0,
            max=10,
            step=1,
            value=react.Bind("count", count=2),
            on_change=react.Callback("count = Number(e.target.value)"),
            on_double_click=react.Callback("count = 2 * count", modifiers=["prevent"]),
        )
        html.Button("Reset", on_click=react.Callback(reset))
        html.Button("Reset 4", on_click=react.Callback(reset, args="[4]", kwargs="{}"))

    assert server.state.count == 2

    tree = root.html
    assert tree == {
        "tag": "div",
        "props": {},
        "children": [
            {
                "tag": "div",
                "props": {},
                "children": ["count = ", {"js": "count"}],
            },
            {
                "tag": "input",
                "props": {
                    "type": "range",
                    "min": 0,
                    "max": 10,
                    "step": 1,
                    "value": {"js": "count"},
                    "onChange": {"callback": {"js": "count = Number(e.target.value)"}},
                    "onDoubleClick": {
                        "callback": {"js": "count = 2 * count"},
                        "modifiers": ["prevent"],
                    },
                },
                "children": [],
            },
            {
                "tag": "button",
                "props": {
                    "onClick": {"callback": {"trigger": server.trigger_name(reset)}}
                },
                "children": ["Reset"],
            },
            {
                "tag": "button",
                "props": {
                    "onClick": {
                        "callback": {
                            "trigger": server.trigger_name(reset),
                            "args": {"js": "[4]"},
                            "kwargs": {"js": "{}"},
                        }
                    }
                },
                "children": ["Reset 4"],
            },
        ],
    }


def test_react_if_and_for():
    server = get_server("test_react_if_and_for", client_type="react")
    server.state.todos = ["Write docs", "Review PR", "Ship it"]

    with html.Div(trame_server=server) as root:
        with react.If(value="todos.length > 0"):
            with html.Ul():
                with react.For(items="todos", name="todo"):
                    html.Li([react.Bind("todo")], key=react.Bind("todo"))

        with react.If(value="todos.length === 0"):
            html.Div("Nothing left to do!")

    tree = root.html
    assert tree["children"][0] == {
        "tag": "ReactIf",
        "props": {"value": {"js": "todos.length > 0"}},
        "children": [
            {
                "tag": "ul",
                "props": {},
                "children": [
                    {
                        "tag": "ReactFor",
                        "props": {"items": {"js": "todos"}, "name": "todo"},
                        "children": [
                            {
                                "tag": "li",
                                "props": {"key": {"js": "todo"}},
                                "children": [{"js": "todo"}],
                            }
                        ],
                    }
                ],
            }
        ],
    }
    assert tree["children"][1] == {
        "tag": "ReactIf",
        "props": {"value": {"js": "todos.length === 0"}},
        "children": [{"tag": "div", "props": {}, "children": ["Nothing left to do!"]}],
    }


def test_react_classes_maps_to_class_name():
    server = get_server("test_react_classes_maps_to_class_name", client_type="react")
    div = html.Div(trame_server=server, classes="my-item")
    assert div.html["props"] == {"className": "my-item"}


def test_react_slot():
    server = get_server("test_react_slot", client_type="react")

    class VDataTable(AbstractElement):
        def __init__(self, **kwargs):
            super().__init__("VDataTable", trame_server=server, **kwargs)
            self._attr_names += ["items", "renderItemName"]

    with html.Div(trame_server=server) as root:
        with react.Slot(params=["item"]) as render_item_name:
            html.Strong(react.Bind("item.name"))

        VDataTable(items=react.Bind("items"), renderItemName=render_item_name)

    # Slot must not also be auto-attached as a visible child: its only
    # attachment point is the renderItemName= prop it's explicitly passed to.
    assert len(root.children) == 1

    tree = root.html
    assert tree["children"][0] == {
        "tag": "VDataTable",
        "props": {
            "items": {"js": "items"},
            "renderItemName": {
                "slot": {
                    "params": ["item"],
                    "children": [
                        {
                            "tag": "strong",
                            "props": {},
                            "children": [{"js": "item.name"}],
                        }
                    ],
                }
            },
        },
        "children": [],
    }


def test_react_skipped_attributes():
    server = get_server("test_react_skipped_attributes", client_type="react")
    div = html.Div(
        trame_server=server, a="a", title="b", something_that_does_not_exist="c"
    )
    assert div.html["props"] == {"title": "b"}
    assert div.skipped_attributes == {"a", "something_that_does_not_exist"}


def test_react_hide_merges_with_existing_style():
    server = get_server(
        "test_react_hide_merges_with_existing_style", client_type="react"
    )
    div = html.Div(trame_server=server, style={"color": "red"})
    div.hide()
    assert div.html["props"]["style"] == {"color": "red", "display": "none"}


def test_react_bind_applies_trame_default():
    server = get_server("test_react_bind_applies_trame_default", client_type="react")
    div = html.Div(trame_server=server, title=react.Bind("t", t=TrameDefault(x=1)))
    _ = div.html
    assert server.state.x == 1


def test_react_tts_sensitive_is_a_noop():
    server = get_server("test_react_tts_sensitive_is_a_noop", client_type="react")
    div = html.Div(trame_server=server)
    before = div.html
    div.ttsSensitive()
    after = div.html
    assert before == after
