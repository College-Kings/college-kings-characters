from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from game.Item_ren import Item
from game.characters.ICharacter_ren import ICharacter
from game.compat.py_compat_ren import Inventory

import renpy.exports as renpy

from game.characters.Frat_ren import Frat
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship

if TYPE_CHECKING:
    from game.detective.Detective_ren import Detective

name: str
joinwolves: bool

"""renpy
init python:
"""


@dataclass
class PlayableCharacter(ICharacter):
    name: str = ""
    username: str = ""
    _profile_pictures: list[str] = field(default_factory=list)
    profile_picture: str = ""
    money: int = 0
    inventory: list["Item"] = field(default_factory=list)
    detective: Optional[Detective] = None
    relationships: dict[ICharacter, Relationship] = field(default_factory=dict)
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    def __post_init__(self) -> None:
        if not self.name:
            self.name = name

        if not self.username:
            self.username = self.name

    @property
    def profile_pictures(self) -> list[str]:
        return CharacterService.get_profile_pictures("mc")

    @profile_pictures.setter
    def profile_pictures(self, value: list[str]) -> None:
        self._profile_pictures = CharacterService.get_profile_pictures("mc")

    def __hash__(self) -> int:
        return hash("mc")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, PlayableCharacter)

    def __setstate__(self, state: dict[str, object]) -> None:
        state["name"] = name
        if not state.get("username", ""):
            state["username"] = name

        state["profile_pictures"] = CharacterService.get_profile_pictures("mc")

        if not isinstance(state["relationships"], dict):
            state["relationships"] = {}

        if "profile_picture" not in state or not state["profile_picture"]:
            state["profile_picture"] = state["profile_pictures"][0]

        if type(state["inventory"]) is Inventory:
            try:
                state["inventory"] = state["inventory"].items
            except AttributeError:
                state["inventory"] = []

        if "frat" not in state:
            state["frat"] = None
        try:
            if joinwolves:
                state["frat"] = Frat.WOLVES
            else:
                state["frat"] = Frat.APES
        except NameError:
            pass

        self.__dict__ = state

    def repair_relationships(self) -> None:
        local_relationships: dict[ICharacter, Relationship] = self.relationships.copy()
        for npc, relationship in local_relationships.items():
            self.relationships[CharacterService.get_user(npc)] = relationship

    @property
    def girlfriends(self) -> list[ICharacter]:
        self.repair_relationships()

        return [
            npc for npc in self.relationships if CharacterService.is_girlfriend(npc)
        ]


mc: PlayableCharacter
