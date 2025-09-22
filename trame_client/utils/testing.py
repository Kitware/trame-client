import json
import sys
from pathlib import Path
from xprocess import ProcessStarter
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

from playwright.sync_api import expect, Page


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


def assert_images_match(img_test: Image, ref_path: Path, threshold=0.1):
    img_ref = Image.open(ref_path)
    img_diff = Image.new("RGBA", img_ref.size)
    diff_path = ref_path.parent / f"diff_{ref_path.with_suffix('.png').name}"

    mismatch = pixelmatch(img_ref, img_test, img_diff, threshold=threshold)
    img_diff.save(diff_path)
    assert mismatch < threshold


# ---------------------------------------------------------
# Playwright helpers
# ---------------------------------------------------------


def assert_screenshot_matches(
    page: Page, ref_dir: Path, name: str, threshold: float = 0.1
):
    img_dir = ref_dir / name
    ref_images = list(img_dir.glob("ref*.png"))
    if not ref_images:
        print(f"No reference images exist in {img_dir}. Creating one...")
        img_dir.mkdir(parents=True, exist_ok=True)
        ref_img_path = img_dir / "ref1.png"
        page.screenshot(path=ref_img_path)
        return

    # Save the test image
    test_img_path = img_dir / "test_image.png"
    page.screenshot(path=test_img_path)
    img_test = Image.open(test_img_path)

    # If there are reference images, find one that matches
    # Only write out image diffs if none succeed
    for ref_img_path in ref_images:
        try:
            # `expect(page).to_have_screenshot()` is not yet supported
            # in Python playwright, even though it is available in
            # JavaScript... :-\
            # Use our own comparison for now.
            # expect(page).to_have_screenshot(threshold=threshold)
            assert_images_match(img_test, ref_img_path, threshold)
        except AssertionError:
            # We'll just try the next one
            continue
        else:
            # It matched. Return!
            return

    raise AssertionError(f"No reference images matched in {img_dir}")


def assert_snapshot_matches(page: Page, ref_dir: Path, name: str):
    html = page.locator("html")
    ref_path = ref_dir / f"{name}.yml"
    if not ref_path.exists():
        print(f"'{ref_path}' does not exist. Creating...")
        with open(ref_path, "w") as wf:
            wf.write(html.aria_snapshot())
        return

    with open(ref_path, "r") as rf:
        expect(html).to_match_aria_snapshot(rf.read())
