class TrameDefault:
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def set_defaults(self, server):
        for k, v in self._kwargs.items():
            server.state.setdefault(k, v)
