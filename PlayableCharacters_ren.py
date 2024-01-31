from typing import Optional, Protocol, runtime_checkable

from game.characters.character_ren import Character
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
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
class PlayableCharacter(Character, Protocol):
    _username: str
    relationships: dict[Character, Relationship]
    inventory: list["Item"]
    money: int = 0
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
        local_relationships: dict[Character, Relationship] = self.relationships.copy()
        for npc, relationship in local_relationships.items():
            user: Character = CharacterService.get_user(npc)
            if isinstance(user, NonPlayableCharacter):
                self.relationships[user] = relationship
