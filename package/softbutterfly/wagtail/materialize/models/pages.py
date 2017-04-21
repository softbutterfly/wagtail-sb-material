# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from .base import MaterializeStreamBase
from .cards import Card
from .cards import PanelCard
from .cards import CardStream

from .typography import Heading1
from .typography import Heading2
from .typography import Heading3
from .typography import Heading4
from .typography import Heading5
from .typography import Heading6
from .typography import Paragraph
from .typography import TextStream

from .grid import Column
from .grid import ColumnStream
from .grid import Container
from .grid import ContainerStream
from .grid import Row
from .grid import RowStream

from .buttons import ButtonStream

from .parallax import Parallax

from .sections import Section

from .helpers import Space
from .helpers import HelpersStream

from .footer import Footer
from .branding import BrandLogo

from .base import HTMLAttributes


class MaterialPage(Page):
    navbar_attributes = StreamField(
        HTMLAttributes(),
        verbose_name=_("Navigation bar attributes"),
        blank=True,
    )

    navbar_fixed = models.BooleanField(
        _("Fixed"),
        default=False,
    )

    brand = models.ForeignKey(
        BrandLogo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = ''

    footer = models.ForeignKey(
        Footer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Settings fields
    include_preloader = models.BooleanField(
        _("Include preloader"),
        help_text=_("A material style preloader will be included in your page"),
        default=False,
    )

    enable_perfect_scrollbar = models.BooleanField(
        _("Enable Perfect Scrollbar"),
        help_text=_("Fancy scroll bar provided by PerfectScrollbar.js will be enabled"),
        default=False,
    )

    enable_font_awesome = models.BooleanField(
        _("Enable FontAwesome"),
        help_text=_("Enalble aditional icons provided by FontAwesome"),
        default=True,
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel('brand'),
        SnippetChooserPanel('footer'),
    ]

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
class Contents(CardStream, TextStream, ButtonStream, HelpersStream):
    class Meta:
        label = _("Contents")


# Starter Template -------------------------------------------------------------
class StarterColumn(Column):
    contents = Contents()


class StarterColumnStream(ColumnStream):
    column = StarterColumn()


class StarterRow(Row):
    contents = StarterColumnStream()


class StarterRowStream(RowStream):
    row = StarterRow()


class StarterContainer(Container):
    contents = StarterRowStream()


class StarterContainerStream(ContainerStream):
    container = StarterContainer()


class StarterParallax(Parallax):
    contents = StarterContainerStream()


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
        MultiFieldPanel(
            [
                SnippetChooserPanel('brand'),
                StreamFieldPanel('navbar_attributes'),
                FieldPanel('navbar_fixed'),
            ],
            _("Navigation bar")
        ),
        StreamFieldPanel('body'),
        SnippetChooserPanel('footer'),
    ]

    class Meta:
        verbose_name = _("Material Page Starter")


# Parallax Template ------------------------------------------------------------
class ParallaxColumnContents(Contents):
    pass


class ParallaxColumn(Column):
    contents = ParallaxColumnContents()


class ParallaxRowContents(ColumnStream):
    contents = Contents()
    column = ParallaxColumn()
    space = Space()

    class Meta:
        label = _("Row contents")


class ParallaxRow(Row):
    contents = ParallaxRowContents()


class ParallaxContainerContents(RowStream):
    contents = Contents()
    row = ParallaxRow()
    space = Space()

    class Meta:
        label = _("Container Contents")


class ParallaxContainer(Container):
    contents = ParallaxContainerContents()


class ParallaxSectionContents(MaterializeStreamBase):
    contents = Contents()
    container = ParallaxContainer()
    space = Space()

    class Meta:
        label = _("Section contents")


class ParallaxSection(Section):
    contents = ParallaxSectionContents()


class ParallaxParallaxContent(MaterializeStreamBase):
    section = ParallaxSection()
    space = Space()

    class Meta:
        label = _("Parallax contents")


class ParallaxParallax(Parallax):
    contents = ParallaxParallaxContent()


class ParallaxPageBody(MaterializeStreamBase):
    parallax = ParallaxParallax()
    section = ParallaxSection()
    space = Space()

    class Meta:
        label = _("Parllax page body")


class MaterialPageParallax(MaterialPage):
    template = 'wagtail/materialize/parallax-page.html'

    body = StreamField(
        ParallaxPageBody(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                SnippetChooserPanel('brand'),
                StreamFieldPanel('navbar_attributes'),
                FieldPanel('navbar_fixed'),
            ],
            _("Navigation bar")
        ),
        StreamFieldPanel('body'),
        SnippetChooserPanel('footer'),
    ]

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
        ('text', TextStream()),
        ('buttons', ButtonStream()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
