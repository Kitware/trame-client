from trame.app import get_server

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../tests"))
from test_translator import NestedApp  # noqa: E402

CLIENT_TYPE = "vue2"
ISOLATED = False


def main():
    root_server = get_server(client_type=CLIENT_TYPE)

    root_app = NestedApp(root_server, client_type=CLIENT_TYPE)

    if not ISOLATED:
        root_app.child_a_app.server.translator.add_translation("f", "common_f")
        root_app.child_b_app.server.translator.add_translation("f", "common_f")

    root_app.ui

    root_server.controller.on_server_ready.add(
        lambda **kwargs: print("Root server ready")
    )
    root_app.server.start()


if __name__ == "__main__":
    main()
