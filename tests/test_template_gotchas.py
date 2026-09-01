"""
Locks down `AbstractElement`/`Template` serialization behavior that isn't
covered elsewhere, with a focus on behavior that either:

- must stay identical across `client_type`s (vue2/vue3 today; a future
  "react" client_type should be checked against these the same way), or
- is a deliberate, known per-`client_type` divergence (currently just the
  `ref=` handling for vue3).

This file exists to give a future `client_type="react"` a clear baseline to
be validated against, and to catch accidental regressions in the string-based
template generation used by the Vue paths today.
"""

import pytest

from trame.app import get_server
from trame_client.utils.defaults import TrameDefault
from trame_client.widgets.html import (
    Div,
    Input,
    Li,
    Ul,
    Component,
    Transition,
    TransitionGroup,
    KeepAlive,
    Teleport,
    Suspense,
    Template,
)

CLIENT_TYPES = ["vue2", "vue3"]


# -----------------------------------------------------------------------------
# ref= is the one attribute that is genuinely client_type-specific today
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_ref_handling_per_client_type(client_type):
    server = get_server(f"test_ref_{client_type}", client_type=client_type)
    widget = Div(trame_server=server, ref="my_ref")

    if client_type == "vue3":
        # vue3 rewrites ref= into a callback that registers the element
        # into trame.refs, so JS-side method calls (server.js_call) work.
        assert widget.html == ("<div :ref=\"(el) => trame.refs['my_ref'] = el\" />")
    elif client_type == "vue2":
        # vue2 has no equivalent rewrite - ref stays a plain Vue template ref.
        assert widget.html == '<div ref="my_ref" />'
    else:
        assert False, "Invalid client type"


# -----------------------------------------------------------------------------
# Attribute value type handling - identical regardless of client_type
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_boolean_attribute_serialization(client_type):
    server = get_server(f"test_bool_{client_type}", client_type=client_type)

    # True -> bare attribute, no value
    assert Div(trame_server=server, hidden=True).html == "<div hidden />"

    # False -> explicit JS-bound false, not simply omitted
    assert Div(trame_server=server, hidden=False).html == '<div :hidden="false" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_style_dict_is_flattened_to_css_string(client_type):
    server = get_server(f"test_style_{client_type}", client_type=client_type)
    widget = Div(trame_server=server, style={"color": "red", "font-size": "12px"})
    assert widget.html == '<div style="color: red; font-size: 12px;" />'


# -----------------------------------------------------------------------------
# v-model modifier gotchas
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_v_model_named_modifiers(client_type):
    server = get_server(f"test_vmodel_named_{client_type}", client_type=client_type)

    assert Input(trame_server=server, v_model_lazy="a").html == (
        '<input v-model.lazy="a" />'
    )
    assert Input(trame_server=server, v_model_trim="a").html == (
        '<input v-model.trim="a" />'
    )
    # a name that is *not* a known modifier keyword becomes a named v-model
    assert Input(trame_server=server, v_model_hello="a").html == (
        '<input v-model:hello="a" />'
    )


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_v_model_modifier_plus_extra_suffix_is_a_gotcha(client_type):
    """
    Combining a recognized modifier keyword (number/lazy/trim) with an
    *additional* modifier does NOT produce `v-model.number.lazy` as one might
    expect. Because `model_name` ("number") is technically a known modifier
    but `modifiers` is non-empty, the code falls into the "named model"
    branch and emits a colon instead of a dot for the first segment:
    `v-model:number.lazy` rather than `v-model.number.lazy`.

    This is almost certainly not what a Vue author would intend (there is no
    custom model literally named "number" here) - it's captured as a test so
    the behavior can't silently change (or silently "get fixed") without
    this test flagging it either way.
    """
    server = get_server(f"test_vmodel_combo_{client_type}", client_type=client_type)
    widget = Input(trame_server=server, v_model_number_lazy="a")
    assert widget.html == '<input v-model:number.lazy="a" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_v_model_tuple_sets_state_default(client_type):
    server = get_server(f"test_vmodel_default_{client_type}", client_type=client_type)
    widget = Input(trame_server=server, v_model_number=("count", 2))
    assert widget.html == '<input v-model.number="count" />'
    assert server.state.count == 2


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_v_model_tuple_with_trame_default_sets_multiple_keys(client_type):
    """
    The second element of a (expr, default) tuple can be a `TrameDefault`
    instead of a plain value, letting a single binding set defaults for
    several state keys at once - not just the one being bound.
    """
    server = get_server(
        f"test_vmodel_multidefault_{client_type}", client_type=client_type
    )
    widget = Input(
        trame_server=server,
        v_model_number=("count", TrameDefault(count=2, offset=1)),
    )
    assert widget.html == '<input v-model.number="count" />'
    assert server.state.count == 2
    assert server.state.offset == 1


# -----------------------------------------------------------------------------
# Event value forms: string / callable / 1-tuple / 2-tuple / 3-tuple
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_event_as_raw_js_string(client_type):
    server = get_server(f"test_event_str_{client_type}", client_type=client_type)
    widget = Div(trame_server=server, click="count = count + 1")
    assert widget.html == '<div @click="count = count + 1" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_event_as_callable_and_tuples(client_type):
    server = get_server(f"test_event_callable_{client_type}", client_type=client_type)

    def handler():
        pass

    trigger_name = server.trigger_name(handler)

    # bare callable -> trigger with no arguments
    assert Div(trame_server=server, click=handler).html == (
        f"<div @click=\"trigger('{trigger_name}')\" />"
    )

    # 1-tuple -> same as bare callable
    assert Div(trame_server=server, click=(handler,)).html == (
        f"<div @click=\"trigger('{trigger_name}')\" />"
    )

    # 2-tuple -> (callable, args_js)
    assert Div(trame_server=server, click=(handler, "[4]")).html == (
        f"<div @click=\"trigger('{trigger_name}', [4])\" />"
    )

    # 3-tuple -> (callable, args_js, kwargs_js)
    assert Div(trame_server=server, click=(handler, "[4]", "{}")).html == (
        f"<div @click=\"trigger('{trigger_name}', [4], {{}})\" />"
    )


def test_event_3tuple_kwargs_are_not_translated():
    """
    `_event_value_processing` deliberately translates the *args* JS
    expression (2nd tuple element) against the state translator/namespace,
    but passes the *kwargs* JS expression (3rd element) through verbatim.
    This matters for namespaced/child servers, where a bare identifier like
    `f` would otherwise get silently renamed to `child_f`.
    """
    root = get_server("test_event_kwargs_translation_root", client_type="vue3")
    child = root.create_child_server(prefix="child_")
    child.state.f = 1

    def handler():
        pass

    trigger_name = child.trigger_name(handler)

    widget = Div(trame_server=child, click=(handler, "f", "{other: f}"))

    # args ("f") got namespaced to the child-prefixed key
    assert f"trigger('{trigger_name}', child_f, {{other: f}})" in widget.html
    # kwargs ("{other: f}") were NOT namespaced - passed through as-is
    assert "{other: f}" in widget.html


# -----------------------------------------------------------------------------
# Custom `__properties`/`__events` extension mechanism (how a widget author
# adds attributes/events beyond the built-in shared set)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_custom_property_plain_string_is_literal(client_type):
    """
    A custom property registered as a plain name (no explicit JS key) is
    treated as a literal HTML attribute, not a JS-bound one - the value is
    NOT run through the JS expression translator, even though it "looks"
    like it could be a bound prop.
    """
    server = get_server(f"test_custom_prop_{client_type}", client_type=client_type)
    widget = Div(
        trame_server=server,
        __properties=["custom_prop"],
        custom_prop="hello",
    )
    assert widget.html == '<div custom-prop="hello" />'
    assert "custom_prop" not in widget.skipped_attributes


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_custom_property_explicit_js_key_supports_binding(client_type):
    """
    Registering a custom property as an (py_name, js_key) tuple with an
    explicit `:jsKey` lets it behave like a real bound prop, including
    the (expr, default) tuple form that sets a state default.
    """
    server = get_server(f"test_custom_prop_js_{client_type}", client_type=client_type)
    widget = Div(
        trame_server=server,
        __properties=[("custom_prop", ":customProp")],
        custom_prop=("my_key", 42),
    )
    assert widget.html == '<div :customProp="my_key" />'
    assert server.state.my_key == 42


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_custom_event(client_type):
    server = get_server(f"test_custom_event_{client_type}", client_type=client_type)
    widget = Div(
        trame_server=server,
        __events=["custom_event"],
        custom_event="doSomething()",
    )
    assert widget.html == '<div @custom-event="doSomething()" />'


# -----------------------------------------------------------------------------
# Small standalone helpers on AbstractElement
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_tts_sensitive_adds_key_binding(client_type):
    server = get_server(f"test_tts_{client_type}", client_type=client_type)
    widget = Div(trame_server=server)
    widget.ttsSensitive()
    assert ':key="`w' in widget.html
    assert '-${tts}`"' in widget.html


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_raw_attrs_are_inserted_verbatim(client_type):
    server = get_server(f"test_raw_attrs_{client_type}", client_type=client_type)
    widget = Template(
        trame_server=server,
        raw_attrs=["v-slot:item.1", 'class="bg-red"'],
    )
    assert widget.html == '<template v-slot:item.1 class="bg-red" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_hide_sets_display_none(client_type):
    server = get_server(f"test_hide_{client_type}", client_type=client_type)
    widget = Div(trame_server=server)
    widget.hide()
    assert 'style="display: none"' in widget.html


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_hide_combined_with_explicit_style_is_a_gotcha(client_type):
    """
    `hide()` writes to a distinct internal attribute key ("__style") rather
    than merging with an already-set `style=` kwarg. The two coexist in the
    attribute dict, so calling `.hide()` on a widget that also has an
    explicit `style=` kwarg renders **two** `style="..."` attributes in the
    output - technically invalid HTML (duplicate attribute), even though
    browsers will just use one of them. Captured here so this doesn't
    silently change (or silently get "fixed") without a test noticing.
    """
    server = get_server(f"test_hide_style_combo_{client_type}", client_type=client_type)
    widget = Div(trame_server=server, style={"color": "red"})
    widget.hide()
    assert widget.html.count('style="') == 2
    assert 'style="color: red;"' in widget.html
    assert 'style="display: none"' in widget.html


# -----------------------------------------------------------------------------
# Vue-only structural components - smoke tests for attribute/event mapping
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_component_is_attribute(client_type):
    server = get_server(f"test_dyncomp_{client_type}", client_type=client_type)
    widget = Component(trame_server=server, is_name="MyWidget")
    assert widget.html == '<component is="MyWidget" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_transition_camel_case_props_and_events(client_type):
    server = get_server(f"test_transition_{client_type}", client_type=client_type)
    widget = Transition(
        trame_server=server,
        name="fade",
        enter_from_class="x",
        before_enter="onBeforeEnter()",
    )
    assert 'name="fade"' in widget.html
    assert 'enterFromClass="x"' in widget.html
    assert '@before-enter="onBeforeEnter()"' in widget.html


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_transition_group_move_class(client_type):
    server = get_server(f"test_transitiongroup_{client_type}", client_type=client_type)
    widget = TransitionGroup(trame_server=server, tag="ul", move_class="move")
    assert widget.html == '<transition-group tag="ul" moveClass="move" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_keep_alive_props(client_type):
    server = get_server(f"test_keepalive_{client_type}", client_type=client_type)
    widget = KeepAlive(trame_server=server, include="a,b", max=5)
    assert widget.html == '<keep-alive include="a,b" max="5" />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_teleport_props(client_type):
    server = get_server(f"test_teleport_{client_type}", client_type=client_type)
    widget = Teleport(trame_server=server, to="body", disabled=True)
    assert widget.html == '<teleport to="body" disabled />'


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_suspense_props_and_events(client_type):
    server = get_server(f"test_suspense_{client_type}", client_type=client_type)
    widget = Suspense(trame_server=server, timeout=100, resolve="onResolve()")
    assert 'timeout="100"' in widget.html
    assert '@resolve="onResolve()"' in widget.html


# -----------------------------------------------------------------------------
# Template slot name registration (fixed, non-dynamic names)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_template_fixed_slot_name(client_type):
    """
    `Template.slot_names` is a *class-level*, globally shared set - any
    widget library that registers slot names (e.g. a data table widget
    registering "item.name") makes that slot kwarg available on every
    `Template` instance for the rest of the process. Save/restore it here so
    this test doesn't leak state into others.
    """
    server = get_server(f"test_template_slot_{client_type}", client_type=client_type)
    original_slot_names = set(Template.slot_names)
    try:
        Template.slot_names.add("item.name")
        widget = Template(trame_server=server, v_slot_item_name="{ item }")
        assert widget.html == '<template v-slot:item.name="{ item }" />'
    finally:
        Template.slot_names.clear()
        Template.slot_names.update(original_slot_names)


# -----------------------------------------------------------------------------
# Parity check: same widget tree should produce structurally equivalent
# output across client types, aside from the known ref= divergence above.
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("client_type", CLIENT_TYPES)
def test_full_widget_tree_parity_across_client_types(client_type):
    server = get_server(f"test_parity_{client_type}", client_type=client_type)
    server.state.items = ["a", "b"]

    with Ul(trame_server=server) as ul:
        Li(
            trame_server=server,
            children="{{ item }}",
            v_for="item in items",
            key="item",
        )

    assert ul.html == (
        '<ul >\n<li :key="item" v-for="item in items">\n{{ item }}\n</li>\n</ul>'
    )
