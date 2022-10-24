import json
from pathlib import Path


def load_json(name):
    file_path = Path(__file__).parent.parent / Path(name)
    with open(file_path, "r") as f:
        return json.load(f)


def to_str(v):
    if isinstance(v, (tuple, list)):
        return v
    return f'"{v}"'


def to_doc_str(v):
    if isinstance(v, (tuple, list)):
        return v[0]
    return v


class HtmlEntry:
    def __init__(self, html_element, html_attributes, html_events):
        self.name = html_element.capitalize()
        self.html_element = html_element
        self.html_attributes = list(map(to_str, html_attributes))
        self.html_events = list(map(to_str, html_events))
        self._raw_props = html_attributes
        self._raw_events = html_events

    def __str__(self):
        lines = []
        lines.append(f"class {self.name}(HtmlElement):")
        lines.append('    """')
        lines.append("    Properties:\n")
        for name in self._raw_props:
            lines.append(f"    :param {to_doc_str(name)}:")
        lines.append("\n    Events:\n")
        for name in self._raw_events:
            lines.append(f"    :param {to_doc_str(name)}:")
        lines.append('\n    """')
        lines.append("    def __init__(self, children=None, **kwargs):")
        lines.append(
            f'        super().__init__("{self.html_element}", children, **kwargs)'
        )

        # List attributes
        if len(self.html_attributes):
            lines.append("        self._attr_names += [")
            for attr in self.html_attributes:
                lines.append(f"            {attr},")
            lines.append("        ]")

        # List events
        if len(self.html_attributes):
            lines.append("        self._event_names += [")
            for event in self.html_events:
                lines.append(f"            {event},")
            lines.append("        ]")

        lines.append("")
        return "\n".join(lines)


# -----------------------------------------------------------------------------
HTML_ATTRIBUTES = load_json("resources/attributes.json")
HTML_EVENTS = load_json("resources/events.json")
HTML_VUEJS = load_json("resources/vue.json")

HTML_ELEMENTS = set(HTML_ATTRIBUTES.keys())
HTML_ELEMENTS.discard("*")


def attributes(name):
    return (
        HTML_ATTRIBUTES.get("*", [])
        + HTML_VUEJS["attributes"].get("*", [])
        + HTML_ATTRIBUTES.get(name, [])
        + HTML_VUEJS["attributes"].get(name, [])
    )


def events(name):
    return (
        HTML_EVENTS.get("*", [])
        + HTML_VUEJS["events"].get("*", [])
        + HTML_EVENTS.get(name, [])
        + HTML_VUEJS["events"].get(name, [])
    )


def generate_html_elements():
    dst_file = Path(__file__).parent / Path("html.py")
    output = [
        "# Generated file - DO NOT EDIT",
        "from .core import HtmlElement, Template",
        "from .. import module",
        "",
        "HtmlElement.MODULE = module",
        "",
    ]

    # Fill __all__
    output.append("__all__ = [")
    output.append('    "Template",')
    for elem in HTML_ELEMENTS:
        output.append(f'    "{elem.capitalize()}",')
    output.append("]\n\n")

    # Fill classes
    for elem in HTML_ELEMENTS:
        output.append(str(HtmlEntry(elem, attributes(elem), events(elem))))

    with open(dst_file, "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    print("Generating HTML elements...")
    generate_html_elements()
    print("Done...")
