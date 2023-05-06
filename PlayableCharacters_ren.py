from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from game.characters.ICharacter_ren import ICharacter

import renpy.exports as renpy

from game.characters.Frat_ren import Frat
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship

if TYPE_CHECKING:
    from game.detective.Detective_ren import Detective

name: str

"""renpy
init python:
"""


@dataclass
class PlayableCharacter(ICharacter):
    name: str = ""
    username: str = ""
    profile_pictures: list[str] = field(default_factory=list)
    money: int = 0
    inventory: list[str] = field(default_factory=list)
    detective: Optional[Detective] = None
    relationships: dict[ICharacter, Relationship] = field(default_factory=dict)
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    def __post_init__(self) -> None:
        if not self.name:
            self.name = name

        if not self.username:
            self.username = self.name

        if not self.profile_pictures:
            self.profile_pictures = CharacterService.get_profile_pictures("mc")

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def profile_picture(self) -> str:
        return self.profile_pictures[0]

    @property
    def girlfriends(self) -> list[ICharacter]:
        return [
            npc
            for npc in self.relationships
            if self.relationships[npc] == Relationship.GIRLFRIEND
        ]

    # @property
    # def fighter(self):
    #     return self._fighter

    # @fighter.setter
    # def fighter(self, value: BasePlayer):
    #     self._fighter = value


mc: PlayableCharacter
