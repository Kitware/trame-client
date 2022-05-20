# Generated file - DO NOT EDIT
from .core import HtmlElement
from .. import module

HtmlElement.MODULE = module

__all__ = [
    "Link",
    "H6",
    "Source",
    "Font",
    "A",
    "Script",
    "Video",
    "Basefont",
    "Del",
    "Hr",
    "Area",
    "Frameset",
    "Q",
    "Data",
    "Progress",
    "Label",
    "H1",
    "Li",
    "Time",
    "Ul",
    "P",
    "Frame",
    "Caption",
    "Dl",
    "Fieldset",
    "Pre",
    "Track",
    "Span",
    "Isindex",
    "Legend",
    "Dir",
    "Output",
    "Tbody",
    "Thead",
    "Col",
    "Blockquote",
    "Ol",
    "Param",
    "Br",
    "Map",
    "H5",
    "Div",
    "Ins",
    "Table",
    "Form",
    "Meter",
    "Style",
    "Iframe",
    "Body",
    "Html",
    "Tr",
    "Dialog",
    "Applet",
    "Input",
    "Option",
    "Button",
    "H3",
    "Slot",
    "Canvas",
    "Object",
    "Th",
    "Img",
    "B",
    "Select",
    "Head",
    "H2",
    "Textarea",
    "I",
    "Colgroup",
    "Audio",
    "Optgroup",
    "Td",
    "Base",
    "Menu",
    "Tfoot",
    "Meta",
    "Details",
    "Embed",
    "H4",
]


class Link(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - as
       - charset
       - color
       - crossorigin
       - disabled
       - href
       - hreflang
       - imagesizes
       - imagesrcset
       - integrity
       - media
       - referrerpolicy
       - rel
       - rev
       - sizes
       - target
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("link", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "as",
            "charset",
            "color",
            "crossorigin",
            "disabled",
            "href",
            "hreflang",
            "imagesizes",
            "imagesrcset",
            "integrity",
            "media",
            "referrerpolicy",
            "rel",
            "rev",
            "sizes",
            "target",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H6(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h6", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Source(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - height
       - media
       - sizes
       - src
       - srcset
       - type
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("source", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "height",
            "media",
            "sizes",
            "src",
            "srcset",
            "type",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Font(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - color
       - face
       - size
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("font", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "color",
            "face",
            "size",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class A(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - charset
       - coords
       - download
       - href
       - hreflang
       - name
       - ping
       - referrerpolicy
       - rel
       - rev
       - shape
       - target
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("a", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "charset",
            "coords",
            "download",
            "href",
            "hreflang",
            "name",
            "ping",
            "referrerpolicy",
            "rel",
            "rev",
            "shape",
            "target",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Script(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - async
       - charset
       - crossorigin
       - defer
       - integrity
       - language
       - nomodule
       - referrerpolicy
       - src
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("script", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "async",
            "charset",
            "crossorigin",
            "defer",
            "integrity",
            "language",
            "nomodule",
            "referrerpolicy",
            "src",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Video(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - autoplay
       - controls
       - crossorigin
       - height
       - loop
       - muted
       - playsinline
       - poster
       - preload
       - src
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("video", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "autoplay",
            "controls",
            "crossorigin",
            "height",
            "loop",
            "muted",
            "playsinline",
            "poster",
            "preload",
            "src",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Basefont(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - color
       - face
       - size
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("basefont", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "color",
            "face",
            "size",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Del(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - cite
       - datetime
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("del", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "cite",
            "datetime",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Hr(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - noshade
       - size
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("hr", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "noshade",
            "size",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Area(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - alt
       - coords
       - download
       - href
       - hreflang
       - nohref
       - ping
       - referrerpolicy
       - rel
       - shape
       - target
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("area", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "alt",
            "coords",
            "download",
            "href",
            "hreflang",
            "nohref",
            "ping",
            "referrerpolicy",
            "rel",
            "shape",
            "target",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Frameset(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - cols
       - rows
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("frameset", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "cols",
            "rows",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Q(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - cite
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("q", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "cite",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Data(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("data", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Progress(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - max
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("progress", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "max",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Label(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - for
       - form
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("label", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "for",
            "form",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H1(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h1", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Li(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - type
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("li", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "type",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Time(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - datetime
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("time", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "datetime",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Ul(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - compact
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ul", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "compact",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class P(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("p", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Frame(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - frameborder
       - longdesc
       - marginheight
       - marginwidth
       - name
       - noresize
       - scrolling
       - src
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("frame", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "frameborder",
            "longdesc",
            "marginheight",
            "marginwidth",
            "name",
            "noresize",
            "scrolling",
            "src",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Caption(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("caption", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Dl(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - compact
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dl", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "compact",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Fieldset(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - disabled
       - form
       - name
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("fieldset", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "disabled",
            "form",
            "name",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Pre(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("pre", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Track(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - default
       - kind
       - label
       - src
       - srclang
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("track", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "default",
            "kind",
            "label",
            "src",
            "srclang",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Span(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("span", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Isindex(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - prompt
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("isindex", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "prompt",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Legend(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("legend", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Dir(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - compact
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dir", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "compact",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Output(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - for
       - form
       - name
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("output", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "for",
            "form",
            "name",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Tbody(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - char
       - charoff
       - valign
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tbody", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "char",
            "charoff",
            "valign",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Thead(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - char
       - charoff
       - valign
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("thead", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "char",
            "charoff",
            "valign",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Col(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - char
       - charoff
       - span
       - valign
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("col", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "char",
            "charoff",
            "span",
            "valign",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Blockquote(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - cite
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("blockquote", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "cite",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Ol(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - compact
       - reversed
       - start
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ol", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "compact",
            "reversed",
            "start",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Param(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - name
       - type
       - value
       - valuetype
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("param", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "name",
            "type",
            "value",
            "valuetype",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Br(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - clear
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("br", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "clear",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Map(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - name
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("map", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "name",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H5(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h5", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Div(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("div", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Ins(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - cite
       - datetime
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ins", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "cite",
            "datetime",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Table(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - bgcolor
       - border
       - cellpadding
       - cellspacing
       - frame
       - rules
       - summary
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("table", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "bgcolor",
            "border",
            "cellpadding",
            "cellspacing",
            "frame",
            "rules",
            "summary",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Form(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - accept
       - accept-charset
       - action
       - autocomplete
       - enctype
       - method
       - name
       - novalidate
       - target
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("form", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "accept",
            "accept-charset",
            "action",
            "autocomplete",
            "enctype",
            "method",
            "name",
            "novalidate",
            "target",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Meter(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - high
       - low
       - max
       - min
       - optimum
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("meter", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "high",
            "low",
            "max",
            "min",
            "optimum",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Style(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - media
       - type
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("style", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "media",
            "type",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Iframe(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - allow
       - allowfullscreen
       - allowpaymentrequest
       - allowusermedia
       - frameborder
       - height
       - loading
       - longdesc
       - marginheight
       - marginwidth
       - name
       - referrerpolicy
       - sandbox
       - scrolling
       - src
       - srcdoc
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("iframe", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "allow",
            "allowfullscreen",
            "allowpaymentrequest",
            "allowusermedia",
            "frameborder",
            "height",
            "loading",
            "longdesc",
            "marginheight",
            "marginwidth",
            "name",
            "referrerpolicy",
            "sandbox",
            "scrolling",
            "src",
            "srcdoc",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Body(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - alink
       - background
       - bgcolor
       - link
       - text
       - vlink
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("body", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "alink",
            "background",
            "bgcolor",
            "link",
            "text",
            "vlink",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Html(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - manifest
       - version
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("html", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "manifest",
            "version",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Tr(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - bgcolor
       - char
       - charoff
       - valign
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tr", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "bgcolor",
            "char",
            "charoff",
            "valign",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Dialog(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - open
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dialog", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "open",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Applet(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - alt
       - archive
       - code
       - codebase
       - height
       - hspace
       - name
       - object
       - vspace
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("applet", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "alt",
            "archive",
            "code",
            "codebase",
            "height",
            "hspace",
            "name",
            "object",
            "vspace",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Input(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - accept
       - align
       - alt
       - autocomplete
       - checked
       - dirname
       - disabled
       - form
       - formaction
       - formenctype
       - formmethod
       - formnovalidate
       - formtarget
       - height
       - ismap
       - list
       - max
       - maxlength
       - min
       - minlength
       - multiple
       - name
       - pattern
       - placeholder
       - readonly
       - required
       - size
       - src
       - step
       - type
       - usemap
       - value
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("input", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "accept",
            "align",
            "alt",
            "autocomplete",
            "checked",
            "dirname",
            "disabled",
            "form",
            "formaction",
            "formenctype",
            "formmethod",
            "formnovalidate",
            "formtarget",
            "height",
            "ismap",
            "list",
            "max",
            "maxlength",
            "min",
            "minlength",
            "multiple",
            "name",
            "pattern",
            "placeholder",
            "readonly",
            "required",
            "size",
            "src",
            "step",
            "type",
            "usemap",
            "value",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Option(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - disabled
       - label
       - selected
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("option", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "disabled",
            "label",
            "selected",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Button(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - disabled
       - form
       - formaction
       - formenctype
       - formmethod
       - formnovalidate
       - formtarget
       - name
       - type
       - value
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("button", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "disabled",
            "form",
            "formaction",
            "formenctype",
            "formmethod",
            "formnovalidate",
            "formtarget",
            "name",
            "type",
            "value",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H3(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h3", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Slot(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - name
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("slot", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "name",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Canvas(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - height
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("canvas", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "height",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Object(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - archive
       - border
       - classid
       - codebase
       - codetype
       - data
       - declare
       - form
       - height
       - hspace
       - name
       - standby
       - type
       - typemustmatch
       - usemap
       - vspace
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("object", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "archive",
            "border",
            "classid",
            "codebase",
            "codetype",
            "data",
            "declare",
            "form",
            "height",
            "hspace",
            "name",
            "standby",
            "type",
            "typemustmatch",
            "usemap",
            "vspace",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Th(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - abbr
       - align
       - axis
       - bgcolor
       - char
       - charoff
       - colspan
       - headers
       - height
       - nowrap
       - rowspan
       - scope
       - valign
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("th", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "abbr",
            "align",
            "axis",
            "bgcolor",
            "char",
            "charoff",
            "colspan",
            "headers",
            "height",
            "nowrap",
            "rowspan",
            "scope",
            "valign",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Img(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - alt
       - border
       - crossorigin
       - decoding
       - height
       - hspace
       - ismap
       - loading
       - longdesc
       - name
       - referrerpolicy
       - sizes
       - src
       - srcset
       - usemap
       - vspace
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("img", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "alt",
            "border",
            "crossorigin",
            "decoding",
            "height",
            "hspace",
            "ismap",
            "loading",
            "longdesc",
            "name",
            "referrerpolicy",
            "sizes",
            "src",
            "srcset",
            "usemap",
            "vspace",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class B(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("b", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Select(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - autocomplete
       - disabled
       - form
       - multiple
       - name
       - required
       - size
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("select", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "autocomplete",
            "disabled",
            "form",
            "multiple",
            "name",
            "required",
            "size",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Head(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - profile
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("head", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "profile",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H2(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h2", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Textarea(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - autocomplete
       - cols
       - dirname
       - disabled
       - form
       - maxlength
       - minlength
       - name
       - placeholder
       - readonly
       - required
       - rows
       - wrap
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("textarea", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "autocomplete",
            "cols",
            "dirname",
            "disabled",
            "form",
            "maxlength",
            "minlength",
            "name",
            "placeholder",
            "readonly",
            "required",
            "rows",
            "wrap",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class I(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("i", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Colgroup(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - char
       - charoff
       - span
       - valign
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("colgroup", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "char",
            "charoff",
            "span",
            "valign",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Audio(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - autoplay
       - controls
       - crossorigin
       - loop
       - muted
       - preload
       - src
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("audio", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "autoplay",
            "controls",
            "crossorigin",
            "loop",
            "muted",
            "preload",
            "src",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Optgroup(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - disabled
       - label
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("optgroup", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "disabled",
            "label",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Td(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - abbr
       - align
       - axis
       - bgcolor
       - char
       - charoff
       - colspan
       - headers
       - height
       - nowrap
       - rowspan
       - scope
       - valign
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("td", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "abbr",
            "align",
            "axis",
            "bgcolor",
            "char",
            "charoff",
            "colspan",
            "headers",
            "height",
            "nowrap",
            "rowspan",
            "scope",
            "valign",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Base(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - href
       - target
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("base", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "href",
            "target",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Menu(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - compact
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("menu", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "compact",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Tfoot(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
       - char
       - charoff
       - valign
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tfoot", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
            "char",
            "charoff",
            "valign",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Meta(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - charset
       - content
       - http-equiv
       - media
       - name
       - scheme
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("meta", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "charset",
            "content",
            "http-equiv",
            "media",
            "name",
            "scheme",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Details(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - open
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("details", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "open",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Embed(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - height
       - src
       - type
       - width
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("embed", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "height",
            "src",
            "type",
            "width",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class H4(HtmlElement):
    """
    Properties:
       - accesskey
       - autocapitalize
       - autofocus
       - classes
       - contenteditable
       - dir
       - draggable
       - enterkeyhint
       - hidden
       - id
       - inputmode
       - is
       - itemid
       - itemprop
       - itemref
       - itemscope
       - itemtype
       - lang
       - nonce
       - slot
       - spellcheck
       - style
       - tabindex
       - title
       - translate
       - ref
       - key
       - v_on
       - v_bind
       - v_text
       - v_html
       - v_show
       - v_if
       - v_else
       - v_else_if
       - v_for
       - v_model
       - v_pre
       - v_once
       - align
    Events:
       - click
       - mousedown
       - mouseup
       - mouseenter
       - mouseleave
       - contextmenu
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h4", children, **kwargs)
        self._attr_names += [
            "accesskey",
            "autocapitalize",
            "autofocus",
            ["classes", "class"],
            "contenteditable",
            "dir",
            "draggable",
            "enterkeyhint",
            "hidden",
            "id",
            "inputmode",
            "is",
            "itemid",
            "itemprop",
            "itemref",
            "itemscope",
            "itemtype",
            "lang",
            "nonce",
            "slot",
            "spellcheck",
            "style",
            "tabindex",
            "title",
            "translate",
            "ref",
            ["key", ":key"],
            ["v_on", "v-on"],
            ["v_bind", "v-bind"],
            "v_text",
            "v_html",
            "v_show",
            "v_if",
            "v_else",
            "v_else_if",
            "v_for",
            "v_model",
            "v_pre",
            "v_once",
            "align",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]
