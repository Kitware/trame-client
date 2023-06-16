from trame.app import get_server
from trame_client.utils.testing import enable_testing

server = get_server()
server.state.count = 1
server.state.trame__template_main = """
    <div>
        <div class="countValue" style="padding: 20px; background: red;">{{ count }}</div>
        <button class="plusButton" @click="count++">Add to count</button>
    </div>
"""

enable_testing(server, "count")
server.start()
