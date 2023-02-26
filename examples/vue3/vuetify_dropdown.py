import time
from trame.app import get_server
from trame.widgets import vuetify3, client, html
from trame.ui.vuetify3 import SinglePageLayout
from trame.ui.html import DivLayout

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.trame__title = "Menu example"


def add_element():
    state.items += [f"New elem {time.time()}"]
    state.dirty("items")
    print("add_element", state.items)


@ctrl.add("on_server_reload")
def reload_internal(*args, **kwargs):
    with DivLayout(server, template_name="internal"):
        vuetify3.VSelect(
            v_model=("active_item", "one"), items=("items", ["one", "two", "three"])
        )
        html.Pre("{{ items }}")


reload_internal()

with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify3.VSpacer()
        vuetify3.VBtn("Add", click=add_element)
        vuetify3.VSelect(
            v_model=("active_item", "one"), items=("items", ["one", "two", "three"])
        )
    with layout.content:
        client.ServerTemplate(name="internal")


if __name__ == "__main__":
    server.start()
