from pathlib import Path


def get_user_preprocessor_scripts_path() -> Path:
    return Path(__file__).with_name("user_preprocessors_module_scripts")


def get_user_preprocessor_umd_scripts_path() -> Path:
    return get_user_preprocessor_scripts_path() / "umd"


def get_user_preprocessor_es_scripts_path() -> Path:
    return get_user_preprocessor_scripts_path() / "es"


def get_user_preprocessor_serve_url_prefix() -> Path:
    return Path("__trame_client_preprocessors")


def setup_client_preprocessing_module(server):
    root_path = get_user_preprocessor_serve_url_prefix()

    serve_path = get_user_preprocessor_scripts_path().resolve()
    module_scripts_path = get_user_preprocessor_umd_scripts_path().resolve()
    umd_scripts_path = get_user_preprocessor_umd_scripts_path().resolve()

    server.enable_module(
        {
            "serve": {root_path.as_posix(): str(serve_path)},
            "module_scripts": [
                (root_path / module_scripts_path.name / module_file.name).as_posix()
                for module_file in module_scripts_path.glob("*.js")
            ],
            "scripts": [
                (root_path / umd_scripts_path.name / module_file.name).as_posix()
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
        setup_client_preprocessing_module(server)
    else:
        raise TypeError(
            f"Trying to initialize trame_client with unknown client_type={client_type}"
        )
