# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import URLBlock

from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeComponentBase
from .base import MaterializeStreamBase

from .helpers import Color
from .helpers import TextColor

from .typography import Paragraph


class CardImage(ImageChooserBlock):
    class Meta:
        label = _("Card image")


class CardTitle(MaterializeComponentBase):
    contents = CharBlock(
        label=_("Card title")
    )

    materialize_class = 'card-title'
    materialize_tag = 'span'

    class Meta:
        template = 'wagtail/materialize/components/card-title.html'
        label = _("Card title")


class CardContentStreamBlock(MaterializeStreamBase):
    paragraph = Paragraph()

    class Meta:
        label = _("Card content")


class CardActionBase(MaterializeComponentBase):
    contents = RawHTMLBlock(
        label=_("Text")
    )

    link = None

    materialize_class = ''
    materialize_tag = 'a'

    class Meta:
        template = 'wagtail/materialize/components/card-action.html'
        icon = "placeholder"


class CardActionToURL(CardActionBase):
    link = URLBlock(
        label=_("URL"),
        required=False,
    )

    class Meta:
        label = _("Acción a URL")

    def get_context(self, request):
        context = super(CardActionBase, self).get_context(request)
        context['action_to_url'] = True
        return context


class CardActionToBookmark(CardActionBase):
    link = CharBlock(
        label=_("Marcador"),
        required=False,
    )

    class Meta:
        label = _("Acción a marcador")

    def get_context(self, request):
        context = super(CardActionBase, self).get_context(request)
        context['action_to_bookmark'] = True
        return context


class CardActionToPage(CardActionBase):
    link = PageChooserBlock(
        label=_("Página"),
        required=False,
    )

    class Meta:
        label = _("Acción a página")

    def get_context(self, request):
        context = super(CardActionBase, self).get_context(request)
        context['action_to_page'] = True
        return context


class CardActionToDocument(CardActionBase):
    link = DocumentChooserBlock(
        label=("Documento"),
        required=False,
    )

    class Meta:
        label = _("Acción a documento")

    def get_context(self, request):
        context = super(CardActionBase, self).get_context(request)
        context['action_to_document'] = True
        return context


class CardActionToImage(CardActionBase):
    link = ImageChooserBlock(
        label=("Imagen"),
        required=False,
    )

    class Meta:
        label = _("Acción a imagen")

    def get_context(self, request):
        context = super(CardActionBase, self).get_context(request)
        context['action_to_image'] = True
        return context


class CardActiontream(MaterializeStreamBase):
    card_action_to_url = CardActionToURL()
    card_action_to_bookmark = CardActionToBookmark()
    card_action_to_page = CardActionToPage()
    card_action_to_document = CardActionToDocument()
    card_action_to_image = CardActionToImage()

    class Meta:
        icon = 'cogs'
        label = _("Card action")


class CardAction(MaterializeComponentBase):
    contents = CardActiontream()

    color = Color(
        required=False,
    )

    materialize_class = 'card-action'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card-actions.html'
        label = _("Card Actions")


_CARD_SIZE_CHOICES = [
    ('small', _("small")),
    ('medium', _("medium")),
    ('large', _("large")),
]


class CardSize(ChoiceBlock):
    choices = _CARD_SIZE_CHOICES

    class Meta:
        label = _("Card size")
        classname = 'full'


class PanelCard(MaterializeComponentBase):
    contents = CardContentStreamBlock()

    color = Color(
        required=False,
    )

    text_color = TextColor(
        required=False,
    )

    materialize_class = 'card-panel'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card-panel.html'
        label = _("Panel card")


class Card(MaterializeComponentBase):
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardAction()

    color = Color(
        required=False,
    )

    text_color = TextColor(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Card")


class ImageCard(MaterializeComponentBase):
    image = CardImage()
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardAction()
    size = CardSize(
        required=False
    )

    put_image_with_title = BooleanBlock(
        label=_("Put image with title"),
        required=False,
        default=False,
    )

    add_gradient_to_title = BooleanBlock(
        label=_("Add gradient to title"),
        required=False,
        default=False,
    )

    use_horizontal_style = BooleanBlock(
        label=_("Use horizontal style"),
        default=False,
        required=False,
    )

    color = Color(
        required=False,
    )

    text_color = TextColor(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Image Card")


class RevealCard(MaterializeComponentBase):
    image = CardImage()
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardAction()
    reveal_contents = CardContentStreamBlock(
        label=_("Reveal contents")
    )
    size = CardSize(
        required=False
    )

    put_image_with_title = BooleanBlock(
        label=_("Put image with title"),
        required=False,
        default=False,
    )

    add_gradient_to_title = BooleanBlock(
        label=_("Add gradient to title"),
        required=False,
        default=False,
    )

    use_sticky_action = BooleanBlock(
        label=_("Use sticky action"),
        required=False,
        default=False,
    )

    color = Color(
        required=False,
    )

    text_color = TextColor(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Reveal Card")


class CardsStreamBlock(StreamBlock):
    card = Card()
    panel_card = PanelCard()
    image_card = ImageCard()
    reveal_card = RevealCard()

    class Meta:
        label = _("Cards")
