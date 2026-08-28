import json

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html
from trame_client.utils.react import parse_directive_key, parse_v_for, split_text

CLIENT_TYPE = "react"


def test_split_text():
    assert split_text("hello") == ["hello"]
    assert split_text("{{ count }}") == [{"expr": "count"}]
    assert split_text("a {{ b }} c") == ["a ", {"expr": "b"}, " c"]
    assert split_text("{{ a }}{{ b + 1 }}") == [{"expr": "a"}, {"expr": "b + 1"}]


def test_parse_v_for():
    assert parse_v_for("item in items") == {
        "item": "item",
        "index": None,
        "source": "items",
    }
    assert parse_v_for("(it, i) in items") == {
        "item": "it",
        "index": "i",
        "source": "items",
    }
    assert parse_v_for("x of list.filter(v => v)") == {
        "item": "x",
        "index": None,
        "source": "list.filter(v => v)",
    }


def test_parse_directive_key():
    assert parse_directive_key("v-if") == ("if", None, [])
    assert parse_directive_key("v-model.lazy") == ("model", None, ["lazy"])
    assert parse_directive_key("v-model:hello.world") == ("model", "hello", ["world"])
    assert parse_directive_key("v-slot:name") == ("slot", "name", [])


def test_react_node_properties():
    server = get_server("test_react_node_properties", client_type=CLIENT_TYPE)
    widget = html.Div(
        trame_server=server,
        v_model_hello="world",
        v_bind_hello="world",
        id="static-id",
        classes="a b",
        tabindex=1,
    )
    node = widget.react_node
    assert node["tag"] == "div"
    assert node["attrs"] == {"id": "static-id", "class": "a b", "tabindex": 1}
    assert node["props"] == {"hello": "world"}
    assert node["dirs"]["models"] == [
        {"arg": "hello", "modifiers": [], "expr": "world"}
    ]


def test_react_node_events():
    server = get_server("test_react_node_events", client_type=CLIENT_TYPE)

    def on_click(*_):
        pass

    widget = html.Div(
        trame_server=server,
        click="count++",
        v_on_mouseout_left_stop="handler",
        mousedown=(on_click, "[count]"),
    )
    node = widget.react_node
    assert node["on"]["click"] == "count++"
    assert node["on"]["mouseout.left.stop"] == "handler"
    assert node["on"]["mousedown"].startswith("trigger('")
    assert node["on"]["mousedown"].endswith("', [count])")


def test_react_node_directives_and_children():
    server = get_server("test_react_node_directives", client_type=CLIENT_TYPE)
    with html.Div(trame_server=server, v_if=("show", True)) as root:
        html.Span("value: {{ count }}", v_show="count > 0")
        html.Li(v_for="(it, i) in items", key="i")

    node = root.react_node
    assert node["dirs"]["if"] == "show"
    span, li = node["children"]
    assert span["dirs"]["show"] == "count > 0"
    assert span["children"] == ["value: ", {"expr": "count"}]
    assert li["dirs"]["for"] == {"item": "it", "index": "i", "source": "items"}
    assert li["props"] == {"key": "i"}
    # tuple default registered in state
    assert server.state["show"] is True


def test_layout_flush_react_payload():
    server = get_server("test_layout_flush_react", client_type=CLIENT_TYPE)
    with DivLayout(server):
        html.Button("Go", click="go()")

    payload = json.loads(server.state["trame__template_main"])
    assert payload["version"] == 1
    assert payload["root"]["tag"] == "div"
    button = payload["root"]["children"][0]
    assert button["tag"] == "button"
    assert button["on"] == {"click": "go()"}
    assert button["children"] == ["Go"]


def test_r_star_aliases():
    server = get_server("test_r_star_aliases", client_type=CLIENT_TYPE)
    with html.Div(trame_server=server, r_if=("visible", True)) as root:
        html.Span(r_show="count > 0")
        html.Li(r_for="(it, i) in items", key="i")
        html.Input(r_model="name_var")
        html.Input(r_model_number="count")
        html.Button(r_on_click_stop="count++")

    node = root.react_node
    span, li, input1, input2, button = node["children"]
    assert node["dirs"]["if"] == "visible"
    assert span["dirs"]["show"] == "count > 0"
    assert li["dirs"]["for"] == {"item": "it", "index": "i", "source": "items"}
    assert input1["dirs"]["models"] == [
        {"arg": None, "modifiers": [], "expr": "name_var"}
    ]
    assert input2["dirs"]["models"] == [
        {"arg": None, "modifiers": ["number"], "expr": "count"}
    ]
    assert button["on"]["click.stop"] == "count++"


def test_direct_attribute_capture():
    # Widgets like trame-vtk write formatted attributes into _attributes
    server = get_server("test_direct_attr_capture", client_type=CLIENT_TYPE)
    widget = html.Div(trame_server=server)
    widget._attributes["ref"] = 'ref="view_1"'
    widget._attributes["view_id"] = ':viewId="view_1Id"'
    widget._attributes["evt"] = '@resize="onResize()"'
    node = widget.react_node
    assert node["attrs"]["ref"] == "view_1"
    assert node["props"]["viewId"] == "view_1Id"
    assert node["on"]["resize"] == "onResize()"


def test_vue_html_untouched_by_capture():
    # Same widget built for vue3 must serialize to the exact same HTML string
    server = get_server("test_vue_html_untouched", client_type="vue3")
    widget = html.Div(
        trame_server=server,
        v_model_hello="world",
        v_bind_hello="world",
    )
    assert widget.html == '<div v-model:hello="world" :hello="world" />'
