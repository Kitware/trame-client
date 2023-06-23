import json
from pathlib import Path
from xprocess import ProcessStarter
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch


# ---------------------------------------------------------
# Pytest helpers
# ---------------------------------------------------------


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
                "--host",
                "127.0.0.1",
                "--port",
                "0",
            ]

        return Path(server_path).name, Starter, TrameServerMonitor


# ---------------------------------------------------------
# Seleniumbase helper functions
# ---------------------------------------------------------


def set_browser_size(sb, width=300, height=300):
    delta_width = 0
    delta_height = 0
    agent = sb.get_user_agent()
    if "Firefox" in agent:
        delta_height = 85
    elif "Chrome" in agent:
        delta_height = 0
    elif "Safari" in agent:
        delta_height = 0

    sb.set_window_size(width + delta_width, height + delta_height)
    wait_for_ready(sb)


def baseline_comparison(sb, check_baseline_path, threshold=0.1):
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

    sb.assert_true(
        min_mismatch < threshold,
        f"Baseline threshold {min_mismatch} < {threshold}",
    )


def wait_for_ready(sb, timeout=60):
    for i in range(timeout):
        print(f"wait_for_ready {i}")
        if sb.is_element_present(".trame__loader"):
            sb.sleep(1)
        else:
            print("Ready")
            return
