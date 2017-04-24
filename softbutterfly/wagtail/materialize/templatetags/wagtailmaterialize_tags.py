# -*- encoding: utf-8 -*-
from django import template

from wagtail.wagtailcore.models import Page

from ..models import MaterialPage


register = template.Library()


"""
Template tags to get from HTMLAttributes (stream block)
"""


@register.simple_tag
def get_tag(blocks):
    """
    Template tag to get the html tag.

    Search for every block and return the first block with block_type 'tag'
    """
    for block in blocks:
        if block.block_type == 'tag':
            return block

    return ''


@register.simple_tag
def get_id(blocks):
    """
    Template tag to get the html id.

    Search for every block and return the first block with block_type 'identifier'
    """
    for block in blocks:
        if block.block_type == 'identifier':
            return block

    return ''


@register.simple_tag
def get_classes(blocks):
    """
    Template tag to get the html classes.

    Search for every block and return the first block with block_type 'classes'
    """
    for block in blocks:
        if block.block_type == 'classes':
            return block

    return ''


@register.simple_tag
def get_attributes(blocks):
    """
    Template tag to get other html attributes.

    Search for every block, join the blocks with block_type 'tag' and return
    them in a list.
    """
    attributes = []

    for block in blocks:
        if block.block_type == 'attribute':
            attributes.append(block)

    return attributes


@register.filter
def get_footer(page):
    """
    Template tag to get other html attributes.
    """
    root_page = Page.objects.ancestor_of(page, inclusive=True).type(MaterialPage).first()
    return root_page.footer


"""
Site strcuture template tags

To be moved to softubtterfly-wagtail-utilities
"""


@register.simple_tag
def make_use_of(var):
    return var


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def has_menu_children(context, page):
    return page.get_children().live().in_menu().exists()


@register.assignment_tag(takes_context=True)
def get_menu_children(context, page):
    return page.get_children().live().in_menu()
