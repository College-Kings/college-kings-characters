from abc import abstractmethod
from typing import Protocol, runtime_checkable

from renpy import config

from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship

chloe: "Character"

"""renpy
init -10 python:
"""


@runtime_checkable
class Character(Protocol):
    relationships: dict["Character", "Relationship"]
    _mood: Moods = Moods.NORMAL

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Character):
            return NotImplemented

        return self.name == __value.name

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def username(self) -> str:
        ...

    @property
    @abstractmethod
    def profile_pictures(self) -> tuple[str, ...]:
        ...

    @property
    def profile_picture(self) -> str:
        try:
            return self.profile_pictures[0]
        except (AttributeError, IndexError):
            if config.developer:
                raise AttributeError(f"{self.name} has no profile pictures.")
            return chloe.profile_picture

    # region Moods
    @property
    def mood(self) -> Moods:
        return self._mood

    @mood.setter
    def mood(self, value: Moods) -> None:
        self._mood = value

    def has_mood(self, mood: Moods) -> bool:
        return mood in self._mood

    def reset_mood(self) -> None:
        self._mood = Moods.NORMAL

    def add_mood(self, mood: Moods) -> None:
        if self._mood == Moods.NORMAL:
            self._mood = mood
            return

        self._mood |= mood

    def remove_mood(self, mood: Moods) -> None:
        self._mood &= ~mood

    def is_mad(self) -> bool:
        return self.mood == Moods.MAD

    def is_threatened(self) -> bool:
        return self.mood == Moods.THREATENED

    # endregion Moods
    # region Relationships
    def get_relationship(self, target: "Character") -> "Relationship":
        return self.relationships.setdefault(target, Relationship.FRIEND)

    def has_relationship(
        self, relationship: "Relationship", target: "Character"
    ) -> bool:
        return self.get_relationship(target) == relationship

    def is_exclusive_girlfriend(self, target: "Character") -> bool:
        return any(
            character.is_girlfriend(target)
            for character in target.relationships
            if character != self
        )

    def is_girlfriend(self, target: "Character") -> bool:
        return self.has_relationship(Relationship.GIRLFRIEND, target)

    def is_exclusive(self, target: "Character") -> bool:
        return any(
            character.is_girlfriend(target) or character.is_fwb(target)
            for character in target.relationships
            if character != self
        )

    def is_fwb(self, target: "Character") -> bool:
        return self.has_relationship(Relationship.FWB, target)

    def is_friend(self, target: "Character") -> bool:
        return self.has_relationship(Relationship.FRIEND, target)

    def is_ex(self, target: "Character") -> bool:
        return self.has_relationship(Relationship.EX, target)

    # endregion Relationships


# _profile_pictures: list[str] = field(default_factory=list)
# _profile_picture: str = ""
# money: int = 0
# _inventory: list["Item"] = field(default_factory=list)
# detective: Optional["Detective"] = None
# relationships: dict["ICharacter", "Relationship"] = field(default_factory=dict)
# frat: Frat = Frat.WOLVES
# daddy_name: str = "Daddy"

# @property
# def name(self) -> str:  # type: ignore
#     return store.name

# @property
# def username(self) -> str:
#     try:
#         if self._username is None:
#             return self.name
#         return self._username
#     except AttributeError:
#         return self.name

# name: str = ""
# _username: str = ""

# relationships: dict[ICharacter, Relationship] = field(default_factory=dict)
# mood: Moods = Moods.NORMAL

# _profile_pictures: list[str] = field(default_factory=list)
# points: int = 0
# has_had_sex_with_mc: bool = False

# is_competitive: bool = False
# vindictive_characters: tuple["ICharacter", ...] = ()
# is_talkative: bool = False

# _pending_text_messages: list[Message] = field(default_factory=list)
# _text_messages: list[Message] = field(default_factory=list)

# _pending_simplr_messages: list[Message] = field(default_factory=list)
# _simplr_messages: list[Message] = field(default_factory=list)
