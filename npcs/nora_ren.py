from game.characters.character_traits_ren import CharacterTrait
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

chloe: NonPlayableCharacter
chris: NonPlayableCharacter

"""renpy
init python:
"""


class Nora(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.relationships = {}

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

    @property
    def name(self) -> str:
        return _("Nora")

    @property
    def username(self) -> str:
        return _("Nora_12")

    @property
    def traits(self) -> CharacterTrait:
        return CharacterTrait.TALKATIVE

    @property
    def vindictive_characters(self) -> tuple[NonPlayableCharacter, ...]:
        return (chris, chloe)
