# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import BooleanBlock
from wagtail.core.blocks import CharBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.blocks import RawHTMLBlock
from wagtail.core.blocks import URLBlock

from wagtail.documents.blocks import DocumentChooserBlock

from wagtail.images.blocks import ImageChooserBlock

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase


class ButtonBase(MaterializeComponentBase):
    contents = RawHTMLBlock(
        label=_("Text"),
    )

    materialize_tag = 'a'
    materialize_class = 'btn'

    class Meta:
        template = "wagtail/materialize/components/button.html"
        icon = 'placeholder'


class ButtonToURL(ButtonBase):
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
        context = super(ButtonBase, self).get_context(request)
        context['button_to_url'] = True
        return context


class ButtonToBookmark(ButtonBase):
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
        context = super(ButtonBase, self).get_context(request)
        context['button_to_bookmark'] = True
        return context


class ButtonToPage(ButtonBase):
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
        context = super(ButtonBase, self).get_context(request)
        context['button_to_page'] = True
        return context


class ButtonToDocument(ButtonBase):
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
        context = super(ButtonBase, self).get_context(request)
        context['button_to_document'] = True
        return context


class ButtonToImage(ButtonBase):
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
        context = super(ButtonBase, self).get_context(request)
        context['button_to_image'] = True
        return context


class ButtonStream(MaterializeStreamBase):
    url_button = ButtonToURL()
    bookmark_button = ButtonToBookmark()
    page_button = ButtonToPage()
    document_button = ButtonToDocument()
    image_button = ButtonToImage()

    class Meta:
        label = _("Buttons")
