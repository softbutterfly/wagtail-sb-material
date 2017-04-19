# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from .base import MaterializeBaseStreamBlock

from .cards import Card
from .cards import PanelCard
from .cards import ImageCard
from .cards import RevealCard

from .typography import Heading1
from .typography import Heading2
from .typography import Heading3
from .typography import Heading4
from .typography import Heading5
from .typography import Heading6
from .typography import Paragraph
from .typography import TextStreamBlock

from .buttons import URLButtonBlock
from .buttons import BookmarkButtonBlock
from .buttons import PageButtonBlock
from .buttons import DocumentButtonBlock
from .buttons import ImageButtonBlock
from .buttons import ButtonsStreamBlock

from .pages import MaterialPageStarter
from .pages import MaterialPageParallax
from .pages import TestingPage

from .helpers import Spacer
from .helpers import HelpersStreamBlock

from .section import Section

from .parallax import Parallax


class TextStream(MaterializeBaseStreamBlock):
    h1 = Heading1()
    h2 = Heading2()
    h3 = Heading3()
    h4 = Heading4()
    h5 = Heading5()
    h6 = Heading6()
    paragraph = Paragraph()

    class Meta:
        label = _("Text stream")


class MultimediaStream(MaterializeBaseStreamBlock):
    class Meta:
        label = _("Multimedia stream")


class CardStream(MaterializeBaseStreamBlock):
    card = Card()
    panel_card = PanelCard()
    image_card = ImageCard()
    reveal_card = RevealCard()

    class Meta:
        label = _("Card stream")
