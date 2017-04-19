# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import RawHTMLBlock

from wagtail.wagtaildocs.blocks import DocumentChooserPanel

from wagtail.wagtailimages.blocks import ImageChooserPanel

from .base import MaterializeBaseStructBlock


class MaterialBoxedImage(MaterializeBaseStructBlock):
    image = ImageChooserPanel(
        label=_("Image")
    )

    caption = RawHTMLBlock(
        label=_("Caption"),
        required=False,
    )

    class Meta:
        label = _("Material boxed image")
        icon = 'image'


class MaterialDownloadDocument(MaterializeBaseStructBlock):
    document = DocumentChooserPanel(
        label=_("Image")
    )

    class Meta:
        label = _("Material download document")
        icon = 'doc-full'
