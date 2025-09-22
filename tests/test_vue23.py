import pytest

from playwright.sync_api import expect
from trame_client.utils.testing import assert_html_matches


@pytest.mark.parametrize(
    "server_path",
    ["examples/vue2/dynamic_template.py"],
)
def test_dynamic_template(server, page, ref_dir):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    ref_path = ref_dir / "test_dynamic_template_initial.html"
    assert_html_matches(page.content(), ref_path)

    expect(page.locator(".staticDiv")).to_have_text("Static text 2")
    expect(page.locator(".countDiv")).to_have_text("count = 2")
    expect(page.locator(".ttsDiv")).to_have_text("tts = 0")
    assert server.get("count") == 2

    page.locator(".plusBtn").click()
    page.locator(".plusBtn").click()
    expect(page.locator(".staticDiv")).to_have_text("Static text 2")
    assert server.get("count") == 4
    expect(page.locator(".countDiv")).to_have_text("count = 4")
    expect(page.locator(".ttsDiv")).to_have_text("tts = 0")
    page.locator(".updateBtn").click()
    page.locator(".updateBtn").click()
    expect(page.locator(".staticDiv")).to_have_text("Static text 6")
    assert server.get("count") == 6
    expect(page.locator(".countDiv")).to_have_text("count = 6")
    expect(page.locator(".ttsDiv")).to_have_text("tts = 2")

    ref_path = ref_dir / "test_dynamic_template_final.html"
    assert_html_matches(page.content(), ref_path)


@pytest.mark.parametrize(
    "server_path",
    ["examples/vue2/js_call.py", "examples/vue3/js_call.py"],
)
def test_js_call(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    expect(page.locator(".jsAlert")).to_have_text("Alert")
    assert server.get("message") == "hello world"
    page.locator(".alertMsg").click()
    expect(page.locator(".jsAlert")).to_have_text("hello world")
    page.locator(".alertMe").click()
    expect(page.locator(".jsAlert")).to_have_text("Yes me")
    page.locator(".swapMsg").click()
    assert server.get("message") == "dlrow olleh"
    page.locator(".alertMsg").click()
    expect(page.locator(".jsAlert")).to_have_text("dlrow olleh")
