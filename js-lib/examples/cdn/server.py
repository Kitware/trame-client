from trame.app import get_server

server = get_server()
state, ctrl = server.state, server.controller

state.list = [
    "a",
    "b",
    "c",
]

state.count = 1


@ctrl.trigger("add")
def add_to_count():
    state.count += 1


@ctrl.trigger("subtract")
def subtract_to_count():
    state.count += 1


server.start()
