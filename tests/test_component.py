import asyncio
import pytest

from trame_client.widgets.core import TrameComponent
from trame.decorators import change, controller, trigger
from trame.app import get_server

from trame.ui.html import DivLayout
from trame.widgets import html

CLIENT_TYPE = "vue3"


class TestComponent(TrameComponent):
    def __init__(self, server):
        self._steps = []
        super().__init__(server)

    def validate(self):
        assert self._steps == [
            "a changed to 1",
            "a changed to 2",
            "ctrl.b() # set",
            "ctrl.c() # add",
        ]

    @change("a")
    def on_a(self, a, **_):
        self._steps.append(f"a changed to {a}")

    @controller.set("b")
    def on_ctrl_b(self):
        self._steps.append("ctrl.b() # set")

    @controller.add("c")
    def on_ctrl_c(self):
        self._steps.append("ctrl.c() # add")

    @trigger("hello")
    def on_trigger(self): ...


class WidgetComponent(html.Div):
    def __init__(self, **kwargs):
        self._steps = []
        super().__init__(**kwargs)
        self.state.setdefault("a", 1)

        with self:
            html.Label("Hello World {{ a }}")

    def validate(self):
        assert self._steps == [
            "a changed to 1",
            "a changed to 2",
            "ctrl.b() # set",
            "ctrl.c() # add",
        ]

    @change("a")
    def on_a(self, a, **_):
        self._steps.append(f"a changed to {a}")

    @controller.set("b")
    def on_ctrl_b(self):
        self._steps.append("ctrl.b() # set")

    @controller.add("c")
    def on_ctrl_c(self):
        self._steps.append("ctrl.c() # add")

    @trigger("hello")
    def on_trigger(self): ...


@pytest.mark.asyncio
async def test_component():
    server = get_server("test_component", client_type=CLIENT_TYPE)
    server.state.a = 1

    component = TestComponent(server)

    server.state.ready()
    await asyncio.sleep(0.1)

    with server.state:
        server.state.a = 2

    component.ctrl.b()
    component.ctrl.c()

    assert server.trigger_name(component.on_trigger) == "hello"

    await asyncio.sleep(0.1)

    component.validate()


@pytest.mark.asyncio
async def test_widget_as_component():
    server = get_server("test_widget_as_component", client_type=CLIENT_TYPE)

    with DivLayout(server) as layout:
        WidgetComponent(ctx_name="test_comp")

    assert (
        layout.html
        == """<div >
<div >
<label >
Hello World {{ a }}
</label>
</div>
</div>"""
    )

    server.state.ready()
    await asyncio.sleep(0.1)

    with server.state:
        server.state.a = 2

    server.controller.b()
    server.controller.c()

    assert server.trigger_name(server.context.test_comp.on_trigger) == "hello"

    await asyncio.sleep(0.1)

    server.context.test_comp.validate()
