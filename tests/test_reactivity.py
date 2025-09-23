from playwright.sync_api import expect
import pytest

from trame_client.utils.testing import assert_snapshot_matches


@pytest.mark.parametrize("server_path", ["examples/test/reactivity.py"])
def test_reactivity(server, page, ref_dir):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    assert_snapshot_matches(page, ref_dir, "simple_count_1")

    plus_button = page.locator(".plusButton")
    count_value = page.locator(".countValue")

    expect(count_value).to_have_text("1")
    assert server.get("count") == 1
    plus_button.click()
    expect(count_value).to_have_text("2")
    assert server.get("count") == 2
    plus_button.click()
    plus_button.click()
    expect(count_value).to_have_text("4")
    assert server.get("count") == 4
    plus_button.click()
    expect(count_value).to_have_text("5")
    assert server.get("count") == 5

    assert_snapshot_matches(page, ref_dir, "simple_count_5")
