from abc import abstractmethod
from typing import Protocol, runtime_checkable
from game.characters.character_ren import Character
from game.characters.character_traits_ren import CharacterTrait


from game.characters.CharacterService_ren import CharacterService
from game.phone.Message_ren import Message

chloe: "NonPlayableCharacter"

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
    @abstractmethod
    def username(self) -> str:
        ...

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
