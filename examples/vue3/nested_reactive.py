from trame.app import get_server
from trame.widgets import html, client
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.nested_1 = {
    "sliders": [
        {"value": 10, "min": 1, "max": 20, "step": 2},
        {"value": 1, "min": 1, "max": 20, "step": 1},
        {"value": 5, "min": 1, "max": 20, "step": 5},
    ],
    "a": 10,
}
state.nested_2 = {
    "sliders": [
        {"value": 10, "min": 1, "max": 20, "step": 2},
        {"value": 1, "min": 1, "max": 20, "step": 1},
        {"value": 5, "min": 1, "max": 20, "step": 5},
    ],
    "a": 10,
}

state.nested_3 = {
    "sliders": [
        {"value": 10, "min": 1, "max": 20, "step": 2},
        {"value": 1, "min": 1, "max": 20, "step": 1},
        {"value": 5, "min": 1, "max": 20, "step": 5},
    ],
    "a": 10,
}


@state.change("nested_1")
def update_nested_1(nested_1, **kwargs):
    print("nested 1")


@state.change("nested_2")
def update_nested_2(nested_2, **kwargs):
    print("nested 2")


@state.change("nested_3")
def update_nested_3(nested_3, **kwargs):
    print("nested 3")


with DivLayout(server) as layout:
    # Workaround / old fashion
    html.Div("{{ nested_2 }}")
    html.Input(
        type="range",
        value=("nested_2.a",),
        raw_attrs=[
            "@input=\"nested_2.a = $event.target.value; flushState('nested_2')\""
        ],
        min=1,
        max=10,
        step=1,
    )
    with html.Div("Nested 1 - {{ nested_1.a }}"):
        html.Input(
            type="range",
            value=("nested_1.a",),
            raw_attrs=[
                "@input=\"nested_1.a = $event.target.value; flushState('nested_1')\""
            ],
            min=1,
            max=10,
            step=1,
        )
        with html.Div("Sliders"):
            html.Input(
                v_for="s, i in nested_1.sliders",
                key="i",
                type="range",
                value=("s.value",),
                min=("s.min",),
                max=("s.max",),
                step=("s.step",),
                raw_attrs=[
                    "@input=\"s.value = $event.target.value; flushState('nested_1')\""
                ],
            )

    # New deep reactive (Vue3 only)
    with client.DeepReactive("nested_2") as dr:
        with html.Div("Nested 2 - {{ nested_2.a }}"):
            html.Input(type="range", v_model="nested_2.a", min=1, max=10, step=1)
            with html.Div("Sliders"):
                html.Input(
                    v_for="s, i in nested_2.sliders",
                    key="i",
                    type="range",
                    v_model="s.value",
                    min=("s.min",),
                    max=("s.max",),
                    step=("s.step",),
                )

    # Not working
    with html.Div("Nested 3 - {{ nested_3.a }}"):
        html.Input(type="range", v_model="nested_3.a", min=1, max=10, step=1)
        with html.Div("Sliders"):
            html.Input(
                v_for="s, i in nested_3.sliders",
                key="i",
                type="range",
                v_model="s.value",
                min=("s.min",),
                max=("s.max",),
                step=("s.step",),
            )

server.start()
