from trame.app import get_server
from trame.widgets import html


class MyDiv(html.Div):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._rw = "initial value"

    @property
    def secret(self):
        return "my secret"

    @property
    def rw(self):
        return self._rw

    @rw.setter
    def rw(self, v):
        print("exec setter")
        self._rw = v


def test_component_setter():
    server = get_server("test_component_props")
    w = MyDiv(trame_server=server)
    assert w.secret == "my secret"
    assert w.rw == "initial value"
    w.rw = "hello new value"
    assert w.rw == "hello new value"
