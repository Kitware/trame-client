from trame_client.widgets.trame import *


def initialize(server):
    from trame_client import module

    server.enable_module(module)
