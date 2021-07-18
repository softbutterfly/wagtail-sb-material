# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import CharBlock
from wagtail.core.blocks import StructBlock
from wagtail.core.blocks import StreamBlock


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
    """
    Override CharBlock for HTML tag specific block

    <tag></tag>
    """

    class Meta:
        label = _("Tag")
        icon = 'cog'


class ID(CharBlock):
    """
    Override CharBlock for HTML id attribute specific block

    <tag id="ID"></tag>
    """

    class Meta:
        template = 'wagtail/materialize/components/id.html'
        label = _("ID")
        icon = 'cog'


class Class(CharBlock):
    """
    Override CharBlock for HTML class atribute specific block

    <tag id="ID" class="Classes"></tag>
    """

    class Meta:
        label = _("Class")
        icon = 'cog'


class Attribute(StructBlock):
    """
    Struct block for html attributes

    <tag id="ID" class="Classes" attribute_name="attribute_value"></tag>
    """

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
    """
    Stream block for attributes
    """

    tag = Tag()
    identifier = ID()
    classes = Class(label=_("Classes"))
    attribute = Attribute()

    class Meta:
        label = _("HTML attributes")
        icon = 'cogs'
        classname = 'full'


class MaterializeComponentBase(MaterializeComponentMixin, StructBlock):
    """
    Base component for Materialize Components
    """

    attributes = HTMLAttributes()

    class Meta:
        template = 'wagtail/materialize/components/materialize-component-base.html'
        label = _("Base Material Struct Block")
        icon = "cog"
        classname = "full"


class MaterializeStreamBase(StreamBlock):
    """
    Base Stream block of Materialize Components
    """

    class Meta:
        template = 'wagtail/materialize/components/materialize-stream-base.html'
        icon = "cogs"
        classname = "full"
