# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import RawHTMLBlock

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class BaseTypographyBlock(MaterializeComponentBase):
    """
    Base Block for text related blocks
    """
    class Meta:
        template = "wagtail/materialize/components/typography.html"


class BaseHeadingBlock(BaseTypographyBlock):
    contents = RawHTMLBlock(
        label=_("Heading")
    )

    class Meta:
        icon = "title"


class Heading1(BaseHeadingBlock):
    materialize_tag = 'h1'

    class Meta:
        label = "H1"


class Heading2(BaseHeadingBlock):
    materialize_tag = 'h2'

    class Meta:
        label = "H2"


class Heading3(BaseHeadingBlock):
    materialize_tag = 'h3'

    class Meta:
        label = "H3"


class Heading4(BaseHeadingBlock):
    materialize_tag = 'h4'

    class Meta:
        label = "H4"


class Heading5(BaseHeadingBlock):
    materialize_tag = 'h5'

    class Meta:
        label = "H5"


class Heading6(BaseHeadingBlock):
    materialize_tag = 'h6'

    class Meta:
        label = "H6"


class Paragraph(BaseTypographyBlock):
    contents = RawHTMLBlock(
        label=_("Paragraph")
    )

    materialize_tag = 'p'

    class Meta:
        icon = "pilcrow"
        label = _("Paragraph")


class TextStream(MaterializeStreamBase):
    h1 = Heading1()
    h2 = Heading2()
    h3 = Heading3()
    h4 = Heading4()
    h5 = Heading5()
    h6 = Heading6()
    paragraph = Paragraph()

    class Meta:
        icon = 'cogs'
        label = _("Text")
