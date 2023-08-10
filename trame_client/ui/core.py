import os
from ..utils.formatter import to_pretty_html


def css_unit(v):
    if isinstance(v, int):
        return "px"
    else:
        return ""


# -----------------------------------------------------------------------------
# URL Builder selector logic (TRAME_IFRAME_URL_BUILDER=[default,serverproxy])
# -----------------------------------------------------------------------------
def iframe_url_builder_default(base_url, server_port, template_name):
    return f"{base_url}:{server_port}/index.html?ui={template_name[16:]}&reconnect=auto"


def iframe_url_builder_serverproxy(base_url, server_port, template_name):
    return f"{base_url}/{server_port}/index.html?ui={template_name[16:]}&reconnect=auto"


def get_iframe_url_builder():
    builder_type = os.environ.get("TRAME_IFRAME_URL_BUILDER", "default")
    builder = iframe_url_builder_default

    if builder_type == "serverproxy":
        builder = iframe_url_builder_serverproxy

    return builder


# -----------------------------------------------------------------------------


class AbstractLayout:
    """
    A layout is responsible for a section if not all the ui of your application.
    It follow the same logic as any HTML container except that it also have to
    evaluate its content so it can be reflected on the client side.
    Usually to do that you will need call `flush_content` or by using it as a ContextManager.

    A layout needs to be bound to a server
    """

    def __init__(
        self,
        _server,
        _root_elem,
        template_name="main",
        width="100%",
        height="600px",
        base_url="http://localhost",
        url_builder=None,
        **kwargs,
    ):
        self._server = _server
        self._current_root = _root_elem
        self._original_root = _root_elem
        self._template_name = f"trame__template_{template_name}"
        self._server.state[self._template_name] = ""
        self.iframe_style = f"border: none; width: {width}{css_unit(width)}; height: {height}{css_unit(height)};"
        self.iframe_base_url = base_url

        if url_builder is None:
            url_builder = get_iframe_url_builder()

        self.iframe_url_builder = url_builder

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

    def __repr__(self):
        return to_pretty_html(self.html)

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

    @property
    def ready(self):
        if not self.server.running:
            # NoOp if already start[ing/ed]
            self.server.start(
                exec_mode="task",
                port=0,
                open_browser=False,
                show_connection_info=False,
                disable_logging=True,
                timeout=0,
            )
        return self.server.ready

    def flush_content(self):
        """Push new content to client"""
        self._server.state[self._template_name] = self.html

    # -------------------------------------------------------------------------
    # Resource manager
    # -------------------------------------------------------------------------

    def __enter__(self):
        self._original_root.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._original_root.__exit__(exc_type, exc_value, exc_traceback)
        self.flush_content()

    # -------------------------------------------------------------------------
    # Jupyter display integration
    # -------------------------------------------------------------------------

    def _jupyter_content(self):
        if not self.server.running:
            return """<div>
                    The server is not running. Before displaying a trame layout you should await it to make sure it is ready.
                    You should run the following code before displaying a layout.
                    <pre style="padding: 5px; border: solid 1px rgb(224,224,224); background: rgb(245,245,245);">await layout.ready</pre>
                    </div>"""

        elem_id = f"{self.server.name}_{self._template_name}"
        src = self.iframe_url_builder(
            self.iframe_base_url, self.server.port, self._template_name
        )
        return (
            f'<iframe id="{elem_id}" src="{src}" style="{self.iframe_style}"></iframe>'
        )

    @property
    def ipywidget(self):
        from ipywidgets.widgets import HTML

        return HTML(self._jupyter_content())

    def _ipython_display_(self):
        from IPython.display import display_html, display

        try:
            display(self.ipywidget)
        except ImportError:
            display_html(self._jupyter_content(), raw=True)
