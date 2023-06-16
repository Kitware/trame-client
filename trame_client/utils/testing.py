import json


def print_state(**kwargs):
    print("STATE:", json.dumps(kwargs), flush=True)


def enable_testing(server, *state_monitor):
    server.state.change(*state_monitor)(print_state)

    @server.controller.add("on_server_ready")
    def print_server_port(**kwargs):
        print("SERVER_PORT:", server.port, flush=True)
