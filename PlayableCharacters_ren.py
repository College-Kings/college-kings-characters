from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

from game.characters.Frat_ren import Frat

from renpy import store
import renpy.exports as renpy

from game.detective.Detective_ren import Detective
from game.characters.CharacterService_ren import CharacterService
from game.characters.Relationship_ren import Relationship

"""renpy
init python:
"""


@dataclass
class PlayableCharacter:
    name: str = ""
    username: str = ""
    profile_picture: str = ""
    money: int = 0
    inventory: list[str] = field(default_factory=list)
    detective: Optional[Detective] = None
    relationships: dict[str, Relationship] = field(default_factory=dict)
    frat: Frat = Frat.WOLVES
    daddy_name: str = "Daddy"

    def __post_init__(self) -> None:
        if not self.name:
            self.name = store.name

        if not self.username:
            self.username = self.name

        if not self.profile_picture:
            self.profile_picture = CharacterService.get_profile_pictures("mc")[0]

    def __hash__(self) -> int:
        return hash(self.name)

    # @property
    # def fighter(self):
    #     return self._fighter

    # @fighter.setter
    # def fighter(self, value: BasePlayer):
    #     self._fighter = value
