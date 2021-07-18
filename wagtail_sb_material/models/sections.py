# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import BooleanBlock

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class Section(MaterializeComponentBase):
    contents = ''

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

    materialize_tag = 'section'
    materialize_class = 'section'

    class Meta:
        template = 'wagtail/materialize/components/section.html'
        label = _("Section")


class SectionStream(MaterializeStreamBase):
    section = Section()

    class Meta:
        label = _("Sections")
