# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentMixin
from .base import MaterializeBaseStructBlock


class Section(MaterializeBaseStructBlock):
    contents = ''

    materialize_tag = 'section'
    materialize_class = 'section'

    class Meta:
        template = 'wagtail/materialize/components/section.html'
        label = _("Section")
