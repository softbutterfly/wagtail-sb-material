# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import StreamBlock


class MaterializeComponentMixin(object):
    materialize_class = ''
    materialize_tag = ''

    def get_context(self, request):
        context = super(StructBlock, self).get_context(request)
        context['materialize_class'] = self.materialize_class
        context['materialize_tag'] = self.materialize_tag
        return context


class AttributeBlock(StructBlock):
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


class IDBlock(CharBlock):
    class Meta:
        template = 'wagtail/materialize/components/id.html'
        label = _("ID")
        icon = 'cog'


class ClassesBlock(CharBlock):
    class Meta:
        label = _("Classes")
        icon = 'cog'


class TagBlock(CharBlock):
    class Meta:
        label = _("Tag")
        icon = 'cog'


class HTMLTagAttributesStreamBlock(StreamBlock):
    tag = TagBlock(label=_("Tag"))
    identifier = IDBlock(label=_("Identifier"))
    classes = ClassesBlock(label=_("Classes"))
    attributes = AttributeBlock(label=_("Attributes"))

    class Meta:
        label = _("HTML Tag attributes")
        icon = 'cogs'
        classname = 'full'


class MaterializeBaseStructBlock(MaterializeComponentMixin, StructBlock):
    attributes = HTMLTagAttributesStreamBlock()

    class Meta:
        label = _("Base Material Struct Block")
        icon = "cog"
        classname = "full"


class MaterializeBaseStreamBlock(StreamBlock):
    class Meta:
        template = 'wagtail/materialize/components/materialize-base-stream-block.html'
        icon = "cogs"
        classname = "full"
