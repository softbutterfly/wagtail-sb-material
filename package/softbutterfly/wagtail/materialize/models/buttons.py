# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.blocks import URLBlock

from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class BaseButtonBlock(MaterializeComponentBase):
    class Meta:
        template = "wagtail/materialize/components/button.html"
        icon = 'placeholder'


class URLButtonBlock(BaseButtonBlock):
    text = RawHTMLBlock(
        label=_("Text"),
    )

    link = URLBlock(
        label=_("URL"),
    )

    disabled = BooleanBlock(
        label=_("Disabled"),
        required=False,
    )

    flat = BooleanBlock(
        label=_("Flat"),
        required=False,
    )

    large = BooleanBlock(
        label=_("Large"),
        required=False,
    )

    class Meta:
        label = _("Botón a URL")

    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_url'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_bookmark'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_page'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_document'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_image'] = True
        return context


class BookmarkButtonBlock(BaseButtonBlock):
    text = RawHTMLBlock(
        label=_("Text"),
    )

    link = CharBlock(
        label=_("Marcador"),
    )

    disabled = BooleanBlock(
        label=_("Disabled"),
        required=False,
    )

    flat = BooleanBlock(
        label=_("Flat"),
        required=False,
    )

    large = BooleanBlock(
        label=_("Large"),
        required=False,
    )

    class Meta:
        label = _("Botón a marcador")

    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_url'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_bookmark'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_page'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_document'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_image'] = True
        return context


class PageButtonBlock(BaseButtonBlock):
    text = RawHTMLBlock(
        label=_("Text"),
    )

    link = PageChooserBlock(
        label=_("Página"),
    )

    disabled = BooleanBlock(
        label=_("Disabled"),
        required=False,
    )

    flat = BooleanBlock(
        label=_("Flat"),
        required=False,
    )

    large = BooleanBlock(
        label=_("Large"),
        required=False,
    )

    class Meta:
        label = _("Botón a página")

    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_url'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_bookmark'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_page'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_document'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_image'] = True
        return context


class DocumentButtonBlock(BaseButtonBlock):
    text = RawHTMLBlock(
        label=_("Text"),
    )

    link = DocumentChooserBlock(
        label=("Documento"),
    )

    disabled = BooleanBlock(
        label=_("Disabled"),
        required=False,
    )

    flat = BooleanBlock(
        label=_("Flat"),
        required=False,
    )

    large = BooleanBlock(
        label=_("Large"),
        required=False,
    )

    class Meta:
        label = _("Botón a documento")

    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_url'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_bookmark'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_page'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_document'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_image'] = True
        return context


class ImageButtonBlock(BaseButtonBlock):
    text = RawHTMLBlock(
        label=_("Text"),
    )

    link = ImageChooserBlock(
        label=("Imagen"),
    )

    disabled = BooleanBlock(
        label=_("Disabled"),
        required=False,
    )

    flat = BooleanBlock(
        label=_("Flat"),
        required=False,
    )

    large = BooleanBlock(
        label=_("Large"),
        required=False,
    )

    class Meta:
        label = _("Botón a imagen")

    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_url'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_bookmark'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_page'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_document'] = True
        return context
    def get_context(self, request):
        context = super(BaseButtonBlock, self).get_context(request)
        context['button_to_image'] = True
        return context


class ButtonsStreamBlock(MaterializeStreamBase):
    url_button = URLButtonBlock()
    bookmark_button = BookmarkButtonBlock()
    page_button = PageButtonBlock()
    document_button = DocumentButtonBlock()
    image_button = ImageButtonBlock()

    class Meta:
        icon = 'cogs'
        label = _("Buttons")
