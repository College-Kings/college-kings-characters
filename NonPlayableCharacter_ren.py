from __future__ import annotations
from dataclasses import dataclass, field

from game.characters.CharacterService_ren import CharacterService
from game.characters.ICharacter_ren import ICharacter
from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship
from game.phone.Message_ren import Message

"""renpy
init python:
"""


@dataclass
class NonPlayableCharacter(ICharacter):
    name: str = ""
    username: str = ""

    relationships: dict[ICharacter, Relationship] = field(default_factory=dict)
    mood: Moods = Moods.NORMAL

    profile_pictures: list[str] = field(default_factory=list)
    points: int = 0
    has_had_sex_with_mc: bool = False

    is_competitive: bool = False
    vindictive_characters: tuple[NonPlayableCharacter, ...] = ()
    is_talkative: bool = False

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
        try:
            return self.profile_pictures[0]
        except (AttributeError, IndexError):
            raise AttributeError(f"{self.name} has no profile pictures.")

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NonPlayableCharacter):
            return NotImplemented

        return self.name == other.name


aaron: NonPlayableCharacter
adam: NonPlayableCharacter
amber: NonPlayableCharacter
aryssa: NonPlayableCharacter
aubrey: NonPlayableCharacter
autumn: NonPlayableCharacter
beth: NonPlayableCharacter
buyer: NonPlayableCharacter
caleb: NonPlayableCharacter
cameron: NonPlayableCharacter
candy: NonPlayableCharacter
charli: NonPlayableCharacter
chloe: NonPlayableCharacter
chris: NonPlayableCharacter
dean: NonPlayableCharacter
elijah: NonPlayableCharacter
emily: NonPlayableCharacter
emmy: NonPlayableCharacter
evelyn: NonPlayableCharacter
grayson: NonPlayableCharacter
imre: NonPlayableCharacter
iris: NonPlayableCharacter
jenny: NonPlayableCharacter
josh: NonPlayableCharacter
julia: NonPlayableCharacter
kai: NonPlayableCharacter
kim: NonPlayableCharacter
kourtney: NonPlayableCharacter
lauren: NonPlayableCharacter
lews_official: NonPlayableCharacter
lindsey: NonPlayableCharacter
mason: NonPlayableCharacter
mr_lee: NonPlayableCharacter
ms_rose: NonPlayableCharacter
naomi: NonPlayableCharacter
nora: NonPlayableCharacter
parker: NonPlayableCharacter
penelope: NonPlayableCharacter
polly: NonPlayableCharacter
riley: NonPlayableCharacter
ryan: NonPlayableCharacter
samantha: NonPlayableCharacter
satin: NonPlayableCharacter
sebastian: NonPlayableCharacter
tom: NonPlayableCharacter
trainer: NonPlayableCharacter
wolf: NonPlayableCharacter
