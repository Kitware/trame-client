from trame.app import get_server
from trame.widgets import html, client
from trame.ui.html import DivLayout

server = get_server()

JS_CONTENT = (
    "import confetti from 'https://esm.sh/canvas-confetti';"
    "trame.utils.confetti = confetti;"
)

with DivLayout(server):
    html.Button("Click Me", click="utils.confetti()")
    client.Script(JS_CONTENT, module=True)

server.start()
