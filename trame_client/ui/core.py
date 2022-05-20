class AbstractLayout:
    """
    A layout is responsible for a section if not all the ui of your application.
    It follow the same logic as any HTML container except that it also have to
    evaluate its content so it can be reflected on the client side.
    Usually to do that you will need call `flush_content` or by using it as a ContextManager.

    A layout needs to be bound to a server
    """

    def __init__(self, _server, _root_elem, template_name="main", **kwargs):
        self._server = _server
        self._current_root = _root_elem
        self._template_name = f"trame__template_{template_name}"
        self._server.state[self._template_name] = ""

    @property
    def root(self):
        """
        Top level Vue component. Useful for providing / injecting into children components. Setting makes old root child of new root.
        """
        return self._current_root

    @root.setter
    def root(self, new_root):
        """Swap the current root with a new one by adding the previous one as a child of that new one."""
        if new_root and self._current_root != new_root:
            new_root.children += [self._current_root]
            self._current_root = new_root

    @property
    def html(self):
        """
        Compute corresponding layout String which represent the html part.
        """
        return self.root.html

    @property
    def server(self):
        """Return the server"""
        return self._server

    @property
    def controller(self):
        """Return the server.controller"""
        return self._server.controller

    @property
    def state(self):
        """Return the server.state"""
        return self._server.state

    def flush_content(self):
        """Push new content to client"""
        self._server.state[self._template_name] = self.html

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        self.root.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.root.__exit__(exc_type, exc_value, exc_traceback)
        self.flush_content()
