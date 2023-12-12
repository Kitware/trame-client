# Run with -d or --debug
from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html

server = get_server(client_type="vue3")

with DivLayout(server) as layout:
    html.Div(
        v_show=True,
        test=({},),
        test_1=([],),
        test_2=(5,),
        __properties=[
            "test",
            "test_1",
            "test_2",
        ],
    )
