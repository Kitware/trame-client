from trame.app import get_server
from trame.widgets import html


def test_widget_kwargs():
    server = get_server("test_widget_kwargs")
    div = html.Div(
        trame_server=server, a="a", title="b", something_that_does_not_exist="c"
    )
    assert div.html == """<div title="b" />"""
    assert div.skipped_attributes == {"a", "something_that_does_not_exist"}
