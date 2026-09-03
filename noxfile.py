"""
Nox automation for trame-client.

Usage:
    uvx nox                 # run every default session (tests + pre-commit)
    uvx nox -s tests         # run the test suite across all supported Pythons
    uvx nox -s "tests-3.12"  # run the test suite against a single version
    uvx nox -s pre_commit    # run pre-commit hooks against the whole repo

Sessions use the `uv` backend (https://docs.astral.sh/uv/), so `nox` doesn't
need pre-installed interpreters for every Python version - uv fetches
whichever one a session asks for.
"""

import shutil
from pathlib import Path

import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["tests", "pre_commit"]

PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14"]

# The Python package serves these prebuilt JS bundles (see pyproject.toml's
# [tool.hatch.build] include list); the browser-driven tests need them built
# once before pytest can exercise them.
WEB_APPS = {
    "vue2-app": Path("src/trame_client/module/vue2-www"),
    "vue3-app": Path("src/trame_client/module/vue3-www"),
    "react-app": Path("src/trame_client/module/react-www"),
}


def _ensure_vue_apps_built(session):
    if shutil.which("npm") is None:
        session.warn(
            "npm not found - skipping Vue2/Vue3/React client build. "
            "Browser-driven tests will fail without it."
        )
        return

    # react-app consumes js-lib's built dist/ output (see
    # docs/adding-support-for-react/react-app-implementation-plan.md §1).
    js_lib_dist = Path("js-lib/dist")
    if not js_lib_dist.exists():
        with session.chdir("js-lib"):
            session.run("npm", "ci", external=True)
            session.run("npm", "run", "build", external=True)

    for app_dir, output_dir in WEB_APPS.items():
        if output_dir.exists():
            session.log(f"{output_dir} already built, skipping `{app_dir}` build")
            continue
        with session.chdir(app_dir):
            session.run("npm", "ci", external=True)
            session.run("npm", "run", "build", external=True)


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite against a given Python version, installed via uv."""
    _ensure_vue_apps_built(session)

    session.install("-e", ".[test]", "coverage")
    session.run("playwright", "install")
    session.run("coverage", "run", "--source", ".", "-m", "pytest", "-s", ".")
    session.run("coverage", "report", "-m")


@nox.session(python="3.12")
def pre_commit(session):
    """Run every pre-commit hook against the full codebase."""
    session.install("-e", ".[dev]")
    session.run("pre-commit", "run", "--all-files")
