# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import RawHTMLBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentBase


class MaterialBoxedImage(MaterializeComponentBase):
    image = ImageChooserBlock(
        label=_("Image")
    )

    caption = RawHTMLBlock(
        label=_("Caption"),
        required=False,
    )

    class Meta:
        label = _("Material boxed image")
        icon = 'image'
