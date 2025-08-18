from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout

server = get_server()

with DivLayout(server) as layout:
    html.Div("App is running")

server.start()
