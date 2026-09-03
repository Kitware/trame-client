import json
from pathlib import Path


def load_json(name):
    file_path = Path(__file__).parent.parent / Path(name)
    with open(file_path, "r") as f:
        return json.load(f)


def to_py_name(v):
    """Python kwarg name for an attributes.json entry (str or [py_name, html_name])."""
    return v[0] if isinstance(v, (list, tuple)) else v


def to_html_name(v):
    """Actual HTML/wire attribute name for an attributes.json entry (str or [py_name, html_name])."""
    return v[1] if isinstance(v, (list, tuple)) else v


def to_str(v):
    if isinstance(v, (tuple, list)):
        return v
    return f'"{v}"'


def to_doc_str(v):
    if isinstance(v, (tuple, list)):
        return v[0]
    return v


# -----------------------------------------------------------------------------
# React: python kwarg name -> react DOM prop name, for the html attribute
# names (resources/attributes.json) that don't already match React's
# camelCase convention as-is. Anything not listed here keeps the exact same
# spelling for both client types (e.g. "type", "min", "max", "value", ...).
# Best-effort - reflects the common/well-known cases, not verified
# exhaustively against react-dom's internal attribute table.
# -----------------------------------------------------------------------------
REACT_ATTRIBUTE_OVERRIDES = {
    "accept-charset": "acceptCharset",
    "accesskey": "accessKey",
    "allowfullscreen": "allowFullScreen",
    "allowpaymentrequest": "allowPaymentRequest",
    "allowusermedia": "allowUserMedia",
    "autocapitalize": "autoCapitalize",
    "autocomplete": "autoComplete",
    "autofocus": "autoFocus",
    "autoplay": "autoPlay",
    "cellpadding": "cellPadding",
    "cellspacing": "cellSpacing",
    "charoff": "charOff",
    "charset": "charSet",
    "classes": "className",
    "classid": "classID",
    "codebase": "codeBase",
    "codetype": "codeType",
    "colspan": "colSpan",
    "contenteditable": "contentEditable",
    "crossorigin": "crossOrigin",
    "datetime": "dateTime",
    "dirname": "dirName",
    "enterkeyhint": "enterKeyHint",
    "for": "htmlFor",
    "formaction": "formAction",
    "formenctype": "formEncType",
    "formmethod": "formMethod",
    "formnovalidate": "formNoValidate",
    "formtarget": "formTarget",
    "frameborder": "frameBorder",
    "hreflang": "hrefLang",
    "http-equiv": "httpEquiv",
    "imagesizes": "imageSizes",
    "imagesrcset": "imageSrcSet",
    "inputmode": "inputMode",
    "ismap": "isMap",
    "itemid": "itemID",
    "itemprop": "itemProp",
    "itemref": "itemRef",
    "itemscope": "itemScope",
    "itemtype": "itemType",
    "longdesc": "longDesc",
    "marginheight": "marginHeight",
    "marginwidth": "marginWidth",
    "maxlength": "maxLength",
    "minlength": "minLength",
    "nomodule": "noModule",
    "novalidate": "noValidate",
    "playsinline": "playsInline",
    "readonly": "readOnly",
    "referrerpolicy": "referrerPolicy",
    "rowspan": "rowSpan",
    "spellcheck": "spellCheck",
    "srcdoc": "srcDoc",
    "srclang": "srcLang",
    "srcset": "srcSet",
    "tabindex": "tabIndex",
    "typemustmatch": "typeMustMatch",
    "usemap": "useMap",
    "valuetype": "valueType",
    "webkitdirectory": "webkitDirectory",
}


def to_vue_entry(v):
    """
    Convert an attributes.json entry (str or [py_name, html_name]) into a
    vue-flavored (py_name, name) generator entry. Python kwargs can't contain
    "-" (e.g. the "accept-charset"/"http-equiv" HTML attributes), so any
    hyphenated name gets its own python-safe alias ("-" -> "_") mapped back
    to the real HTML/Vue attribute name, the same way ["classes", "class"]
    already maps around the "class" keyword clash.
    """
    py_name = to_py_name(v)
    html_name = to_html_name(v)
    safe_py_name = py_name.replace("-", "_")
    if safe_py_name == html_name:
        return safe_py_name
    return [safe_py_name, html_name]


def to_react_entry(v):
    """
    Convert an attributes.json entry (str or [py_name, html_name]) into a
    (py_name, react_name) generator entry: same "-" -> "_" python-name
    sanitizing as to_vue_entry, then translated through
    REACT_ATTRIBUTE_OVERRIDES (looked up by the original, possibly
    hyphenated, python name) where needed.
    """
    py_name = to_py_name(v)
    safe_py_name = py_name.replace("-", "_")
    react_name = REACT_ATTRIBUTE_OVERRIDES.get(py_name, py_name)
    if react_name == safe_py_name:
        return safe_py_name
    return [safe_py_name, react_name]


class HtmlEntry:
    def __init__(self, html_element, html_attributes):
        self.name = html_element.capitalize()
        self.html_element = html_element
        self._raw_props = list(map(to_vue_entry, html_attributes))
        self.vue_attributes = list(map(to_str, self._raw_props))
        self.react_attributes = list(map(to_str, map(to_react_entry, html_attributes)))

    def __str__(self):
        lines = []
        lines.append(f"class {self.name}(HtmlElement):")
        lines.append('    """')
        if len(self._raw_props):
            lines.append("    Properties:\n")
            for name in self._raw_props:
                lines.append(f"    :param {to_doc_str(name)}:")
        else:
            lines.append(
                "    No element-specific properties. See AbstractElement for the"
            )
            lines.append("    shared attributes/events available on every element.")
        lines.append('\n    """')
        lines.append("    def __init__(self, children=None, **kwargs):")
        lines.append(
            f'        super().__init__("{self.html_element}", children, **kwargs)'
        )

        if len(self.vue_attributes):
            lines.append("        if self.server.client_type in VUE_CLIENT_TYPES:")
            lines.append("            self.props += [")
            for attr in self.vue_attributes:
                lines.append(f"                {attr},")
            lines.append("            ]")
            lines.append('        elif self.server.client_type == "react":')
            lines.append("            self.props += [")
            for attr in self.react_attributes:
                lines.append(f"                {attr},")
            lines.append("            ]")

        lines.append("")
        return "\n".join(lines)


# -----------------------------------------------------------------------------
HTML_ATTRIBUTES = load_json("resources/attributes.json")

# Sorted (not a bare set) so regenerating this file twice in a row produces
# an identical diff - plain `set` iteration order is subject to Python's
# per-process string-hash randomization.
HTML_ELEMENTS = sorted(set(HTML_ATTRIBUTES.keys()) - {"*"})


def attributes(name):
    """
    Element-specific attributes only. The universal ones (id, class(Name),
    style, ref, key, the vue directives, ...) are already added to every
    element by AbstractElement's active implementation
    (vue.HtmlElement/react.HtmlElement's own SHARED_ATTRIBUTES/SHARED_PROPS)
    - baking resources/attributes.json's "*" entry into every generated
    class here too would just be a redundant (and, for react's differently
    -spelled prop names, actively incorrect) duplicate.
    """
    return HTML_ATTRIBUTES.get(name, [])


def generate_html_elements():
    dst_file = Path(__file__).parent / Path("html.py")
    output = [
        "# Generated file - DO NOT EDIT",
        "from .core import (",
        "   VUE_CLIENT_TYPES,",
        "   HtmlElement,",
        "   Template,",
        "   Component,",
        "   Transition,",
        "   TransitionGroup,",
        "   KeepAlive,",
        "   Teleport,",
        "   Suspense,",
        ")",
        "from .. import module",
        "",
        "HtmlElement.MODULE = module",
        "",
    ]

    # Fill __all__
    output.append("__all__ = [")
    output.append('    "Template",')
    output.append('    "Component",')
    output.append('    "Transition",')
    output.append('    "TransitionGroup",')
    output.append('    "KeepAlive",')
    output.append('    "Teleport",')
    output.append('    "Suspense",')
    for elem in HTML_ELEMENTS:
        output.append(f'    "{elem.capitalize()}",')
    output.append("]\n\n")

    # Fill classes
    for elem in HTML_ELEMENTS:
        output.append(str(HtmlEntry(elem, attributes(elem))))

    with open(dst_file, "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    print("Generating HTML elements...")
    generate_html_elements()
    print("Done...")
