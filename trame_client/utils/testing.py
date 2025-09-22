import json
import sys
from pathlib import Path
from xprocess import ProcessStarter
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch


# ---------------------------------------------------------
# Pytest helpers
# ---------------------------------------------------------


class TrameServerMonitor:
    def __init__(self, log_path, do_print_log_lines=False):
        self._log_path = log_path
        self._last_state = {}
        self.port = 0
        self.do_print_log_lines = do_print_log_lines
        self.update()

    def update(self):
        last_state_line = "STATE: {}"
        with open(self._log_path, "r") as f:
            for line in f.readlines():
                if self.do_print_log_lines:
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
                Path(sys.executable).as_posix(),
                str(self.root_path / server_path),
                "--server",
                "--host",
                "127.0.0.1",
                "--port",
                "0",
            ]

        return Path(server_path).name, Starter, TrameServerMonitor


def baseline_comparison(check_baseline_path, threshold=0.1):
    baseline_test = Path(check_baseline_path)
    baseline_refs = baseline_test.parent.glob("baseline_ref*.png")
    baseline_diff = baseline_test.with_name("baseline_diff.png")

    img_test = Image.open(baseline_test)
    min_mismatch = 1000000

    for baseline_ref in baseline_refs:
        img_ref = Image.open(baseline_ref)
        img_diff = Image.new("RGBA", img_ref.size)
        baseline_diff = (
            baseline_ref.parent / f"baseline_diff{baseline_ref.name[12:-4]}.png"
        )

        mismatch = pixelmatch(img_ref, img_test, img_diff, threshold=threshold)
        img_diff.save(baseline_diff)
        min_mismatch = min(min_mismatch, mismatch)

    assert min_mismatch < threshold, f"Baseline threshold {min_mismatch} < {threshold}"


# ---------------------------------------------------------
# Playwright helpers
# ---------------------------------------------------------


def assert_html_matches(html_str: str, ref_path: Path):
    if not ref_path.exists():
        print(f"'{ref_path}' does not exist. Creating...")
        with open(ref_path, "w") as wf:
            wf.write(html_str)
        return

    with open(ref_path, "r") as rf:
        assert html_str == rf.read()
