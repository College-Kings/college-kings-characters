from game.characters.Moods_ren import Moods
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

"""renpy
init python:
"""


class Faris(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.points = 0

        self.relationships = {}
        self.mood = Moods.NORMAL

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

    @property
    def name(self) -> str:
        return _("Faris")

    @property
    def username(self) -> str:
        return _("Faris")
