from trame.app import get_server

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../tests"))
from test_translator import BasicApp  # noqa: E402

CLIENT_TYPE = "vue2"


def main():
    root_server = get_server(client_type=CLIENT_TYPE)
    one_of_the_app = None
    for app_name in ["main", "a", "b", "c"]:
        child_server = root_server.create_child_server(prefix=f"{app_name}_")
        app = BasicApp(child_server, app_name, CLIENT_TYPE)
        app.ui
        app.add()
        app.ctrl.plus()
        one_of_the_app = app

    # root_server.controller.on_server_ready.add(
    #   lambda **kwargs: print(json.dumps(root_server.state.to_dict(), indent=2))
    # )
    root_server.controller.on_server_ready.add(
        lambda **kwargs: print("Root server ready")
    )
    one_of_the_app.server.controller.on_server_ready.add(
        lambda **kwargs: print("Sub server ready")
    )
    one_of_the_app.server.start()


if __name__ == "__main__":
    main()
