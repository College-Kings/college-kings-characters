from game.characters.character_traits_ren import CharacterTrait
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

ryan: NonPlayableCharacter

"""renpy
init python:
"""


class Charli(NonPlayableCharacter, object):
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
        return _("Charli")

    @property
    def username(self) -> str:
        return _("CharliAndTheCockFactory")

    @property
    def traits(self) -> CharacterTrait:
        return CharacterTrait.COMPETITIVE
