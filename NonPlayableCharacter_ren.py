from typing import Protocol, runtime_checkable

from renpy import config

from game.characters.character_ren import Character
from game.characters.character_traits_ren import CharacterTrait
from game.characters.CharacterService_ren import CharacterService
from game.phone.Message_ren import Message

name: str

"""renpy
init python:
"""


@runtime_checkable
class NonPlayableCharacter(Character, Protocol):
    pending_text_messages: list["Message"]
    text_messages: list["Message"]

    pending_simplr_messages: list["Message"]
    simplr_messages: list["Message"]

    points: int = 0

    @property
    def name(self) -> str:
        try:
            return self.__dict__["name"]
        except KeyError:
            return ""

    @property
    def username(self) -> str:
        try:
            return self.__dict__["username"]
        except KeyError:
            return ""

    @property
    def profile_pictures(self) -> tuple[str, ...]:
        return CharacterService.get_profile_pictures(self.name.lower())

    @property
    def traits(self) -> "CharacterTrait":
        return CharacterTrait(0)

    @property
    def vindictive_characters(self) -> tuple["NonPlayableCharacter", ...]:
        return ()

    @property
    def is_competitive(self) -> bool:
        return CharacterTrait.COMPETITIVE in self.traits

    @property
    def is_talkative(self) -> bool:
        return CharacterTrait.TALKATIVE in self.traits


config.ex_rollback_classes.append(NonPlayableCharacter)
