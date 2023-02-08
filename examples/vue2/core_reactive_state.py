from trame.app import get_server

server = get_server()
state, ctrl = server.state, server.controller

server.client_type = "vue2"  # default until trame>=3.x

state.count = 2
state.double = 4
state.client_type = server.client_type


@state.change("count")
def update_count(count, **kwargs):
    state.double = 2 * int(count)


state.trame__template_main = """
    <div>
        <label>{{ client_type }}</label>
        <div>count = {{ count }}</div>
        <div>2 x count = {{ double }}</div>
        <input type="range" min="0" max="10" step="1" v-model="count" />
    </div>
"""

server.start()
