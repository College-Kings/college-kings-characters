from __future__ import annotations
from dataclasses import dataclass, field

from game.characters.CharacterService_ren import CharacterService
from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship
from game.characters.PlayableCharacters_ren import PlayableCharacter
from game.phone.Message_ren import Message

"""renpy
init python:
"""


@dataclass
class NonPlayableCharacter:
    name: str
    username: str = ""

    relationships: dict[PlayableCharacter, Relationship] = field(default_factory=dict)
    mood: Moods = Moods.NORMAL

    profile_pictures: list[str] = field(default_factory=list)
    points = 0
    has_had_sex_with_mc = False

    pending_text_messages: list[Message] = field(default_factory=list)
    text_messages: list[Message] = field(default_factory=list)

    pending_simplr_messages: list[Message] = field(default_factory=list)
    simplr_messages: list[Message] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.username:
            self.username = self.name

        if not self.profile_pictures:
            self.profile_pictures = CharacterService.get_profile_pictures(self.name)

    @property
    def profile_picture(self) -> str:
        return self.profile_pictures[0]

    def __hash__(self) -> int:
        return hash(self.name)
