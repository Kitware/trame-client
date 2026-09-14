import uuid

import pytest
from trame.app import get_server
from trame.widgets import react

from trame_client.widgets.adapter import VUE_TO_REACT_EVENT_NAMES, ClientAdapter
from trame_client.widgets.react import SHARED_EVENTS as REACT_SHARED_EVENTS


def _server(client_type: str):
    return get_server(f"test_client_adapter_{uuid.uuid4()}", client_type=client_type)


def _adapter(client_type: str) -> ClientAdapter:
    return ClientAdapter(_server(client_type))


def _handler(*_args):
    return None


def test_vue_adapter_renders_a_css_style_string():
    adapter = _adapter("vue3")

    assert (
        adapter.style({"background-color": "black", "flex-grow": "1"})
        == "background-color: black; flex-grow: 1;"
    )


def test_vue_adapter_also_accepts_camel_case_keys():
    adapter = _adapter("vue3")

    assert adapter.style({"backgroundColor": "black"}) == "background-color: black;"


def test_react_adapter_camel_cases_the_style_keys():
    adapter = _adapter("react")

    assert adapter.style({"background-color": "black", "flex-grow": "1"}) == {
        "backgroundColor": "black",
        "flexGrow": "1",
    }


def test_vue_adapter_uses_the_dom_event_name():
    adapter = _adapter("vue3")

    assert adapter.event("mouseenter", _handler) == {"mouseenter": _handler}


def test_vue_adapter_uses_the_bubbling_focus_event_names():
    adapter = _adapter("vue3")

    assert adapter.event("focusin", _handler) == {"focusin": _handler}
    assert adapter.event("focusout", _handler) == {"focusout": _handler}


def test_react_adapter_maps_bubbling_focus_events():
    adapter = _adapter("react")

    assert set(adapter.event("focusin", _handler)) == {"on_focus"}
    assert set(adapter.event("focusout", _handler)) == {"on_blur"}


def test_vue_adapter_applies_event_modifiers():
    adapter = _adapter("vue3")

    assert adapter.event("click", _handler, modifiers=["stop", "prevent"]) == {
        "v_on_click_stop_prevent": _handler
    }


def test_react_adapter_applies_event_modifiers():
    adapter = _adapter("react")

    result = adapter.event("click", _handler, modifiers=["prevent"])

    assert list(result) == ["on_click"]
    assert result["on_click"].modifiers == ["prevent"]


def test_react_adapter_maps_animation_and_transition_events():
    adapter = _adapter("react")

    assert set(
        adapter.events(
            animationstart=_handler,
            animationend=_handler,
            animationiteration=_handler,
            transitionend=_handler,
        )
    ) == {
        "on_animation_start",
        "on_animation_end",
        "on_animation_iteration",
        "on_transition_end",
    }


def test_react_event_map_matches_the_react_renderer():
    react_event_kwargs = {
        name if isinstance(name, str) else name[0] for name in REACT_SHARED_EVENTS
    }
    assert set(VUE_TO_REACT_EVENT_NAMES.values()) == react_event_kwargs


def test_react_adapter_wraps_the_event_callback():
    server = _server("react")
    adapter = ClientAdapter(server)

    result = adapter.event("mouseenter", _handler)

    assert list(result) == ["on_mouse_enter"]
    assert result["on_mouse_enter"].to_json(server) == {
        "callback": {"trigger": server.trigger_name(_handler)}
    }


def test_react_adapter_maps_several_events():
    adapter = _adapter("react")

    assert set(adapter.events(click=_handler, mouseleave=_handler)) == {
        "on_click",
        "on_mouse_leave",
    }


def test_react_adapter_rejects_an_unknown_event():
    adapter = _adapter("react")

    with pytest.raises(ValueError, match="not_an_event"):
        adapter.event("not_an_event", _handler)


def test_adapter_expression_is_client_specific():
    assert _adapter("vue3").expression("count + 1") == ("count + 1",)
    assert isinstance(_adapter("react").expression("count + 1"), react.Bind)


def test_vue_dynamic_style_becomes_a_bound_style_object():
    adapter = _adapter("vue3")

    style = adapter.style(
        {
            "position": "relative",
            "width": "100%",
            "cursor": adapter.expression("`${active_view_cursor}`"),
        }
    )

    assert style == (
        "{position: 'relative', width: '100%', cursor: `${active_view_cursor}`}",
    )


def test_vue_dynamic_style_camel_cases_bound_keys():
    adapter = _adapter("vue3")

    style = adapter.style(
        {"background-color": adapter.expression("color"), "width": "100%"}
    )

    assert style == ("{backgroundColor: color, width: '100%'}",)


def test_adapter_resolves_the_server_from_the_active_widget_context():
    from trame.widgets import html

    server = _server("react")

    with html.Div(trame_server=server):
        adapter = ClientAdapter()

    assert adapter.server is server


def test_adapter_is_exposed_from_the_client_widget_module():
    from trame.widgets import client

    assert client.ClientAdapter is ClientAdapter
