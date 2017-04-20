# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import StreamBlock


class MaterializeComponentMixin(object):
    """
    Mixin used to make default materialize css class and html tag for
    current component.
    """

    materialize_class = ''
    materialize_tag = ''

    def get_context(self, request):
        context = super(StructBlock, self).get_context(request)
        context['materialize_class'] = self.materialize_class
        context['materialize_tag'] = self.materialize_tag
        return context


class Tag(CharBlock):
    class Meta:
        label = _("Tag")
        icon = 'cog'


class ID(CharBlock):
    class Meta:
        template = 'wagtail/materialize/components/id.html'
        label = _("ID")
        icon = 'cog'


class Class(CharBlock):
    class Meta:
        label = _("Class")
        icon = 'cog'


class Attribute(StructBlock):
    attribute_name = CharBlock(
        label=_("Attribute name")
    )

    attribute_value = CharBlock(
        label=_("Attribute value"),
        required=False,
        default='',
    )

    class Meta:
        template = 'wagtail/materialize/components/attribute.html'
        label = _("Attribute")
        icon = 'cogs'


class HTMLAttributes(StreamBlock):
    tag = Tag()
    identifier = ID()
    classes = Class(label=_("Classes"))
    attribute = Attribute()

    class Meta:
        label = _("HTML attributes")
        icon = 'cogs'
        classname = 'full'


class MaterializeComponentBase(MaterializeComponentMixin, StructBlock):
    attributes = HTMLAttributes()

    class Meta:
        label = _("Base Material Struct Block")
        icon = "cog"
        classname = "full"


class MaterializeStreamBase(StreamBlock):
    class Meta:
        template = 'wagtail/materialize/components/materialize-stream-base.html'
        icon = "cogs"
        classname = "full"
