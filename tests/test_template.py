from trame.app import get_server
from trame_client.widgets.html import Div

CLIENT_TYPE = "vue3"


def test_properties():
    server = get_server("test_properties", client_type=CLIENT_TYPE)
    widget = Div(
        trame_server=server,
        v_model_hello="world",
        v_model_hello_world="something",
        v_bind_hello="world",
        v_bind_hello_world="something",
        v_model_number="number_value",
    )
    assert widget.html == (
        "<div "
        'v-model:hello="world" '
        'v-model:hello.world="something" '
        ':hello="world" '
        ':hello.world="something" '
        'v-model.number="number_value" '
        "/>"
    )


def test_events():
    server = get_server("test_events", client_type=CLIENT_TYPE)
    widget = Div(
        trame_server=server,
        v_on_click="click",
        v_on_mouseenter_left="left",
        v_on_mouseout_left_stop="left_stop",
    )
    assert widget.html == (
        '<div @click="click" @mouseenter.left="left" @mouseout.left.stop="left_stop" />'
    )
