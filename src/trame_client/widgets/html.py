# Generated file - DO NOT EDIT
from .core import (
    VUE_CLIENT_TYPES,
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
    "A",
    "Abbr",
    "Address",
    "Area",
    "Article",
    "Aside",
    "Audio",
    "B",
    "Base",
    "Bdi",
    "Bdo",
    "Blockquote",
    "Body",
    "Br",
    "Button",
    "Canvas",
    "Caption",
    "Cite",
    "Code",
    "Col",
    "Colgroup",
    "Data",
    "Datalist",
    "Dd",
    "Del",
    "Details",
    "Dfn",
    "Dialog",
    "Div",
    "Dl",
    "Dt",
    "Em",
    "Embed",
    "Fieldset",
    "Figcaption",
    "Figure",
    "Footer",
    "Form",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Head",
    "Header",
    "Hgroup",
    "Hr",
    "Html",
    "I",
    "Iframe",
    "Img",
    "Input",
    "Ins",
    "Kbd",
    "Label",
    "Legend",
    "Li",
    "Link",
    "Main",
    "Map",
    "Mark",
    "Menu",
    "Meta",
    "Meter",
    "Nav",
    "Object",
    "Ol",
    "Optgroup",
    "Option",
    "Output",
    "P",
    "Param",
    "Picture",
    "Pre",
    "Progress",
    "Q",
    "Rp",
    "Rt",
    "Ruby",
    "S",
    "Samp",
    "Script",
    "Search",
    "Section",
    "Select",
    "Slot",
    "Small",
    "Source",
    "Span",
    "Strong",
    "Style",
    "Sub",
    "Summary",
    "Sup",
    "Svg",
    "Table",
    "Tbody",
    "Td",
    "Textarea",
    "Tfoot",
    "Th",
    "Thead",
    "Time",
    "Title",
    "Tr",
    "Track",
    "U",
    "Ul",
    "Var",
    "Video",
    "Wbr",
]


class A(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("a", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                ["charset", "charSet"],
                "coords",
                "download",
                "href",
                ["hreflang", "hrefLang"],
                "name",
                "ping",
                ["referrerpolicy", "referrerPolicy"],
                "rel",
                "rev",
                "shape",
                "target",
                "type",
            ]


class Abbr(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("abbr", children, **kwargs)


class Address(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("address", children, **kwargs)


class Area(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("area", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "alt",
                "coords",
                "download",
                "href",
                ["hreflang", "hrefLang"],
                "nohref",
                "ping",
                ["referrerpolicy", "referrerPolicy"],
                "rel",
                "shape",
                "target",
                "type",
            ]


class Article(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("article", children, **kwargs)


class Aside(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("aside", children, **kwargs)


class Audio(HtmlElement):
    """
    Properties:

    :param autoplay:
    :param controls:
    :param crossorigin:
    :param loop:
    :param muted:
    :param preload:
    :param src:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("audio", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "autoplay",
                "controls",
                "crossorigin",
                "loop",
                "muted",
                "preload",
                "src",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["autoplay", "autoPlay"],
                "controls",
                ["crossorigin", "crossOrigin"],
                "loop",
                "muted",
                "preload",
                "src",
            ]


class B(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("b", children, **kwargs)


class Base(HtmlElement):
    """
    Properties:

    :param href:
    :param target:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("base", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "href",
                "target",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "href",
                "target",
            ]


class Bdi(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("bdi", children, **kwargs)


class Bdo(HtmlElement):
    """
    Properties:

    :param dir:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("bdo", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "dir",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "dir",
            ]


class Blockquote(HtmlElement):
    """
    Properties:

    :param cite:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("blockquote", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "cite",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "cite",
            ]


class Body(HtmlElement):
    """
    Properties:

    :param alink:
    :param background:
    :param bgcolor:
    :param link:
    :param text:
    :param vlink:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("body", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "alink",
                "background",
                "bgcolor",
                "link",
                "text",
                "vlink",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "alink",
                "background",
                "bgcolor",
                "link",
                "text",
                "vlink",
            ]


class Br(HtmlElement):
    """
    Properties:

    :param clear:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("br", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "clear",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "clear",
            ]


class Button(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("button", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "disabled",
                "form",
                ["formaction", "formAction"],
                ["formenctype", "formEncType"],
                ["formmethod", "formMethod"],
                ["formnovalidate", "formNoValidate"],
                ["formtarget", "formTarget"],
                "name",
                "type",
                "value",
            ]


class Canvas(HtmlElement):
    """
    Properties:

    :param height:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("canvas", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "height",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "height",
                "width",
            ]


class Caption(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("caption", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class Cite(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("cite", children, **kwargs)


class Code(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("code", children, **kwargs)


class Col(HtmlElement):
    """
    Properties:

    :param align:
    :param char:
    :param charoff:
    :param span:
    :param valign:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("col", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "char",
                "charoff",
                "span",
                "valign",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "char",
                ["charoff", "charOff"],
                "span",
                "valign",
                "width",
            ]


class Colgroup(HtmlElement):
    """
    Properties:

    :param align:
    :param char:
    :param charoff:
    :param span:
    :param valign:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("colgroup", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "char",
                "charoff",
                "span",
                "valign",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "char",
                ["charoff", "charOff"],
                "span",
                "valign",
                "width",
            ]


class Data(HtmlElement):
    """
    Properties:

    :param value:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("data", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "value",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "value",
            ]


class Datalist(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("datalist", children, **kwargs)


class Dd(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dd", children, **kwargs)


class Del(HtmlElement):
    """
    Properties:

    :param cite:
    :param datetime:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("del", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "cite",
                "datetime",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "cite",
                ["datetime", "dateTime"],
            ]


class Details(HtmlElement):
    """
    Properties:

    :param open:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("details", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "open",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "open",
            ]


class Dfn(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dfn", children, **kwargs)


class Dialog(HtmlElement):
    """
    Properties:

    :param open:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dialog", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "open",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "open",
            ]


class Div(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("div", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class Dl(HtmlElement):
    """
    Properties:

    :param compact:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dl", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "compact",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "compact",
            ]


class Dt(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("dt", children, **kwargs)


class Em(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("em", children, **kwargs)


class Embed(HtmlElement):
    """
    Properties:

    :param height:
    :param src:
    :param type:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("embed", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "height",
                "src",
                "type",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "height",
                "src",
                "type",
                "width",
            ]


class Fieldset(HtmlElement):
    """
    Properties:

    :param disabled:
    :param form:
    :param name:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("fieldset", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "disabled",
                "form",
                "name",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "disabled",
                "form",
                "name",
            ]


class Figcaption(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("figcaption", children, **kwargs)


class Figure(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("figure", children, **kwargs)


class Footer(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("footer", children, **kwargs)


class Form(HtmlElement):
    """
    Properties:

    :param accept:
    :param accept_charset:
    :param action:
    :param autocomplete:
    :param enctype:
    :param method:
    :param name:
    :param novalidate:
    :param target:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("form", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "accept",
                ["accept_charset", "accept-charset"],
                "action",
                "autocomplete",
                "enctype",
                "method",
                "name",
                "novalidate",
                "target",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "accept",
                ["accept_charset", "acceptCharset"],
                "action",
                ["autocomplete", "autoComplete"],
                "enctype",
                "method",
                "name",
                ["novalidate", "noValidate"],
                "target",
            ]


class H1(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h1", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class H2(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h2", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class H3(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h3", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class H4(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h4", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class H5(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h5", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class H6(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("h6", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class Head(HtmlElement):
    """
    Properties:

    :param profile:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("head", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "profile",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "profile",
            ]


class Header(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("header", children, **kwargs)


class Hgroup(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("hgroup", children, **kwargs)


class Hr(HtmlElement):
    """
    Properties:

    :param align:
    :param noshade:
    :param size:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("hr", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "noshade",
                "size",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "noshade",
                "size",
                "width",
            ]


class Html(HtmlElement):
    """
    Properties:

    :param manifest:
    :param version:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("html", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "manifest",
                "version",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "manifest",
                "version",
            ]


class I(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("i", children, **kwargs)


class Iframe(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("iframe", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "allow",
                ["allowfullscreen", "allowFullScreen"],
                ["allowpaymentrequest", "allowPaymentRequest"],
                ["allowusermedia", "allowUserMedia"],
                ["frameborder", "frameBorder"],
                "height",
                "loading",
                ["longdesc", "longDesc"],
                ["marginheight", "marginHeight"],
                ["marginwidth", "marginWidth"],
                "name",
                ["referrerpolicy", "referrerPolicy"],
                "sandbox",
                "scrolling",
                "src",
                ["srcdoc", "srcDoc"],
                "width",
            ]


class Img(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("img", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "alt",
                "border",
                ["crossorigin", "crossOrigin"],
                "decoding",
                "height",
                "hspace",
                ["ismap", "isMap"],
                "loading",
                ["longdesc", "longDesc"],
                "name",
                ["referrerpolicy", "referrerPolicy"],
                "sizes",
                "src",
                ["srcset", "srcSet"],
                ["usemap", "useMap"],
                "vspace",
                "width",
            ]


class Input(HtmlElement):
    """
    Properties:

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
    :param width:
    :param webkitdirectory:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("input", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
                "webkitdirectory",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "accept",
                "align",
                "alt",
                ["autocomplete", "autoComplete"],
                "checked",
                ["dirname", "dirName"],
                "disabled",
                "form",
                ["formaction", "formAction"],
                ["formenctype", "formEncType"],
                ["formmethod", "formMethod"],
                ["formnovalidate", "formNoValidate"],
                ["formtarget", "formTarget"],
                "height",
                ["ismap", "isMap"],
                "list",
                "max",
                ["maxlength", "maxLength"],
                "min",
                ["minlength", "minLength"],
                "multiple",
                "name",
                "pattern",
                "placeholder",
                ["readonly", "readOnly"],
                "required",
                "size",
                "src",
                "step",
                "type",
                ["usemap", "useMap"],
                "value",
                "width",
                ["webkitdirectory", "webkitDirectory"],
            ]


class Ins(HtmlElement):
    """
    Properties:

    :param cite:
    :param datetime:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ins", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "cite",
                "datetime",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "cite",
                ["datetime", "dateTime"],
            ]


class Kbd(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("kbd", children, **kwargs)


class Label(HtmlElement):
    """
    Properties:

    :param for:
    :param form:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("label", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "for",
                "form",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["for", "htmlFor"],
                "form",
            ]


class Legend(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("legend", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class Li(HtmlElement):
    """
    Properties:

    :param type:
    :param value:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("li", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "type",
                "value",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "type",
                "value",
            ]


class Link(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("link", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "as",
                ["charset", "charSet"],
                "color",
                ["crossorigin", "crossOrigin"],
                "disabled",
                "href",
                ["hreflang", "hrefLang"],
                ["imagesizes", "imageSizes"],
                ["imagesrcset", "imageSrcSet"],
                "integrity",
                "media",
                ["referrerpolicy", "referrerPolicy"],
                "rel",
                "rev",
                "sizes",
                "target",
                "type",
            ]


class Main(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("main", children, **kwargs)


class Map(HtmlElement):
    """
    Properties:

    :param name:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("map", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "name",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "name",
            ]


class Mark(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mark", children, **kwargs)


class Menu(HtmlElement):
    """
    Properties:

    :param compact:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("menu", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "compact",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "compact",
            ]


class Meta(HtmlElement):
    """
    Properties:

    :param charset:
    :param content:
    :param http_equiv:
    :param media:
    :param name:
    :param scheme:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("meta", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "charset",
                "content",
                ["http_equiv", "http-equiv"],
                "media",
                "name",
                "scheme",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["charset", "charSet"],
                "content",
                ["http_equiv", "httpEquiv"],
                "media",
                "name",
                "scheme",
            ]


class Meter(HtmlElement):
    """
    Properties:

    :param high:
    :param low:
    :param max:
    :param min:
    :param optimum:
    :param value:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("meter", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "high",
                "low",
                "max",
                "min",
                "optimum",
                "value",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "high",
                "low",
                "max",
                "min",
                "optimum",
                "value",
            ]


class Nav(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("nav", children, **kwargs)


class Object(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("object", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "archive",
                "border",
                ["classid", "classID"],
                ["codebase", "codeBase"],
                ["codetype", "codeType"],
                "data",
                "declare",
                "form",
                "height",
                "hspace",
                "name",
                "standby",
                "type",
                ["typemustmatch", "typeMustMatch"],
                ["usemap", "useMap"],
                "vspace",
                "width",
            ]


class Ol(HtmlElement):
    """
    Properties:

    :param compact:
    :param reversed:
    :param start:
    :param type:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ol", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "compact",
                "reversed",
                "start",
                "type",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "compact",
                "reversed",
                "start",
                "type",
            ]


class Optgroup(HtmlElement):
    """
    Properties:

    :param disabled:
    :param label:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("optgroup", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "disabled",
                "label",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "disabled",
                "label",
            ]


class Option(HtmlElement):
    """
    Properties:

    :param disabled:
    :param label:
    :param selected:
    :param value:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("option", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "disabled",
                "label",
                "selected",
                "value",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "disabled",
                "label",
                "selected",
                "value",
            ]


class Output(HtmlElement):
    """
    Properties:

    :param for:
    :param form:
    :param name:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("output", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "for",
                "form",
                "name",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["for", "htmlFor"],
                "form",
                "name",
            ]


class P(HtmlElement):
    """
    Properties:

    :param align:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("p", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
            ]


class Param(HtmlElement):
    """
    Properties:

    :param name:
    :param type:
    :param value:
    :param valuetype:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("param", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "name",
                "type",
                "value",
                "valuetype",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "name",
                "type",
                "value",
                ["valuetype", "valueType"],
            ]


class Picture(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("picture", children, **kwargs)


class Pre(HtmlElement):
    """
    Properties:

    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("pre", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "width",
            ]


class Progress(HtmlElement):
    """
    Properties:

    :param max:
    :param value:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("progress", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "max",
                "value",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "max",
                "value",
            ]


class Q(HtmlElement):
    """
    Properties:

    :param cite:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("q", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "cite",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "cite",
            ]


class Rp(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("rp", children, **kwargs)


class Rt(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("rt", children, **kwargs)


class Ruby(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ruby", children, **kwargs)


class S(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("s", children, **kwargs)


class Samp(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("samp", children, **kwargs)


class Script(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("script", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "async",
                ["charset", "charSet"],
                ["crossorigin", "crossOrigin"],
                "defer",
                "integrity",
                "language",
                ["nomodule", "noModule"],
                ["referrerpolicy", "referrerPolicy"],
                "src",
                "type",
            ]


class Search(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("search", children, **kwargs)


class Section(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("section", children, **kwargs)


class Select(HtmlElement):
    """
    Properties:

    :param autocomplete:
    :param disabled:
    :param form:
    :param multiple:
    :param name:
    :param required:
    :param size:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("select", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "autocomplete",
                "disabled",
                "form",
                "multiple",
                "name",
                "required",
                "size",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["autocomplete", "autoComplete"],
                "disabled",
                "form",
                "multiple",
                "name",
                "required",
                "size",
            ]


class Slot(HtmlElement):
    """
    Properties:

    :param name:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("slot", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "name",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "name",
            ]


class Small(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("small", children, **kwargs)


class Source(HtmlElement):
    """
    Properties:

    :param height:
    :param media:
    :param sizes:
    :param src:
    :param srcset:
    :param type:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("source", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "height",
                "media",
                "sizes",
                "src",
                "srcset",
                "type",
                "width",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "height",
                "media",
                "sizes",
                "src",
                ["srcset", "srcSet"],
                "type",
                "width",
            ]


class Span(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("span", children, **kwargs)


class Strong(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("strong", children, **kwargs)


class Style(HtmlElement):
    """
    Properties:

    :param media:
    :param type:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("style", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "media",
                "type",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "media",
                "type",
            ]


class Sub(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("sub", children, **kwargs)


class Summary(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("summary", children, **kwargs)


class Sup(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("sup", children, **kwargs)


class Svg(HtmlElement):
    """
    Properties:

    :param width:
    :param height:
    :param xmlns:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("svg", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "width",
                "height",
                "xmlns",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "width",
                "height",
                "xmlns",
            ]


class Table(HtmlElement):
    """
    Properties:

    :param align:
    :param bgcolor:
    :param border:
    :param cellpadding:
    :param cellspacing:
    :param frame:
    :param rules:
    :param summary:
    :param width:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("table", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "bgcolor",
                "border",
                ["cellpadding", "cellPadding"],
                ["cellspacing", "cellSpacing"],
                "frame",
                "rules",
                "summary",
                "width",
            ]


class Tbody(HtmlElement):
    """
    Properties:

    :param align:
    :param char:
    :param charoff:
    :param valign:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tbody", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "char",
                "charoff",
                "valign",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "char",
                ["charoff", "charOff"],
                "valign",
            ]


class Td(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("td", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "abbr",
                "align",
                "axis",
                "bgcolor",
                "char",
                ["charoff", "charOff"],
                ["colspan", "colSpan"],
                "headers",
                "height",
                "nowrap",
                ["rowspan", "rowSpan"],
                "scope",
                "valign",
                "width",
            ]


class Textarea(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("textarea", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                ["autocomplete", "autoComplete"],
                "cols",
                ["dirname", "dirName"],
                "disabled",
                "form",
                ["maxlength", "maxLength"],
                ["minlength", "minLength"],
                "name",
                "placeholder",
                ["readonly", "readOnly"],
                "required",
                "rows",
                "wrap",
            ]


class Tfoot(HtmlElement):
    """
    Properties:

    :param align:
    :param char:
    :param charoff:
    :param valign:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tfoot", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "char",
                "charoff",
                "valign",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "char",
                ["charoff", "charOff"],
                "valign",
            ]


class Th(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("th", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                "abbr",
                "align",
                "axis",
                "bgcolor",
                "char",
                ["charoff", "charOff"],
                ["colspan", "colSpan"],
                "headers",
                "height",
                "nowrap",
                ["rowspan", "rowSpan"],
                "scope",
                "valign",
                "width",
            ]


class Thead(HtmlElement):
    """
    Properties:

    :param align:
    :param char:
    :param charoff:
    :param valign:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("thead", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "char",
                "charoff",
                "valign",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "char",
                ["charoff", "charOff"],
                "valign",
            ]


class Time(HtmlElement):
    """
    Properties:

    :param datetime:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("time", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "datetime",
            ]
        elif self.server.client_type == "react":
            self.props += [
                ["datetime", "dateTime"],
            ]


class Title(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("title", children, **kwargs)


class Tr(HtmlElement):
    """
    Properties:

    :param align:
    :param bgcolor:
    :param char:
    :param charoff:
    :param valign:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("tr", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "align",
                "bgcolor",
                "char",
                "charoff",
                "valign",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "align",
                "bgcolor",
                "char",
                ["charoff", "charOff"],
                "valign",
            ]


class Track(HtmlElement):
    """
    Properties:

    :param default:
    :param kind:
    :param label:
    :param src:
    :param srclang:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("track", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "default",
                "kind",
                "label",
                "src",
                "srclang",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "default",
                "kind",
                "label",
                "src",
                ["srclang", "srcLang"],
            ]


class U(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("u", children, **kwargs)


class Ul(HtmlElement):
    """
    Properties:

    :param compact:
    :param type:

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("ul", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
                "compact",
                "type",
            ]
        elif self.server.client_type == "react":
            self.props += [
                "compact",
                "type",
            ]


class Var(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("var", children, **kwargs)


class Video(HtmlElement):
    """
    Properties:

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

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("video", children, **kwargs)
        if self.server.client_type in VUE_CLIENT_TYPES:
            self.props += [
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
        elif self.server.client_type == "react":
            self.props += [
                ["autoplay", "autoPlay"],
                "controls",
                ["crossorigin", "crossOrigin"],
                "height",
                "loop",
                "muted",
                ["playsinline", "playsInline"],
                "poster",
                "preload",
                "src",
                "width",
            ]


class Wbr(HtmlElement):
    """
    No element-specific properties. See AbstractElement for the
    shared attributes/events available on every element.

    """

    def __init__(self, children=None, **kwargs):
        super().__init__("wbr", children, **kwargs)
