from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from .core import HTML_CTX
from .react import Bind, Callback

if TYPE_CHECKING:
    from trame_server import Server

__all__ = [
    "ClientAdapter",
]

VUE_TO_REACT_EVENT_NAMES: dict[str, str] = {
    "click": "on_click",
    "contextmenu": "on_context_menu",
    "dblclick": "on_double_click",
    "mousedown": "on_mouse_down",
    "mouseup": "on_mouse_up",
    "mouseenter": "on_mouse_enter",
    "mouseleave": "on_mouse_leave",
    "mousemove": "on_mouse_move",
    "mouseover": "on_mouse_over",
    "mouseout": "on_mouse_out",
    "keydown": "on_key_down",
    "keyup": "on_key_up",
    "keypress": "on_key_press",
    "submit": "on_submit",
    "input": "on_input",
    "change": "on_change",
    "focusin": "on_focus",
    "focusout": "on_blur",
    "touchstart": "on_touch_start",
    "touchmove": "on_touch_move",
    "touchend": "on_touch_end",
    "touchcancel": "on_touch_cancel",
    "animationstart": "on_animation_start",
    "animationend": "on_animation_end",
    "animationiteration": "on_animation_iteration",
    "transitionend": "on_transition_end",
}


class ClientAdapter:
    """
    Client-type aware UI helpers.

    Callers use the Vue syntax (the default); the adapter translates it to the
    active client so widgets stay client-agnostic.
    """

    def __init__(self, server: Server | None = None):
        self._server = server if server is not None else self._current_server()

    @property
    def server(self) -> Server:
        return self._server

    def style(self, style: Mapping[str, Any]) -> Any:
        """
        Return a client-specific ``style`` value from a CSS mapping.

        Keys may be kebab-case or camelCase. Dynamic values (see
        :meth:`expression`) are supported on both clients.
        """
        if self._is_react:
            return {self._to_camel_case(name): value for name, value in style.items()}

        if any(self._is_js_expression(value) for value in style.values()):
            entries = ", ".join(
                f"{self._to_camel_case(name)}: {self._style_value(value)}"
                for name, value in style.items()
            )
            return (f"{{{entries}}}",)

        return " ".join(
            f"{self._to_kebab_case(name)}: {value};" for name, value in style.items()
        )

    def event(
        self, name: str, handler: Any, modifiers: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Return the kwargs binding ``handler`` to the DOM event ``name``.

        ``name`` uses the Vue spelling and ``modifiers`` are Vue-style. Use the
        bubbling ``"focusin"``/``"focusout"`` names rather than
        ``"focus"``/``"blur"`` for cross-client focus events.
        """
        if not self._is_react:
            if modifiers:
                return {f"v_on_{name}_{'_'.join(modifiers)}": handler}
            return {name: handler}

        try:
            react_name = VUE_TO_REACT_EVENT_NAMES[name]
        except KeyError as error:
            _error_msg = f"Event {name!r} is not supported by the react client"
            raise ValueError(_error_msg) from error
        return {react_name: Callback(handler, modifiers=modifiers)}

    def events(self, **events: Any) -> dict[str, Any]:
        """
        Return the kwargs for several DOM events at once.
        """
        kwargs: dict[str, Any] = {}
        for name, handler in events.items():
            kwargs.update(self.event(name, handler))
        return kwargs

    def expression(self, js_expression: str) -> Any:
        """
        Return a client-specific wrapper for a dynamic JS expression.

        Usable as a prop value or inside :meth:`style`.
        """
        if self._is_react:
            return Bind(js_expression)
        return (js_expression,)

    @classmethod
    def _current_server(cls) -> Server:
        if HTML_CTX.element_stack:
            server = HTML_CTX.element_stack[-1].server
            if server is not None:
                return server
        return HTML_CTX._server

    @property
    def _client_type(self) -> str:
        return self._server.client_type

    @property
    def _is_react(self) -> bool:
        return self._client_type == "react"

    @property
    def _is_vue(self) -> bool:
        return self._client_type in ("vue2", "vue3")

    @classmethod
    def _to_kebab_case(cls, name: str) -> str:
        return "".join(f"-{char.lower()}" if char.isupper() else char for char in name)

    @classmethod
    def _to_camel_case(cls, name: str) -> str:
        head, *rest = name.split("-")
        return head + "".join(part[:1].upper() + part[1:] for part in rest)

    @classmethod
    def _is_js_expression(cls, value: Any) -> bool:
        return (
            isinstance(value, tuple) and len(value) == 1 and isinstance(value[0], str)
        )

    @classmethod
    def _js_string(cls, value: Any) -> str:
        if isinstance(value, str):
            escaped = value.replace("\\", "\\\\").replace("'", "\\'")
            return f"'{escaped}'"
        if isinstance(value, bool):
            return "true" if value else "false"
        if value is None:
            return "null"
        return json.dumps(value)

    @classmethod
    def _style_value(cls, value: Any) -> str:
        if cls._is_js_expression(value):
            return value[0]
        return cls._js_string(value)
