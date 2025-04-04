from game.characters.Moods_ren import Moods
from game.characters.character_traits_ren import CharacterTrait
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

imre: NonPlayableCharacter

"""renpy
init python:
"""


class Ryan(NonPlayableCharacter, object):
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
        return _("Ryan")

    @property
    def username(self) -> str:
        return _("Ryanator")

    @property
    def traits(self) -> CharacterTrait:
        return CharacterTrait(0)

    @property
    def vindictive_characters(self) -> tuple[NonPlayableCharacter, ...]:
        return (imre,)
