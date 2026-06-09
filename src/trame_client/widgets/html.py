# Generated file - DO NOT EDIT
from .core import (
    HtmlElement,
    Template,
    Component,
    Transition,
    TransitionGroup,
    KeepAlive,
    Teleport,
    Suspense,
)
from .. import module

HtmlElement.MODULE = module

__all__ = [
    "Template",
    "Component",
    "Transition",
    "TransitionGroup",
    "KeepAlive",
    "Teleport",
    "Suspense",
    "Tr",
    "Form",
    "Hr",
    "Meta",
    "Link",
    "Rp",
    "Label",
    "Param",
    "Textarea",
    "P",
    "H4",
    "Iframe",
    "Canvas",
    "Table",
    "Caption",
    "A",
    "Div",
    "Span",
    "Style",
    "Meter",
    "Em",
    "Samp",
    "Img",
    "Dialog",
    "Kbd",
    "Output",
    "Video",
    "Q",
    "Address",
    "Base",
    "Mark",
    "Data",
    "Td",
    "Picture",
    "Ol",
    "Input",
    "Ruby",
    "Dfn",
    "Bdo",
    "Time",
    "Var",
    "Select",
    "Script",
    "Dd",
    "Dt",
    "Figcaption",
    "H6",
    "Code",
    "U",
    "Strong",
    "B",
    "Slot",
    "Area",
    "Section",
    "Hgroup",
    "Br",
    "Track",
    "Svg",
    "H3",
    "Legend",
    "Embed",
    "Rt",
    "Map",
    "Tbody",
    "H1",
    "Button",
    "Dl",
    "Bdi",
    "Sub",
    "Cite",
    "Aside",
    "Li",
    "Colgroup",
    "Html",
    "Audio",
    "I",
    "Datalist",
    "Nav",
    "Tfoot",
    "Main",
    "H5",
    "Summary",
    "Object",
    "Footer",
    "Figure",
    "Pre",
    "Source",
    "Th",
    "Body",
    "Thead",
    "Menu",
    "Title",
    "Header",
    "Blockquote",
    "Details",
    "Head",
    "Small",
    "Optgroup",
    "Ul",
    "H2",
    "Wbr",
    "Col",
    "Sup",
    "Option",
    "Search",
    "Ins",
    "Article",
    "Fieldset",
    "Abbr",
    "S",
    "Progress",
    "Del",
]


class Tr(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param bgcolor:
    :param char:
    :param charoff:
    :param valign:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Form(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param accept:
    :param accept-charset:
    :param action:
    :param autocomplete:
    :param enctype:
    :param method:
    :param name:
    :param novalidate:
    :param target:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Hr(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param noshade:
    :param size:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Meta(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param charset:
    :param content:
    :param http-equiv:
    :param media:
    :param name:
    :param scheme:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Link(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param as:
    :param charset:
    :param color:
    :param crossorigin:
    :param disabled:
    :param href:
    :param hreflang:
    :param imagesizes:
    :param imagesrcset:
    :param integrity:
    :param media:
    :param referrerpolicy:
    :param rel:
    :param rev:
    :param sizes:
    :param target:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Rp(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("rp", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param for:
    :param form:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Param(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param name:
    :param type:
    :param value:
    :param valuetype:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Textarea(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param autocomplete:
    :param cols:
    :param dirname:
    :param disabled:
    :param form:
    :param maxlength:
    :param minlength:
    :param name:
    :param placeholder:
    :param readonly:
    :param required:
    :param rows:
    :param wrap:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class P(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class H4(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Iframe(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param allow:
    :param allowfullscreen:
    :param allowpaymentrequest:
    :param allowusermedia:
    :param frameborder:
    :param height:
    :param loading:
    :param longdesc:
    :param marginheight:
    :param marginwidth:
    :param name:
    :param referrerpolicy:
    :param sandbox:
    :param scrolling:
    :param src:
    :param srcdoc:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Canvas(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param height:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Table(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param bgcolor:
    :param border:
    :param cellpadding:
    :param cellspacing:
    :param frame:
    :param rules:
    :param summary:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Caption(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class A(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param charset:
    :param coords:
    :param download:
    :param href:
    :param hreflang:
    :param name:
    :param ping:
    :param referrerpolicy:
    :param rel:
    :param rev:
    :param shape:
    :param target:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Div(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Span(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param media:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Meter(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param high:
    :param low:
    :param max:
    :param min:
    :param optimum:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Em(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("em", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Samp(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("samp", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param alt:
    :param border:
    :param crossorigin:
    :param decoding:
    :param height:
    :param hspace:
    :param ismap:
    :param loading:
    :param longdesc:
    :param name:
    :param referrerpolicy:
    :param sizes:
    :param src:
    :param srcset:
    :param usemap:
    :param vspace:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Dialog(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param open:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Kbd(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("kbd", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param for:
    :param form:
    :param name:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Video(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param autoplay:
    :param controls:
    :param crossorigin:
    :param height:
    :param loop:
    :param muted:
    :param playsinline:
    :param poster:
    :param preload:
    :param src:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Q(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param cite:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Address(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("address", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param href:
    :param target:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Mark(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mark", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Td(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param abbr:
    :param align:
    :param axis:
    :param bgcolor:
    :param char:
    :param charoff:
    :param colspan:
    :param headers:
    :param height:
    :param nowrap:
    :param rowspan:
    :param scope:
    :param valign:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Picture(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("picture", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param compact:
    :param reversed:
    :param start:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Input(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param accept:
    :param align:
    :param alt:
    :param autocomplete:
    :param checked:
    :param dirname:
    :param disabled:
    :param form:
    :param formaction:
    :param formenctype:
    :param formmethod:
    :param formnovalidate:
    :param formtarget:
    :param height:
    :param ismap:
    :param list:
    :param max:
    :param maxlength:
    :param min:
    :param minlength:
    :param multiple:
    :param name:
    :param pattern:
    :param placeholder:
    :param readonly:
    :param required:
    :param size:
    :param src:
    :param step:
    :param type:
    :param usemap:
    :param value:
    :param webkitdirectory:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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
            "webkitdirectory",
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


class Ruby(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ruby", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Dfn(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dfn", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Bdo(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param dir:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("bdo", children, **kwargs)
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
            "v_memo",
            "v_cloak",
            "dir",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param datetime:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Var(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("var", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param autocomplete:
    :param disabled:
    :param form:
    :param multiple:
    :param name:
    :param required:
    :param size:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Script(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param async:
    :param charset:
    :param crossorigin:
    :param defer:
    :param integrity:
    :param language:
    :param nomodule:
    :param referrerpolicy:
    :param src:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Dd(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dd", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Dt(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dt", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Figcaption(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("figcaption", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Code(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("code", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class U(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("u", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Strong(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("strong", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param name:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Area(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param alt:
    :param coords:
    :param download:
    :param href:
    :param hreflang:
    :param nohref:
    :param ping:
    :param referrerpolicy:
    :param rel:
    :param shape:
    :param target:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Section(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("section", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Hgroup(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("hgroup", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param clear:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Track(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param default:
    :param kind:
    :param label:
    :param src:
    :param srclang:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Svg(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param width:
    :param height:
    :param xmlns:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("svg", children, **kwargs)
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
            "v_memo",
            "v_cloak",
            "width",
            "height",
            "xmlns",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Legend(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Embed(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param height:
    :param src:
    :param type:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Rt(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("rt", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param name:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param char:
    :param charoff:
    :param valign:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class H1(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Button(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param disabled:
    :param form:
    :param formaction:
    :param formenctype:
    :param formmethod:
    :param formnovalidate:
    :param formtarget:
    :param name:
    :param type:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Dl(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param compact:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Bdi(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("bdi", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Sub(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("sub", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Cite(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("cite", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Aside(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("aside", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param type:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Colgroup(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param char:
    :param charoff:
    :param span:
    :param valign:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Html(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param manifest:
    :param version:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Audio(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param autoplay:
    :param controls:
    :param crossorigin:
    :param loop:
    :param muted:
    :param preload:
    :param src:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class I(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Datalist(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("datalist", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Nav(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("nav", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param char:
    :param charoff:
    :param valign:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Main(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("main", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Summary(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("summary", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param archive:
    :param border:
    :param classid:
    :param codebase:
    :param codetype:
    :param data:
    :param declare:
    :param form:
    :param height:
    :param hspace:
    :param name:
    :param standby:
    :param type:
    :param typemustmatch:
    :param usemap:
    :param vspace:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Footer(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("footer", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Figure(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("figure", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Source(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param height:
    :param media:
    :param sizes:
    :param src:
    :param srcset:
    :param type:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Th(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param abbr:
    :param align:
    :param axis:
    :param bgcolor:
    :param char:
    :param charoff:
    :param colspan:
    :param headers:
    :param height:
    :param nowrap:
    :param rowspan:
    :param scope:
    :param valign:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Body(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param alink:
    :param background:
    :param bgcolor:
    :param link:
    :param text:
    :param vlink:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Thead(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param char:
    :param charoff:
    :param valign:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Menu(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param compact:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Title(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("title", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class Header(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("header", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param cite:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Details(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param open:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Head(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param profile:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Small(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("small", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param disabled:
    :param label:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Ul(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param compact:
    :param type:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class H2(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Wbr(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("wbr", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param align:
    :param char:
    :param charoff:
    :param span:
    :param valign:
    :param width:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Sup(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("sup", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param disabled:
    :param label:
    :param selected:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Search(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("search", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param cite:
    :param datetime:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Article(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("article", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param disabled:
    :param form:
    :param name:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Abbr(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("abbr", children, **kwargs)
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
            "v_memo",
            "v_cloak",
        ]
        self._event_names += [
            "click",
            "mousedown",
            "mouseup",
            "mouseenter",
            "mouseleave",
            "contextmenu",
        ]


class S(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("s", children, **kwargs)
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
            "v_memo",
            "v_cloak",
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

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param max:
    :param value:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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


class Del(HtmlElement):
    """
    Properties:

    :param accesskey:
    :param autocapitalize:
    :param autofocus:
    :param classes:
    :param contenteditable:
    :param dir:
    :param draggable:
    :param enterkeyhint:
    :param hidden:
    :param id:
    :param inputmode:
    :param is:
    :param itemid:
    :param itemprop:
    :param itemref:
    :param itemscope:
    :param itemtype:
    :param lang:
    :param nonce:
    :param slot:
    :param spellcheck:
    :param style:
    :param tabindex:
    :param title:
    :param translate:
    :param ref:
    :param key:
    :param v_on:
    :param v_bind:
    :param v_text:
    :param v_html:
    :param v_show:
    :param v_if:
    :param v_else:
    :param v_else_if:
    :param v_for:
    :param v_model:
    :param v_pre:
    :param v_once:
    :param v_memo:
    :param v_cloak:
    :param cite:
    :param datetime:

    Events:

    :param click:
    :param mousedown:
    :param mouseup:
    :param mouseenter:
    :param mouseleave:
    :param contextmenu:

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
            "v_memo",
            "v_cloak",
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
