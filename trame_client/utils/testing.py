import json
from pathlib import Path
from xprocess import ProcessStarter


class TrameServerMonitor:
    def __init__(self, log_path):
        self._log_path = log_path
        self._last_state = {}
        self.port = 0
        self.update()

    def update(self):
        last_state_line = "STATE: {}"
        with open(self._log_path, "r") as f:
            for line in f.readlines():
                print(line)
                if "SERVER_PORT:" in line:
                    self.port = int(line[13:])
                if line[:7] == "STATE: ":
                    last_state_line = line

        self._last_state = json.loads(last_state_line[7:])

    def get_state(self):
        self.update()
        return self._last_state

    def get(self, name):
        self.update()
        return self._last_state.get(name)


def print_state(**kwargs):
    print("STATE:", json.dumps(kwargs), flush=True)


def enable_testing(server, *state_monitor):
    server.state.change(*state_monitor)(print_state)

    @server.controller.add("on_server_ready")
    def print_server_port(**kwargs):
        print("SERVER_PORT:", server.port, flush=True)

    return server


class FixtureHelper:
    def __init__(self, root_path):
        self.root_path = Path(root_path)

    def remove_page_urls(self):
        BASE_PATH = self.root_path / "visual_baseline"
        for file in BASE_PATH.glob("**/page_url.txt"):
            file.unlink()
            print(f" - remove: {file}")

    def get_xprocess_args(self, server_path):
        class Starter(ProcessStarter):
            terminate_on_interrupt = True
            pattern = "App running at:"

            # command to start process
            args = [
                "python3",
                str(self.root_path / server_path),
                "--server",
                "--port",
                "0",
            ]

        return Path(server_path).name, Starter, TrameServerMonitor
