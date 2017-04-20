# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from .base import MaterializeStreamBase
from .cards import Card
from .cards import PanelCard
from .cards import CardsStreamBlock

from .typography import Heading1
from .typography import Heading2
from .typography import Heading3
from .typography import Heading4
from .typography import Heading5
from .typography import Heading6
from .typography import Paragraph
from .typography import TextStreamBlock

from .grid import Column
from .grid import ColumnStreamBlock
from .grid import Container
from .grid import ContainerStreamBlock
from .grid import Row
from .grid import RowStreamBlock

from .buttons import ButtonsStreamBlock

from .parallax import Parallax

from .helpers import HelpersStreamBlock


class MaterialPage(Page):
    # -*- Settings fields
    include_preloader = models.BooleanField(
        _("Include preloader"),
        help_text=_("A material style preloader will be included in your page"),
        default=True,
    )

    enable_perfect_scrollbar = models.BooleanField(
        _("Enable Perfect Scrollbar"),
        help_text=_("Fancy scroll bar provided by PerfectScrollbar.js will be enabled"),
        default=True,
    )

    enable_font_awesome = models.BooleanField(
        _("Enable FontAwesome"),
        help_text=_("Enalble aditional icons provided by FontAwesome"),
        default=False,
    )

    promote_panels = [
        MultiFieldPanel(
            Page.promote_panels,
            _("Common page configuration")
        ),
        MultiFieldPanel(
            [
                FieldPanel('include_preloader'),
                FieldPanel('enable_perfect_scrollbar'),
                FieldPanel('enable_font_awesome'),
            ],
            _("Material page configuration"),
        )
    ]

    class Meta:
        abstract = True


# Generic Content Stream Block -------------------------------------------------
class ContentStreamBlock(CardsStreamBlock, TextStreamBlock, ButtonsStreamBlock, HelpersStreamBlock):
    class Meta:
        label = _("Contents")


# Starter Template -------------------------------------------------------------
class StarterColumn(Column):
    contents = ContentStreamBlock()


class StarterColumnStreamBlock(ColumnStreamBlock):
    column = StarterColumn()


class StarterRow(Row):
    contents = StarterColumnStreamBlock()


class StarterRowStreamBlock(RowStreamBlock):
    row = StarterRow()


class StarterContainer(Container):
    contents = StarterRowStreamBlock()


class StarterContainerStreamBlock(ContainerStreamBlock):
    container = StarterContainer()


class StarterParallax(Parallax):
    contents = StarterContainerStreamBlock()


class StarterContent(MaterializeStreamBase):
    container = StarterContainer()
    parallax = StarterParallax()


class MaterialPageStarter(MaterialPage):
    template = 'wagtail/materialize/starter.html'

    body = StreamField(
        StarterContent(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _("Material Page Starter")


# Parallax Template ------------------------------------------------------------
class MaterialPageParallax(MaterialPage):
    template = 'wagtail/materialize/paralax.html'

    class Meta:
        verbose_name = _("Material Page Parallax")


# Article Template -------------------------------------------------------------
class MaterialPageArticle(MaterialPage):
    template = 'wagtail/materialize/article.html'

    class Meta:
        verbose_name = _("Material Page Blog")


# Testing Template -------------------------------------------------------------
class TestingPage(MaterialPage):
    template = 'wagtail/materialize/testing-page.html'

    body = StreamField([
        ('panel_card', PanelCard()),
        ('card', Card()),
        ('container', Container()),
        ('heading1', Heading1()),
        ('heading2', Heading2()),
        ('heading3', Heading3()),
        ('heading4', Heading4()),
        ('heading5', Heading5()),
        ('heading6', Heading6()),
        ('paragraph', Paragraph()),
        ('text', TextStreamBlock()),
        ('buttons', ButtonsStreamBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
