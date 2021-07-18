# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.fields import StreamField

from wagtail.snippets.models import register_snippet

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase

from .buttons import ButtonStream

from .cards import CardStream

from .grid import Column
from .grid import ColumnStream
from .grid import Container
from .grid import ContainerStream
from .grid import Row
from .grid import RowStream

from .helpers import HelpersStream
from .helpers import Space

from .typography import TextStream

from .base import HTMLAttributes


class Contents(CardStream, TextStream, ButtonStream, HelpersStream):
    class Meta:
        label = _("Contents")


class FooterColumnContents(Contents):
    pass


class FooterColumn(Column):
    contents = FooterColumnContents()


class FooterRowContents(ColumnStream):
    column = FooterColumn()
    space = Space()

    class Meta:
        label = _("Row contents")


class FooterRow(Row):
    contents = FooterRowContents()


class FooterContainerContents(RowStream):
    row = FooterRow()
    space = Space()

    class Meta:
        label = _("Container Contents")


class FooterContainer(Container):
    contents = FooterContainerContents()


class FooterContents(ContainerStream):
    container = FooterContainer()

    class Meta:
        label = _("Footer contents")


@register_snippet
class Footer(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=32,
        blank=True,
    )

    attributes = StreamField(
        HTMLAttributes(),
        verbose_name=_("Attributes"),
        blank=True,
    )

    contents = StreamField(
        FooterContents(),
        verbose_name=_("Contents"),
        blank=True,
    )

    copyright_text = models.TextField()

    tags = TaggableManager(blank=True)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('attributes'),
        StreamFieldPanel('contents'),
        FieldPanel('copyright_text'),
        FieldPanel('tags'),
    ]

    class Meta:
        verbose_name = _("Footer")
        verbose_name_plural = _("Footers")

    def __str__(self):
        return self.name or "Footer"
