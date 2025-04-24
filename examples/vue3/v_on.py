from trame_client.widgets import html
from trame.app import get_server

server = get_server()
print(html.Div(trame_server=server, v_on_click_left_stop_self="hello"))
