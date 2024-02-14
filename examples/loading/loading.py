import os
from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout
import time

server = get_server(client_type=os.environ.get("TRAME_CLIENT_TYPE", "vue3"))

# -----------------------------------------------------------------------------
# Only with Vue3
# -----------------------------------------------------------------------------
with DivLayout(server, template_name="error") as layout:
    html.Div("App disconnected: {{ trame_error_report_msg }}")

with DivLayout(server, template_name="error_reconnect") as layout:
    html.Div("App disconnected but you can reconnect: {{ trame_error_report_msg }}")
# -----------------------------------------------------------------------------

with DivLayout(server) as layout:
    html.Div("App is fully loaded")

# Busy wait
time.sleep(5)

server.start()
