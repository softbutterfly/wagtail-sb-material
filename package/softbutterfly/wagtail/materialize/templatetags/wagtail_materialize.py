from django import template
from django.utils.six.moves.urllib.parse import urlencode

import hashlib

register = template.Library()


"""
Template tags for HTMLAttributes stream block processing
"""


@register.filter
def get_tag(blocks):
    """
    Template tag to retrieve the html tag.

    Search for every block and return the first block with block_type 'tag'
    """
    for block in blocks:
        if block.block_type == 'tag':
            return block

    return ''


@register.filter
def get_id(blocks):
    """
    Template tag to retrieve the html id.

    Search for every block and return the first block with block_type 'identifier'
    """
    for block in blocks:
        if block.block_type == 'identifier':
            return block

    return ''


@register.filter
def get_classes(blocks):
    """
    Template tag to retrieve the html classes.

    Search for every block and return the first block with block_type 'classes'
    """
    for block in blocks:
        if block.block_type == 'classes':
            return block

    return ''


@register.filter
def get_attributes(blocks):
    """
    Template tag to retrieve other html attributes.

    Search for every block, join the blocks with block_type 'tag' and return
    them in a list.
    """
    attributes = []

    for block in blocks:
        if block.block_type == 'attribute':
            attributes.append(block)

    return attributes



"""
"""

@register.assignment_tag(takes_context=True)
def get_gravatar_url(context, email, size=50):
    default = "blank"

    gravatar_url = "//www.gravatar.com/avatar/{hash}?{params}".format(
        hash=hashlib.md5(email.lower().encode('utf-8')).hexdigest(),
        params=urlencode({'s': int(size), 'd': default})
    )

    return gravatar_url


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


"""
# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")





# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('demo/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('demo/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves all live pages which are children of the calling page
#for standard index listing
@register.inclusion_tag(
    'demo/tags/standard_index_listing.html',
    takes_context=True
)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live()
    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Person feed for home page
@register.inclusion_tag(
    'demo/tags/person_listing_homepage.html',
    takes_context=True
)
def person_listing_homepage(context, count=2):
    people = PersonPage.objects.live().order_by('?')
    return {
        'people': people[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Blog feed for home page
@register.inclusion_tag(
    'demo/tags/blog_listing_homepage.html',
    takes_context=True
)
def blog_listing_homepage(context, count=2):
    blogs = BlogPage.objects.live().order_by('-date')
    return {
        'blogs': blogs[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Events feed for home page
@register.inclusion_tag(
    'demo/tags/event_listing_homepage.html',
    takes_context=True
)
def event_listing_homepage(context, count=2):
    events = EventPage.objects.live()
    events = events.filter(date_from__gte=date.today()).order_by('date_from')
    return {
        'events': events[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Advert snippets
@register.inclusion_tag('demo/tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'adverts': Advert.objects.select_related('page'),
        'request': context['request'],
    }


@register.inclusion_tag('demo/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }
"""


