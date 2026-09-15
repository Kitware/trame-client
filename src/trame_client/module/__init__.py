import atexit
import os
import shutil
import tempfile
from pathlib import Path

# Registered scripts are copied to a temporary directory that is served to the client and removed at process exit.
_TMP_DIR_PATH = Path(tempfile.mkdtemp(prefix="trame-client-"))
_TMP_DIR_PID = os.getpid()


@atexit.register
def _cleanup_tmp_dir():
    if os.getpid() == _TMP_DIR_PID:
        shutil.rmtree(_TMP_DIR_PATH, ignore_errors=True)


USER_PROVIDED_SCRIPTS_DIR_PATH = _TMP_DIR_PATH
USER_PROVIDED_UMD_SCRIPTS_DIR_PATH = USER_PROVIDED_SCRIPTS_DIR_PATH / "umd"
USER_PROVIDED_ES_SCRIPTS_DIR_PATH = USER_PROVIDED_SCRIPTS_DIR_PATH / "es"
USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX = Path("__trame_client_external_scripts")

USER_PROVIDED_ES_SCRIPTS_DIR_PATH.mkdir()
USER_PROVIDED_UMD_SCRIPTS_DIR_PATH.mkdir()


def setup_handler_module(server):
    serve_path = USER_PROVIDED_SCRIPTS_DIR_PATH.resolve()
    module_scripts_path = USER_PROVIDED_ES_SCRIPTS_DIR_PATH.resolve()
    umd_scripts_path = USER_PROVIDED_UMD_SCRIPTS_DIR_PATH.resolve()

    server.enable_module(
        {
            "serve": {
                USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX.as_posix(): str(serve_path)
            },
            "module_scripts": [
                (
                    USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX
                    / module_scripts_path.name
                    / module_file.name
                ).as_posix()
                for module_file in module_scripts_path.glob("*.js")
            ],
            "scripts": [
                (
                    USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX
                    / umd_scripts_path.name
                    / module_file.name
                ).as_posix()
                for module_file in umd_scripts_path.glob("*.js")
            ],
        }
    )


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type == "vue2":
        from . import vue2

        server.enable_module(vue2)
    elif client_type == "vue3":
        from . import vue3

        server.enable_module(vue3)
        setup_handler_module(server)
    elif client_type == "react":
        from . import react

        server.enable_module(react)
        setup_handler_module(server)
    else:
        raise TypeError(
            f"Trying to initialize trame_client with unknown client_type={client_type}"
        )
