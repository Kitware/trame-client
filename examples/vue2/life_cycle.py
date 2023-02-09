from trame.app import get_server

server = get_server()
server.client_type = "vue2"
ctrl = server.controller
server.state.trame__template_main = "Life Cycle App"


@ctrl.add("on_server_ready")
def server_ready(**state):
    print("on_server_ready")


@ctrl.add("on_client_connected")
def client_connected():
    print("on_client_connected")


@ctrl.add("on_client_unmounted")
def client_unmounted():
    print("on_client_unmounted")


@ctrl.add("on_client_exited")
def client_exited():
    print("on_client_exited")


@ctrl.add("on_server_exited")
def server_exited(**state):
    print("on_server_exited")


server.start()
