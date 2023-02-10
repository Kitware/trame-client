import os
import json
import pytest
from xprocess import ProcessStarter
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.absolute()


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
                if "Network:" in line:
                    self.port = line.split(":").pop().split("/")[0]
                if line[:7] == "STATE: ":
                    last_state_line = line

        self._last_state = json.loads(last_state_line[7:])

    def get_state(self):
        self.update()
        return self._last_state

    def get(self, name):
        self.update()
        return self._last_state.get(name)


def remove_page_urls():
    BASE_PATH = Path(__file__).parent.with_name("visual_baseline")
    for root, dirs, files in os.walk(BASE_PATH):
        if "page_url.txt" in files:
            full_path = os.path.join(root, "page_url.txt")
            os.remove(full_path)
            print(f" - remove: {full_path}")


@pytest.fixture()
def baseline_image():
    remove_page_urls()
    yield
    remove_page_urls()


@pytest.fixture
def server(xprocess, server_path):
    name = Path(server_path).name

    class Starter(ProcessStarter):
        terminate_on_interrupt = True
        pattern = "App running at:"

        # command to start process
        args = [
            "python3",
            ROOT_PATH / server_path,
            "--server",
            "--port",
            "0",
        ]

    # ensure process is running and return its logfile
    logfile = xprocess.ensure(name, Starter)
    yield TrameServerMonitor(logfile[1])

    # clean up whole process tree afterwards
    xprocess.getinfo(name).terminate()
