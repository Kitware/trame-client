from trame_client.widgets import html
from trame.app import get_server

server = get_server(client_type="react")
print(html.Div(trame_server=server, r_on_click_left_stop_self="hello").react_node)
