# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentMixin
from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class ParallaxImage(MaterializeComponentMixin, ImageChooserBlock):
    class Meta:
        label = _("Paralax image")
        icon = 'image'
        classname = 'full'


class Parallax(MaterializeComponentBase):
    contents = 'Paralax Content'
    image = ParallaxImage()
    full_screen = BooleanBlock(
        label=_("Full screen"),
        required=False,
    )

    middle_align = BooleanBlock(
        label=_("Middle align"),
        required=False,
    )

    center_align = BooleanBlock(
        label=_("Center align"),
        required=False,
    )

    materialize_tag = 'div'
    materialize_class = 'parallax-container'

    class Meta:
        template = 'wagtail/materialize/components/parallax.html'
        label = _("Parallax")


class ParallaxStream(MaterializeStreamBase):
    parallax = Parallax()

    class Meta:
        label = _("Parallaxes")
