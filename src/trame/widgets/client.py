from trame_client.widgets.client import *  # noqa F403


def initialize(server):
    from trame_client import module

    server.enable_module(module)
