"""
Exercise every widget in `trame.widgets.client` against the react client:

    - Style               inject/update a global <style> tag
    - Script              inject a global <script> tag and call what it defines
    - ClientStateChange   fire a callback whenever a state variable changes
    - ClientTriggers      call named client-side handlers from the server,
                           and route client-side events back to the server
    - JSEval              run arbitrary JS client-side from a server trigger
    - LifeCycleMonitor    observe a subtree's mount/unmount life cycle
    - SizeObserver        bind an element's on-screen size to state

Each section below is self-contained and logs what happened to the shared
event log on the right so its behavior is visible without opening the
browser console.
"""

from trame.app import TrameApp
from trame.widgets import client, html, react
from trame.ui.html import DivLayout

# React elements take `style` as a dict of camelCase CSS properties, not a
# CSS text string (that's a Vue-ism).
CARD_STYLE = {
    "border": "1px solid #ccc",
    "borderRadius": "6px",
    "padding": "12px",
    "marginBottom": "12px",
}


class ClientWidgetsApp(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")

        self.state.counter = 0
        self.state.events = []
        self.state.box_size = None
        self.state.dark_theme = False
        self.state.show_monitor = True

        with DivLayout(self.server) as self.ui:
            self._style = client.Style(self._css(dark=False))
            client.Script(
                "window.trameClientWidgetsDemo = "
                "() => window.alert('Injected by client.Script!');"
            )

            with html.Div(
                style={"maxWidth": "900px", "margin": "0 auto", "padding": "16px"}
            ):
                html.H1("trame client widgets (react)")

                with html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "2fr 1fr",
                        "gap": "16px",
                    }
                ):
                    with html.Div():
                        self._style_section()
                        self._script_section()
                        self._client_state_change_section()
                        self._client_triggers_section()
                        self._js_eval_section()
                        self._life_cycle_monitor_section()
                        self._size_observer_section()

                    self._event_log()

    # -------------------------------------------------------------------
    # Shared helpers
    # -------------------------------------------------------------------
    def _css(self, dark):
        if dark:
            return (
                "body { margin: 0; font-family: sans-serif; "
                "background: #222; color: #eee; }"
            )
        return "body { margin: 0; font-family: sans-serif; }"

    def _log(self, message):
        self.state.events = [message, *self.state.events][:12]

    def _event_log(self):
        with html.Div(style={**CARD_STYLE, "height": "fit-content"}):
            html.H3("Event log")
            with html.Ul(style={"paddingLeft": "18px", "fontFamily": "monospace"}):
                with react.For(items="events", name="entry"):
                    html.Li([react.Bind("entry")])

    # -------------------------------------------------------------------
    # client.Style
    # -------------------------------------------------------------------
    def _style_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("Style")
            html.P("Toggle a global CSS rule injected by client.Style.")
            html.Button("Toggle dark theme", on_click=react.Callback(self.toggle_theme))

    def toggle_theme(self):
        self.state.dark_theme = not self.state.dark_theme
        self._style.update(self._css(self.state.dark_theme))
        self._log(f"Style: theme is now {'dark' if self.state.dark_theme else 'light'}")

    # -------------------------------------------------------------------
    # client.Script
    # -------------------------------------------------------------------
    def _script_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("Script")
            html.P("Call a function defined by the script client.Script injected.")
            html.Button(
                "Call window.trameClientWidgetsDemo()",
                on_click=react.Callback("window.trameClientWidgetsDemo()"),
            )

    # -------------------------------------------------------------------
    # client.ClientStateChange
    # -------------------------------------------------------------------
    def _client_state_change_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("ClientStateChange")
            html.P(["counter = ", react.Bind("counter")])
            html.Button("counter += 1", on_click=react.Callback(self.increment))
            client.ClientStateChange(
                value="counter",
                trigger_on_create=True,
                change=react.Callback(self.on_counter_changed),
            )

    def increment(self):
        self.state.counter += 1

    def on_counter_changed(self):
        self._log(f"ClientStateChange: counter changed to {self.state.counter}")

    # -------------------------------------------------------------------
    # client.ClientTriggers
    # -------------------------------------------------------------------
    def _client_triggers_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("ClientTriggers")
            html.P("Ask the client to emit 'ping', which calls back to the server.")
            triggers = client.ClientTriggers(
                mounted=react.Callback(self.on_triggers_mounted),
                ping=react.Callback(self.on_ping),
            )
            html.Button(
                "Ping client",
                on_click=react.Callback(triggers.call, "['ping']"),
            )

    def on_triggers_mounted(self):
        self._log("ClientTriggers: mounted")

    def on_ping(self):
        self._log("ClientTriggers: server asked client to ping, client replied")

    # -------------------------------------------------------------------
    # client.JSEval
    # -------------------------------------------------------------------
    def _js_eval_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("JSEval")
            html.P("Trigger arbitrary JS from the server, with a bound payload.")
            js_eval = client.JSEval(
                event="Hello from JSEval!",
                exec=react.Callback("window.alert($event)"),
            )
            html.Button("Show alert", on_click=react.Callback(js_eval.exec))

    # -------------------------------------------------------------------
    # client.LifeCycleMonitor
    # -------------------------------------------------------------------
    def _life_cycle_monitor_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("LifeCycleMonitor")
            html.P("Mount/unmount a monitored subtree and watch the log.")
            html.Button(
                "Toggle monitored subtree",
                on_click=react.Callback("show_monitor = !show_monitor"),
            )
            with react.If(value="show_monitor"):
                client.LifeCycleMonitor(
                    name="DemoMonitor",
                    type="emit",
                    value="counter",
                    events=["mounted", "destroyed"],
                    mounted=react.Callback(self.on_monitor_event, "['mounted']"),
                    destroyed=react.Callback(self.on_monitor_event, "['destroyed']"),
                )
                html.Div("(monitored subtree is mounted)")

    def on_monitor_event(self, phase):
        self._log(f"LifeCycleMonitor: {phase}")

    # -------------------------------------------------------------------
    # client.SizeObserver
    # -------------------------------------------------------------------
    def _size_observer_section(self):
        with html.Div(style=CARD_STYLE):
            html.H3("SizeObserver")
            html.P("Drag the bottom-right corner to resize and watch the size update.")
            with html.Div(
                style={
                    "width": "320px",
                    "height": "120px",
                    "resize": "both",
                    "overflow": "auto",
                    "border": "1px dashed #888",
                }
            ):
                with client.SizeObserver("box_size"):
                    html.Div(
                        [
                            react.Bind(
                                "box_size ? "
                                "`${Math.round(box_size.size.width)} x "
                                "${Math.round(box_size.size.height)} px` : "
                                "'measuring...'"
                            )
                        ],
                        style={"padding": "8px"},
                    )


def main():
    app = ClientWidgetsApp()
    app.server.start()


if __name__ == "__main__":
    main()
