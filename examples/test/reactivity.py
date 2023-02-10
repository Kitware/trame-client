import json
from trame.app import get_server


server = get_server()
server.state.count = 1
server.state.trame__template_main = """
    <div>
        <div class="countValue" style="padding: 20px; background: red;">{{ count }}</div>
        <button class="plusButton" @click="count++">Add to count</button>
    </div>
"""


@server.state.change("count")
def print_state(**kwargs):
    print("STATE:", json.dumps(kwargs), flush=True)


server.start()
