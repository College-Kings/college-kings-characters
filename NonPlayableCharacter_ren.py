from typing import Protocol, runtime_checkable

from renpy import config

from game.characters.character_ren import Character
from game.characters.character_traits_ren import CharacterTrait
from game.characters.CharacterService_ren import CharacterService
from game.phone.Message_ren import Message
from renpy.display.displayable import Displayable
from renpy.display.transform import Transform

name: str

"""renpy
init python:
"""


@runtime_checkable
class NonPlayableCharacter(Character, Protocol):
    _profile_pictures: tuple[str, ...]
    _profile_picture: str
    _profile_picture_65x65: "Displayable"

    pending_text_messages: list["Message"]
    text_messages: list["Message"]

    pending_simplr_messages: list["Message"]
    simplr_messages: list["Message"]

    points: int

    def __repr__(self) -> str:
        try:
            return f"{self.__class__.__name__}({self.name}, {self.username=}, {self.profile_picture=}, {self.profile_pictures=}, {self.relationships=}, {self.mood=}, {self.pending_text_messages=}, {self.text_messages=}, {self.pending_simplr_messages=}, {self.simplr_messages=}, {self.points=})"
        except AttributeError:
            return f"{self.__class__.__name__}({self.__dict__})"

    @property
    def name(self) -> str:
        try:
            return self.__dict__["name"]
        except KeyError:
            return ""

    @property
    def username(self) -> str:
        return (
            self.__dict__.get("username")
            or self.__dict__.get("_username")
            or self.__dict__.get("name", "")
        )

    @property
    def profile_pictures(self) -> tuple[str, ...]:
        return CharacterService.get_profile_pictures(self.name.lower())

    @property
    def profile_picture_65x65(self) -> "Displayable":
        try:
            return self._profile_picture_65x65
        except AttributeError:
            self.set_profile_pictures()
        return self._profile_picture_65x65

    def set_profile_pictures(self) -> None:
        self._profile_pictures = self.profile_pictures

        try:
            profile_picture = self._profile_pictures[0]
        except IndexError:
            profile_picture = "characters/images/chloe/chloe.png"

        self._profile_picture = profile_picture
        self._profile_picture_65x65 = Transform(profile_picture, xysize=(65, 65))

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
