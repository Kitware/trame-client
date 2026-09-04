import pytest
from playwright.sync_api import expect

from trame_client.utils.testing import assert_snapshot_matches


@pytest.mark.parametrize("server_path", ["examples/test/react_reactivity.py"])
def test_react_reactivity(server, page, ref_dir):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    plus_button = page.locator(".plusButton")
    count_value = page.locator(".countValue")

    # Wait for the initial connect/render round trip (async, unlike Vue's
    # synchronous template mount) before snapshotting or interacting.
    expect(count_value).to_have_text("1")
    assert_snapshot_matches(page, ref_dir, "react_simple_count_1")

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

    assert_snapshot_matches(page, ref_dir, "react_simple_count_5")


@pytest.mark.parametrize("server_path", ["examples/test/react_if_for.py"])
def test_react_if_for(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    count_value = page.locator(".countValue")
    slider = page.locator(".countSlider")

    # Bind: initial value round-trips from Python state
    expect(count_value).to_have_text("2")

    # Callback with a JS expression (`count = Number($event.target.value)`):
    # exercises client-side reactivity without a server round trip.
    slider.fill("7")
    slider.dispatch_event("change")
    expect(count_value).to_have_text("7")
    assert server.get("count") == 7

    # Callback wrapping a Python callable: triggers a server-side method,
    # whose state write flows back down to the client.
    page.locator(".resetButton").click()
    expect(count_value).to_have_text("2")
    assert server.get("count") == 2

    # For: one <li> per item, each bound to its own loop variable.
    todo_items = page.locator(".todoItem")
    expect(todo_items).to_have_count(3)
    expect(todo_items.nth(0)).to_have_text("Write docs")
    expect(todo_items.nth(1)).to_have_text("Review PR")
    expect(todo_items.nth(2)).to_have_text("Ship it")
    expect(page.locator(".emptyMsg")).to_have_count(0)

    # If: flips which branch is mounted once the bound expression's truthiness
    # changes server-side.
    page.locator(".clearButton").click()
    expect(page.locator(".todoList")).to_have_count(0)
    expect(page.locator(".emptyMsg")).to_have_text("No todos left")
    assert server.get("todos") == []
