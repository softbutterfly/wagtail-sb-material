# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .base import MaterializeBaseStructBlock
from .base import MaterializeBaseStreamBlock


class BaseGridElement(MaterializeBaseStructBlock):
    materialize_tag = 'div'

    class Meta:
        template = "wagtail/materialize/components/grid.html"


class Column(BaseGridElement):
    materialize_class = 'col'

    class Meta:
        label = _("Column")


class ColumnStreamBlock(MaterializeBaseStreamBlock):
    column = Column()

    class Meta:
        label = _("Columns")


class Row(BaseGridElement):
    contents = ColumnStreamBlock()

    materialize_class = 'row'

    class Meta:
        label = _("Row")


class RowStreamBlock(MaterializeBaseStreamBlock):
    row = Row()

    class Meta:
        label = _("Rows")


class Container(BaseGridElement):
    contents = RowStreamBlock()

    materialize_class = 'container'

    class Meta:
        label = _("Contianer")


class ContainerStreamBlock(MaterializeBaseStreamBlock):
    container = Container()

    class Meta:
        label = _("Containers")
