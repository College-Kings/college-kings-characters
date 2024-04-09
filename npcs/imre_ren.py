from typing import Any
from game.characters.character_traits_ren import CharacterTrait
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

ryan: NonPlayableCharacter

"""renpy
init python:
"""


class Imre(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.relationships = {}

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__init__()

        self.__dict__.update(state)

    @property
    def name(self) -> str:
        return _("Imre")

    @property
    def username(self) -> str:
        return _("BadBoyImre")

    @property
    def traits(self) -> CharacterTrait:
        return CharacterTrait(0)

    @property
    def vindictive_characters(self) -> tuple[NonPlayableCharacter, ...]:
        return (ryan,)
