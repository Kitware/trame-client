from trame.app import get_server
from trame.widgets import html

from trame_client.widgets.core import VirtualNode


def test_vue_virtual_node_renders_template_string():
    server = get_server("test_vue_virtual_node", client_type="vue3")
    node = VirtualNode(server)
    with node:
        html.Div("hello")

    assert node.html.strip() == "<div >\nhello\n</div>"


def test_react_virtual_node_renders_fragment():
    server = get_server("test_react_virtual_node", client_type="react")
    node = VirtualNode(server)
    with node:
        html.Div("hello")

    assert node.html == {
        "tag": "ReactFragment",
        "props": {},
        "children": [{"tag": "div", "props": {}, "children": ["hello"]}],
    }
