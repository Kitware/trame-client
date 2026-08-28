from playwright.sync_api import expect
import pytest


@pytest.mark.parametrize("server_path", ["examples/test/reactivity_react.py"])
def test_react_reactivity(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

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


@pytest.mark.parametrize("server_path", ["examples/test/model_react.py"])
def test_react_model_slider(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    slider = page.locator("input[type=range]")
    expect(slider).to_have_value("2")
    assert server.get("count") == 2
    assert server.get("double") == 4

    slider.fill("7")
    expect(slider).to_have_value("7")
    assert server.get("count") == 7
    assert server.get("double") == 14
