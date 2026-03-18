from pathlib import Path

def setup_client_preprocessing_module(server):
    root_path = Path("__trame_client_preprocessors")

    serve_path = Path(__file__).with_name("user_preprocessors_module_scripts").resolve()
    server.enable_module(
        {
            "serve": {
                root_path.as_posix(): str(serve_path)
            },
            "module_scripts": [
                (root_path / module_file.name).as_posix() for module_file in serve_path.glob("*.js")
            ]
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
        setup_client_preprocessing_module(server)
    else:
        raise TypeError(
            f"Trying to initialize trame_client with unknown client_type={client_type}"
        )
