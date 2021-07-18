# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel


from wagtail.snippets.models import register_snippet

from taggit.managers import TaggableManager

from .base import HTMLAttributes


@register_snippet
class BrandLogo(models.Model):
    name = models.CharField(
        _("name"),
        max_length=32,
    )

    attributes = StreamField(
        HTMLAttributes(),
        verbose_name=_("Attributes"),
        blank=True,
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    text = models.CharField(
        _("Text"),
        max_length=255,
        null=True,
        blank=True,
    )

    tags = TaggableManager(blank=True)

    panels = [
        FieldPanel('name'),
        MultiFieldPanel(
            [
                StreamFieldPanel('attributes'),
                ImageChooserPanel('image'),
                FieldPanel('text'),
            ],
            _("Brand")
        ),
        FieldPanel('tags'),
    ]

    class Meta:
        verbose_name = _("Brand logo")
        verbose_name_plural = _("Brand logos")

    def __str__(self):
        return self.name or "Brand logo"


"""
<a id="logo-container" href="#" class="brand-logo">
    Logo
</a>
"""
