from __future__ import annotations
from abc import ABC
from game.characters.Moods_ren import Moods

from game.characters.Relationship_ren import Relationship

"""renpy
init python:
"""


class ICharacter(ABC):
    relationships: dict[ICharacter, Relationship]
    mood: Moods
