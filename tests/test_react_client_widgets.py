from trame.app import get_server
from trame.widgets import html, client, react


def test_react_jseval_ref_and_exec_event():
    server = get_server("test_react_jseval", client_type="react")

    with html.Div(trame_server=server) as root:
        client.JSEval(event="hello", ref="my_exec")

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-exec"
    assert tree["props"]["ref"] == "my_exec"
    assert tree["props"]["event"] == "hello"
    # Vue's raw `_attributes["ref"]` hack must not leak into the react tree.
    assert "onExec" not in tree["props"]


def test_react_style_binds_css_reactively():
    server = get_server("test_react_style", client_type="react")

    with html.Div(trame_server=server) as root:
        style = client.Style("body { color: red; }")

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-style"
    assert tree["props"]["css"] == {"js": style.var_name}
    assert server.state[style.var_name] == "body { color: red; }"

    style.update("body { color: blue; }")
    assert server.state[style.var_name] == "body { color: blue; }"


def test_react_script_binds_script_reactively():
    server = get_server("test_react_script", client_type="react")

    with html.Div(trame_server=server) as root:
        script = client.Script("console.log(1)", module=True)

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-script"
    assert tree["props"]["script"] == {"js": script.var_name}
    assert tree["props"]["module"] is True
    assert server.state[script.var_name] == "console.log(1)"


def test_react_client_state_change_wraps_value_in_bind():
    server = get_server("test_react_client_state_change", client_type="react")
    server.state.count = 1

    def on_change():
        pass

    with html.Div(trame_server=server) as root:
        client.ClientStateChange(
            value="count",
            trigger_on_create=True,
            change=react.Callback(on_change),
        )

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-client-state-change"
    assert tree["props"]["value"] == {"js": "count"}
    assert tree["props"]["triggerChangeOnCreate"] is True
    assert tree["props"]["onChange"] == {
        "callback": {"trigger": server.trigger_name(on_change)}
    }


def test_react_client_triggers_ref_and_custom_events():
    server = get_server("test_react_client_triggers", client_type="react")

    def on_mounted():
        pass

    def on_custom():
        pass

    with html.Div(trame_server=server) as root:
        client.ClientTriggers(
            ref="my_triggers",
            mounted=react.Callback(on_mounted),
            my_custom_event=react.Callback(on_custom),
        )

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-client-triggers"
    assert tree["props"]["ref"] == "my_triggers"
    assert tree["props"]["mounted"] == {
        "callback": {"trigger": server.trigger_name(on_mounted)}
    }
    assert tree["props"]["my_custom_event"] == {
        "callback": {"trigger": server.trigger_name(on_custom)}
    }


def test_react_life_cycle_monitor_serializes_cleanly():
    server = get_server("test_react_life_cycle_monitor", client_type="react")

    with html.Div(trame_server=server) as root:
        client.LifeCycleMonitor(name="mon", type="log", value="v")

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-life-cycle-monitor"
    assert tree["props"] == {"name": "mon", "type": "log", "value": "v"}


def test_react_size_observer_serializes_cleanly():
    server = get_server("test_react_size_observer", client_type="react")

    with html.Div(trame_server=server) as root:
        client.SizeObserver("my_size")

    tree = root.html["children"][0]
    assert tree["tag"] == "trame-size-observer"
    assert tree["props"]["name"] == "my_size"
    assert server.state.my_size is None
