# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentMixin
from .base import MaterializeBaseStructBlock


class ParallaxImage(MaterializeComponentMixin, ImageChooserBlock):
    materialize_tag = 'div'
    materialize_class = 'parallax'

    class Meta:
        template = 'wagtail/materialize/components/parallax.html'
        label = _("Paralax image")
        icon = 'image'
        classname = 'full'


class Parallax(MaterializeBaseStructBlock):
    contents = ''
    image = ParallaxImage()
    full_screen = BooleanBlock(
        label=_("Full screen"),
        required=False,
    )

    materialize_tag = 'div'
    materialize_class = 'parallax-container'

    class Meta:
        template = 'wagtail/materialize/components/parallax.html'
        label = _("Parallax")
