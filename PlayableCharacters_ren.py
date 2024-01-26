from typing import Optional, Protocol, runtime_checkable

from game.characters.CharacterProtocol_ren import CharacterProtocol
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.compat.py_compat_ren import Inventory
from game.items.Item_ren import Item
from game.characters.Frat_ren import Frat
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship
from game.detective.Detective_ren import Detective

name: str
joinwolves: bool

"""renpy
init python:
"""


@runtime_checkable
class PlayableCharacter(CharacterProtocol, Protocol):
    username: str
    relationships: dict[CharacterProtocol, Relationship]
    _inventory: list["Item"]
    money: int = 0
    detective: Optional["Detective"] = None
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    @property
    def name(self) -> str:
        return name

    @property
    def profile_pictures(self) -> tuple[str, ...]:
        return CharacterService.get_profile_pictures("mc")

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
    def girlfriends(self) -> tuple[NonPlayableCharacter, ...]:
        self.repair_relationships()

        return tuple(
            npc
            for npc in self.relationships
            if isinstance(npc, NonPlayableCharacter) and npc.is_girlfriend(self)
        )

    def is_wolf(self) -> bool:
        return self.frat == Frat.WOLVES

    def is_ape(self) -> bool:
        return self.frat == Frat.APES

    def repair_relationships(self) -> None:
        local_relationships: dict[
            CharacterProtocol, Relationship
        ] = self.relationships.copy()
        for npc, relationship in local_relationships.items():
            user: CharacterProtocol = CharacterService.get_user(npc)
            if isinstance(user, NonPlayableCharacter):
                self.relationships[user] = relationship
