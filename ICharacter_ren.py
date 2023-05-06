from __future__ import annotations
from abc import ABC
from game.characters.Moods_ren import Moods

from game.characters.Relationship_ren import Relationship
from game.phone.Message_ren import Message

"""renpy
init python:
"""


class ICharacter(ABC):
    name: str
    username: str

    relationships: dict[ICharacter, Relationship]
    mood: Moods

    profile_pictures: list[str]
    profile_picture: str
    points: int
    has_had_sex_with_mc: bool

    is_competitive: bool
    vindictive_characters: tuple[ICharacter, ...]
    is_talkative: bool

    pending_text_messages: list[Message]
    text_messages: list[Message]

    pending_simplr_messages: list[Message]
    simplr_messages: list[Message]
