import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("server_path", ["examples/test/react_client_widgets.py"])
def test_react_client_widgets(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    mounted_count = page.locator(".mountedCount")
    size_box = page.locator(".sizeBox")

    # ClientTriggers: fires "mounted" once on the initial connect/render.
    expect(mounted_count).to_have_text("1")
    assert server.get("mounted_count") == 1

    # Style: injected CSS actually applies (background becomes red).
    expect(size_box).to_be_visible()
    bg = size_box.evaluate("el => getComputedStyle(el).backgroundColor")
    assert bg == "rgb(255, 0, 0)"

    # SizeObserver: writes the observed box's dimensions into state.
    box_size = server.get("box_size")
    assert box_size is not None
    assert box_size["size"]["width"] > 0
    assert box_size["size"]["height"] > 0
