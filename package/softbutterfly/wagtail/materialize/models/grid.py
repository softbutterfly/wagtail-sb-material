# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class GridComponentBase(MaterializeComponentBase):
    materialize_tag = 'div'

    class Meta:
        template = "wagtail/materialize/components/grid.html"


class Column(GridComponentBase):
    materialize_class = 'col'

    class Meta:
        label = _("Column")


class ColumnStream(MaterializeStreamBase):
    column = Column()

    class Meta:
        label = _("Columns")


class Row(GridComponentBase):
    contents = ColumnStream()

    materialize_class = 'row'

    class Meta:
        label = _("Row")


class RowStream(MaterializeStreamBase):
    row = Row()

    class Meta:
        label = _("Rows")


class Container(GridComponentBase):
    contents = RowStream()

    materialize_class = 'container'

    class Meta:
        label = _("Container")


class ContainerStream(MaterializeStreamBase):
    container = Container()

    class Meta:
        label = _("Containers")
