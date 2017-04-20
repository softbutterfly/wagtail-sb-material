# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class BaseGridElement(MaterializeComponentBase):
    materialize_tag = 'div'

    class Meta:
        template = "wagtail/materialize/components/grid.html"


class Column(BaseGridElement):
    materialize_class = 'col'

    class Meta:
        label = _("Column")


class ColumnStreamBlock(MaterializeStreamBase):
    column = Column()

    class Meta:
        label = _("Columns")


class Row(BaseGridElement):
    contents = ColumnStreamBlock()

    materialize_class = 'row'

    class Meta:
        label = _("Row")


class RowStreamBlock(MaterializeStreamBase):
    row = Row()

    class Meta:
        label = _("Rows")


class Container(BaseGridElement):
    contents = RowStreamBlock()

    materialize_class = 'container'

    class Meta:
        label = _("Contianer")


class ContainerStreamBlock(MaterializeStreamBase):
    container = Container()

    class Meta:
        label = _("Containers")
