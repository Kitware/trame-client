from pathlib import Path

import multiprocessing
import pytest
import traceback
import uuid
from playwright.async_api import expect, async_playwright
from trame.app import get_server
from unittest.mock import MagicMock

from trame.ui.html import DivLayout
from trame.widgets import html
from trame_client.widgets import client


def _register_external_script_worker(script_path, name, barrier, errors):
    from trame_client.widgets import client

    barrier.wait()

    try:
        client.register_external_script(
            Path(script_path), function_names=["run"], name=name
        )
        errors.put(None)
    except BaseException:  # noqa: BLE001
        errors.put(f"{name}:\n{traceback.format_exc()}")


def test_register_external_script_is_safe_across_processes(tmp_path):
    n_workers = 8
    context = multiprocessing.get_context("spawn")
    barrier = context.Barrier(n_workers)
    errors = context.Queue()

    processes = []
    for index in range(n_workers):
        script = tmp_path / f"worker_{index}.js"
        script.write_text(f"export function run_worker_{index}() {{}}\n")
        processes.append(
            context.Process(
                target=_register_external_script_worker,
                args=(str(script), f"worker_{index}", barrier, errors),
            )
        )

    for process in processes:
        process.start()

    # Drain while running: large tracebacks would fill the pipe and deadlock a join-first.
    failures = [error for error in (errors.get() for _ in range(n_workers)) if error]

    for process in processes:
        process.join()

    assert not failures, "Concurrent script registration failed:\n" + "\n".join(
        failures
    )


@pytest.mark.asyncio
async def test_registered_external_script_runs_in_the_browser(
    tmp_path, unused_tcp_port
):
    script = tmp_path / "double.js"
    script.write_text(
        "export function double(value) {"
        "  return { status: true, outputs: Number(value) * 2 };"
        "}\n"
    )

    server = get_server(f"test_external_script_{uuid.uuid4()}", client_type="vue3")
    server.state.result = 0
    mock = MagicMock()

    registered = client.register_external_script(
        script, function_names=["double"], name="double"
    )

    def on_completed(outputs):
        server.state.result = outputs
        mock(outputs)

    with DivLayout(server):
        with client.Handler(
            variable="value_ref",
            function=registered,
            completed=(on_completed, "[$event.outputs]"),
        ):
            html.Input(v_model="value_ref.value", classes="input")
        html.Span("{{ result }}", classes="result")

    server.start(port=unused_tcp_port, exec_mode="task")
    try:
        await server.ready

        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                await page.goto(f"http://127.0.0.1:{server.port}/")
                await page.locator(".input").fill("21")
                await expect(page.locator(".result")).to_have_text("42")
                mock.assert_called_once_with(42)
            finally:
                await browser.close()
    finally:
        await server.stop()
