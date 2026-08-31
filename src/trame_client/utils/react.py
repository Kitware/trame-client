"""React serialization of trame widget trees.

When ``server.client_type == "react"`` the layout content is serialized as a
JSON component tree rather than an HTML/template string. The React client
(react-app) walks that tree with ``React.createElement`` and evaluates the
embedded expressions against the trame shared state.

Node schema (version 1)::

    {
        "tag": "div",
        "attrs": {"id": "container"},  # static attributes
        "props": {"disabled": "count > 3"},  # dynamic (JS expressions)
        "on": {"click": "trigger('name')"},  # event name => JS body
        "dirs": {  # structural directives
            "if": "expr",
            "elseIf": "expr",
            "else": True,
            "show": "expr",
            "for": {"item": "i", "index": "idx", "source": "expr"},
            "models": [{"arg": None, "modifiers": [], "expr": "varName"}],
            "text": "expr",
            "html": "expr",
            "slot": {"arg": "name", "expr": "slotProps"},
            "onObject": "expr",
            "bindObject": "expr",
        },
        "raw": ["v-anything='...'"],  # raw_attrs passthrough
        "children": [node | "text" | {"expr": "count + 1"}],
    }
"""

import re

MUSTACHE_RE = re.compile(r"\{\{(.*?)\}\}", re.DOTALL)
V_FOR_RE = re.compile(
    r"^\s*\(?\s*([\w$]+)\s*(?:,\s*([\w$]+))?\s*(?:,\s*([\w$]+))?\s*\)?"
    r"\s+(?:in|of)\s+(.+?)\s*$",
    re.DOTALL,
)


def split_text(text, server=None):
    """Split a text child into plain strings and {"expr": ...} segments"""
    segments = []
    pos = 0
    for m in MUSTACHE_RE.finditer(text):
        if m.start() > pos:
            segments.append(text[pos : m.start()])
        expr = m.group(1).strip()
        if server is not None:
            expr = server.state.translator.translate_js_expression(server.state, expr)
        segments.append({"expr": expr})
        pos = m.end()
    if pos < len(text):
        segments.append(text[pos:])
    return segments


def parse_v_for(expression):
    """Parse a "(item, index) in source" expression into a structure"""
    m = V_FOR_RE.match(expression)
    if m is None:
        return {"item": "item", "index": None, "source": expression}
    item, index, extra, source = m.groups()
    result = {"item": item, "index": index, "source": source}
    if extra:
        result["extra"] = extra
    return result


def parse_directive_key(js_key):
    """Split a "v-name:arg.mod1.mod2" key into (name, arg, modifiers)"""
    body = js_key[2:]  # strip "v-"
    arg = None
    if ":" in body:
        body, arg = body.split(":", 1)
        if "." in arg:
            arg, *arg_modifiers = arg.split(".")
            return body, arg, arg_modifiers
        return body, arg, []
    if "." in body:
        body, *modifiers = body.split(".")
        return body, arg, modifiers
    return body, arg, []


def _apply_directive(dirs, js_key, expr):
    name, arg, modifiers = parse_directive_key(js_key)
    if name == "if":
        dirs["if"] = expr
    elif name == "else-if":
        dirs["elseIf"] = expr
    elif name == "else":
        dirs["else"] = True
    elif name == "show":
        dirs["show"] = expr
    elif name == "for":
        dirs["for"] = parse_v_for(expr)
    elif name == "model":
        dirs.setdefault("models", []).append(
            {"arg": arg, "modifiers": modifiers, "expr": expr}
        )
    elif name == "text":
        dirs["text"] = expr
    elif name == "html":
        dirs["html"] = expr
    elif name == "slot":
        dirs["slot"] = {"arg": arg, "expr": expr or None}
    elif name == "on":
        dirs["onObject"] = expr
    elif name == "bind":
        dirs["bindObject"] = expr
    else:
        # pre, once, memo, cloak, custom directives => passthrough
        dirs.setdefault("custom", {})[js_key] = {
            "arg": arg,
            "modifiers": modifiers,
            "expr": expr,
        }


def to_react_node(elem):
    """Serialize an AbstractElement (or VirtualNode) into a react node dict"""
    if isinstance(elem, str):
        return {"tag": "__fragment", "children": split_text(elem)}

    if not hasattr(elem, "_elem_name"):
        # VirtualNode and other child containers
        return {
            "tag": "__fragment",
            "children": _children_to_react(elem.children, elem.server),
        }

    node = {"tag": elem._elem_name}
    attrs = {}
    props = {}
    on = {}
    dirs = {}
    raw = []

    for entry in elem._attr_entries.values():
        kind = entry["kind"]
        if kind == "static":
            attrs[entry["key"]] = entry["value"]
        elif kind == "bind":
            props[entry["key"]] = entry["expr"]
        elif kind == "event":
            on[entry["key"]] = entry["expr"]
        elif kind == "directive":
            _apply_directive(dirs, entry["key"], entry["expr"])
        elif kind == "raw":
            raw.append(entry["value"])

    # Some widgets write directly into _attributes (e.g. Getter's v-slot,
    # trame-vtk's ref= and :viewId=); capture whatever the structured
    # entries missed.
    for name, formatted in elem._attributes.items():
        if name in elem._attr_entries:
            continue
        m = re.match(r'^(v-[\w:.-]+)="(.*)"$', formatted, re.DOTALL)
        if m:
            _apply_directive(dirs, m.group(1), m.group(2))
            continue
        m = re.match(r'^:([\w:.-]+)="(.*)"$', formatted, re.DOTALL)
        if m:
            props[m.group(1)] = m.group(2)
            continue
        m = re.match(r'^@([\w:.-]+)="(.*)"$', formatted, re.DOTALL)
        if m:
            on[m.group(1)] = m.group(2)
            continue
        m = re.match(r'^([\w-]+)="(.*)"$', formatted, re.DOTALL)
        if m:
            attrs[m.group(1)] = m.group(2)
            continue
        raw.append(formatted)

    if attrs:
        node["attrs"] = attrs
    if props:
        node["props"] = props
    if on:
        node["on"] = on
    if dirs:
        node["dirs"] = dirs
    if raw:
        node["raw"] = raw

    children = _children_to_react(elem.children, elem.server)
    if children:
        node["children"] = children

    return node


def _children_to_react(children, server=None):
    result = []
    for child in children:
        if isinstance(child, str):
            result.extend(split_text(child, server))
        elif hasattr(child, "react_node"):
            result.append(child.react_node)
        else:
            result.append(to_react_node(child))
    return result


def to_react_template(root):
    """Serialize a layout root into the native dict pushed to the client"""
    node = root.react_node if hasattr(root, "react_node") else to_react_node(root)
    return {"version": 1, "root": node}
