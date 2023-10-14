from dataclasses import dataclass, field
from typing import Optional

from renpy import store
import renpy.exports as renpy

from game.compat.py_compat_ren import Inventory
from game.Item_ren import Item
from game.characters.ICharacter_ren import ICharacter
from game.characters.Frat_ren import Frat
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship
from game.detective.Detective_ren import Detective

joinwolves: bool

"""renpy
init python:
"""


@dataclass
class PlayableCharacter(ICharacter):
    _username: Optional[str] = None
    _profile_pictures: list[str] = field(default_factory=list)
    _profile_picture: str = ""
    money: int = 0
    _inventory: list["Item"] = field(default_factory=list)
    detective: Optional["Detective"] = None
    relationships: dict["ICharacter", "Relationship"] = field(default_factory=dict)
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    @property
    def name(self) -> str:  # type: ignore
        return store.name

    @property
    def username(self) -> str:
        try:
            if self._username is None:
                return self.name
            return self._username
        except AttributeError:
            return self.name

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def profile_pictures(self) -> list[str]:
        return CharacterService.get_profile_pictures("mc")

    @profile_pictures.setter
    def profile_pictures(self, value: list[str]) -> None:
        self._profile_pictures = CharacterService.get_profile_pictures("mc")

    @property
    def profile_picture(self) -> str:
        try:
            if not self._profile_picture:
                self.profile_picture = self.profile_pictures[0]
        except AttributeError:
            self.profile_picture = self.profile_pictures[0]

        if not renpy.loadable(self._profile_picture):  # type: ignore
            self.profile_picture = self.profile_pictures[0]

        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, value: str) -> None:
        self._profile_picture = value

    @property
    def inventory(self) -> list["Item"]:
        try:
            self._inventory
        except AttributeError:
            old_inventory = self.__dict__.get("inventory", [])
            if isinstance(old_inventory, Inventory):
                old_inventory = old_inventory.items
            self._inventory = [item for item in old_inventory]

        return self._inventory

    @inventory.setter
    def inventory(self, value: list["Item"]) -> None:
        self._inventory = value

    @property
    def girlfriends(self) -> list[ICharacter]:
        self.repair_relationships()

        return [
            npc for npc in self.relationships if CharacterService.is_girlfriend(npc)
        ]

    def is_wolf(self) -> bool:
        return self.frat == Frat.WOLVES

    def is_ape(self) -> bool:
        return self.frat == Frat.APES

    def __hash__(self) -> int:
        return hash("mc")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, PlayableCharacter)

    def repair_relationships(self) -> None:
        local_relationships: dict[ICharacter, Relationship] = self.relationships.copy()
        for npc, relationship in local_relationships.items():
            self.relationships[CharacterService.get_user(npc)] = relationship


mc: PlayableCharacter
