import asyncio
import time
import uuid

import pytest
from playwright.sync_api import expect, sync_playwright

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import html

from trame_client.widgets.adapter import ClientAdapter

MOUSE_EVENTS = [
    "click",
    "contextmenu",
    "dblclick",
    "mousedown",
    "mouseup",
    "mouseenter",
    "mouseleave",
    "mousemove",
    "mouseover",
    "mouseout",
]
KEY_EVENTS = ["keydown", "keyup", "keypress"]
FOCUS_EVENTS = ["focusin", "focusout"]
TOUCH_EVENTS = ["touchstart", "touchmove", "touchend", "touchcancel"]
ANIMATION_EVENTS = ["animationstart", "animationend", "animationiteration"]
TRANSITION_EVENTS = ["transitionend"]

TARGET_EVENTS = (
    MOUSE_EVENTS
    + KEY_EVENTS
    + FOCUS_EVENTS
    + TOUCH_EVENTS
    + ANIMATION_EVENTS
    + TRANSITION_EVENTS
)
EVENT_NAMES = TARGET_EVENTS + ["input", "change", "submit"]

CLIENT_TYPES = ["vue3", "react"]


def _state_key(event_name):
    return f"event_{event_name}"


def build_events_app(server):
    for name in EVENT_NAMES:
        server.state.setdefault(_state_key(name), False)

    def make_handler(event_name):
        def handler(**_):
            server.state[_state_key(event_name)] = True

        return handler

    handlers = {name: make_handler(name) for name in EVENT_NAMES}
    adapter = ClientAdapter(server)

    with DivLayout(server):
        html.Button(
            "target",
            classes="eventTarget",
            **adapter.events(**{name: handlers[name] for name in TARGET_EVENTS}),
        )
        with html.Form(
            classes="eventForm", **adapter.events(submit=handlers["submit"])
        ):
            html.Input(
                classes="eventInput",
                **adapter.events(
                    input=handlers["input"],
                    change=handlers["change"],
                    focusin=handlers["focusin"],
                    focusout=handlers["focusout"],
                ),
            )


def run_interactions(url):
    """Drive every event through a real browser interaction (or dispatch)."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url)

            target = page.locator(".eventTarget")
            text_input = page.locator(".eventInput")
            form = page.locator(".eventForm")
            expect(target).to_be_visible()

            target.click()
            target.dblclick()
            target.click(button="right")

            target.hover()
            page.mouse.move(1000, 600)

            target.focus()
            text_input.focus()

            target.focus()
            page.keyboard.press("a")

            text_input.fill("hello")
            target.focus()
            form.dispatch_event("submit")

            for name in ("touchstart", "touchmove", "touchend", "touchcancel"):
                target.dispatch_event(name)

            for name in (
                "animationstart",
                "animationend",
                "animationiteration",
                "transitionend",
            ):
                target.dispatch_event(name)

            # Let the event triggers round-trip to the (same-process) server
            # before the browser is closed.
            page.wait_for_timeout(500)
        finally:
            browser.close()


async def wait_for_event(server, event_name, timeout=5.0):
    deadline = time.monotonic() + timeout
    while server.state[_state_key(event_name)] is not True:
        if time.monotonic() > deadline:
            raise AssertionError(f"Event {event_name!r} was not triggered")
        await asyncio.sleep(0.05)


@pytest.mark.asyncio
@pytest.mark.parametrize("client_type", CLIENT_TYPES)
async def test_events_trigger_for_the_same_interactions(client_type, unused_tcp_port):
    server = get_server(f"test_events_{uuid.uuid4()}", client_type=client_type)
    build_events_app(server)

    server.start(port=unused_tcp_port, exec_mode="task")
    try:
        await server.ready
        await asyncio.to_thread(run_interactions, f"http://127.0.0.1:{server.port}/")

        for name in EVENT_NAMES:
            await wait_for_event(server, name)
    finally:
        await server.stop()
