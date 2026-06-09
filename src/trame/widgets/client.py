from trame_client.widgets.trame import *  # noqa F403


def initialize(server):
    from trame_client import module

    server.enable_module(module)
