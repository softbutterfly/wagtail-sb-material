# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from .base import MaterializeStreamBase
from .base import MaterializeStructBase

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

from .buttons import ButtonToURL
from .buttons import ButtonToBookmark
from .buttons import ButtonToPage
from .buttons import ButtonToDocument
from .buttons import ButtonToImage

from .helpers import Space
from .helpers import PromotedIcon

from .grid import Container
from .grid import Column
from .grid import Row

from .section import Section

from .parallax import Parallax


class TextStream(MaterializeStreamBase):
    h1 = Heading1()
    h2 = Heading2()
    h3 = Heading3()
    h4 = Heading4()
    h5 = Heading5()
    h6 = Heading6()
    paragraph = Paragraph()

    class Meta:
        label = _("Text stream")


class MultimediaStream(MaterializeStreamBase):
    class Meta:
        label = _("Multimedia stream")


class CardStream(MaterializeStreamBase):
    card = Card()
    panel_card = PanelCard()
    image_card = ImageCard()
    reveal_card = RevealCard()

    class Meta:
        label = _("Card stream")


class Body(MaterializeStreamBase):
    parallax = Parallax()
    section = Section()
    container = Container()

    class Meta:
        label = _("Body")
        icon = 'cog'
