import os
import shutil
from pathlib import Path
from typing import Callable
from ..utils.formatter import to_pretty_html


def css_unit(v):
    if isinstance(v, int):
        return "px"
    else:
        return ""


# -----------------------------------------------------------------------------
# IFrame builder (env TRAME_IFRAME_BUILDER)
# => default, serverproxy, jupyter-extension, jupyter-hub
# -----------------------------------------------------------------------------


def iframe_url_builder_default(layout):
    base_url = layout.iframe_base_url
    server = layout.server
    template_name = layout._template_name
    src = f"{base_url}:{server.port}/index.html?ui={template_name[16:]}&reconnect=auto"
    elem_id = f"{server.name}_{template_name}"

    return {
        "id": elem_id,
        "src": src,
        "style": layout.iframe_style,
        **layout.iframe_attrs,
    }


def iframe_url_builder_serverproxy(layout):
    base_url = layout.iframe_base_url
    server = layout.server
    template_name = layout._template_name
    src = f"{base_url}/{server.port}/index.html?ui={template_name[16:]}&reconnect=auto"
    elem_id = f"{server.name}_{template_name}"

    return {
        "id": elem_id,
        "src": src,
        "style": layout.iframe_style,
        **layout.iframe_attrs,
    }


def iframe_url_builder_jupyter_extension(layout):
    from ..utils.jupyter import get_kernel_id

    www_endpoint = os.environ.get("TRAME_JUPYTER_ENDPOINT", "/trame-jupyter-server")
    server = layout.server
    template_name = layout._template_name
    url_base = f"{www_endpoint}/{server.client_type}/index.html"
    url_query = f"ui={template_name[16:]}&server={server.name}&wsProxy&reconnect=auto"
    src = f"{url_base}?{url_query}"
    elem_id = f"{server.name}_{template_name}"

    # Check if server/kernel are collocated
    www_path = os.environ.get("TRAME_JUPYTER_WWW")

    if www_path and Path(www_path).exists():
        server_www = Path(www_path) / "servers" / server.name
        url_base = f"{www_endpoint}/servers/{server.name}/index.html"
        url_query = (
            f"ui={template_name[16:]}&server={server.name}&wsProxy&reconnect=auto"
        )
        src = f"{url_base}?{url_query}"
        if not server_www.exists():
            shutil.copytree(server._www, str(server_www.resolve()), dirs_exist_ok=True)
            for sub_path, src_dir in server.serve.items():
                dst_dir = server_www / sub_path
                shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

    return {
        "id": elem_id,
        "src": src,
        "style": layout.iframe_style,
        "data-kernel-id": get_kernel_id(),
        **layout.iframe_attrs,
    }


def iframe_url_builder_jupyter_hub(layout):
    server = layout.server
    template_name = layout._template_name
    url_base = (
        f"{os.environ['JUPYTERHUB_SERVICE_PREFIX']}proxy/{server.port}/index.html"
    )
    url_query = f"ui={template_name[16:]}&reconnect=auto"
    src = f"{url_base}?{url_query}"
    elem_id = f"{server.name}_{template_name}"

    return {
        "id": elem_id,
        "src": src,
        "style": layout.iframe_style,
        **layout.iframe_attrs,
    }


def iframe_url_builder_jupyter_hub_host(layout):
    host = os.environ.get("HOSTNAME")
    server = layout.server
    template_name = layout._template_name
    url_base = f"{os.environ['JUPYTERHUB_SERVICE_PREFIX']}proxy/{host}:{server.port}/index.html"
    url_query = f"ui={template_name[16:]}&reconnect=auto"
    src = f"{url_base}?{url_query}"
    elem_id = f"{server.name}_{template_name}"

    return {
        "id": elem_id,
        "src": src,
        "style": layout.iframe_style,
        **layout.iframe_attrs,
    }


def get_iframe_builder(name="default"):
    if isinstance(name, Callable):
        return name

    # Try to detect JupyterHub automatically
    if name == "default" and "JUPYTERHUB_SERVICE_PREFIX" in os.environ:
        name = "jupyter-hub"

    builder_type = os.environ.get("TRAME_IFRAME_BUILDER", name)
    builder = iframe_url_builder_default

    if builder_type == "serverproxy":
        builder = iframe_url_builder_serverproxy
    elif builder_type == "jupyter-extension":
        builder = iframe_url_builder_jupyter_extension
    elif builder_type == "jupyter-hub":
        builder = iframe_url_builder_jupyter_hub
    elif builder_type == "jupyter-hub-host":
        builder = iframe_url_builder_jupyter_hub_host

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
        iframe_builder="default",
        **kwargs,
    ):
        self._server = _server
        self._current_root = _root_elem
        self._original_root = _root_elem
        self._template_name = f"trame__template_{template_name}"
        self._server.state[self._template_name] = ""
        self.iframe_style = f"border: none; width: {width}{css_unit(width)}; height: {height}{css_unit(height)};"
        self.iframe_attrs = {}
        self.iframe_base_url = base_url
        self._iframe_builder = get_iframe_builder(iframe_builder)

    @property
    def iframe_builder(self):
        """Instance of iframe builder responsible for generating the iframe tag for mainly for Jupyter"""
        return self._iframe_builder

    @iframe_builder.setter
    def iframe_builder(self, name_or_fn):
        """
        Set iframe builder after construction.
        Method expect a name of built-in (default, serverproxy, jupyter-extension, jupyter-hub)
        or an actual function.
        """
        self._iframe_builder = get_iframe_builder(name_or_fn)

    @property
    def root(self):
        """
        Top level Vue component. Useful for providing / injecting into children components.
        Setting makes old root child of new root.
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
        """Start the server as a background task (if not already started)
        and return the future that represent the status of that task."""
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
            return """
<div>
The server is not running.
Before displaying a trame layout you should await it to make sure it is ready.
You should run the following code before displaying a layout.
<pre style="padding: 5px; border: solid 1px rgb(224,224,224); background: rgb(245,245,245);">await layout.ready</pre>
</div>"""

        attributes = self.iframe_builder(self)
        attributes_str = " ".join(
            f'{key}="{str(value)}"' for key, value in attributes.items()
        )

        return f"<iframe {attributes_str}></iframe>"

    @property
    def ipywidget(self):
        """Convert the UI into a ipywidget so it can be embedded in an ipywidget layout."""
        from ipywidgets.widgets import HTML

        return HTML(value=self._jupyter_content())

    @property
    def url(self):
        """Return application url if started"""
        if not self.server.running:
            return "Server is not running"

        return self.iframe_builder(self)["src"]

    def _ipython_display_(self):
        from IPython.display import display_html, display

        if os.environ.get("TRAME_IPYWIDGETS_DISABLE"):
            display_html(self._jupyter_content(), raw=True)
        else:
            try:
                display(self.ipywidget)
            except ImportError:
                display_html(self._jupyter_content(), raw=True)
