from typing import Optional, Protocol, runtime_checkable

from renpy import config

from game.characters.character_ren import Character
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.items.Item_ren import Item
from game.characters.Frat_ren import Frat
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship
from game.detective.Detective_ren import Detective

name: str = ""

"""renpy
init python:
"""


@runtime_checkable
class PlayableCharacter(Character, Protocol):
    _username: str
    _profile_picture: str
    relationships: dict[Character, Relationship]
    inventory: list["Item"]
    detective: Optional["Detective"] = None
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    @property
    def name(self) -> str:
        return name

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def profile_pictures(self) -> tuple[str, ...]:
        return CharacterService.get_profile_pictures("mc")

    @property
    def profile_picture(self) -> str:
        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, value: str) -> None:
        self._profile_picture = value

    @property
    def girlfriends(self) -> tuple[NonPlayableCharacter, ...]:
        return tuple(
            npc
            for npc in self.relationships
            if isinstance(npc, NonPlayableCharacter) and npc.is_girlfriend(self)
        )

    @property
    def partners(self) -> tuple[NonPlayableCharacter, ...]:
        return tuple(
            npc
            for npc in self.relationships
            if isinstance(npc, NonPlayableCharacter)
            and npc.is_girlfriend(self)
            and npc.is_fwb(self)
        )

    @property
    def fwbs(self) -> tuple[NonPlayableCharacter, ...]:
        return tuple(
            npc
            for npc in self.relationships
            if isinstance(npc, NonPlayableCharacter) and npc.is_fwb(self)
        )

    def is_wolf(self) -> bool:
        return self.frat == Frat.WOLVES

    def is_ape(self) -> bool:
        return self.frat == Frat.APES


config.ex_rollback_classes.append(PlayableCharacter)
