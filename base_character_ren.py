from abc import abstractmethod
from typing import Any, Optional, Protocol, runtime_checkable

from game.characters.npcs.chloe_ren import Chloe
from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship
from game.minigames.kings.kings_data_ren import KingsData

chloe: Chloe
name: str

"""renpy
init -10 python:
"""


@runtime_checkable
class BaseCharacter(Protocol):
    _profile_pictures: tuple[str, ...]

    relationships: dict["BaseCharacter", "Relationship"]
    mood: Moods

    _kings_data: Optional["KingsData"] = None

    def __call__(self, *args: Any, **kwds: Any) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        if self.name:
            return self.name
        name = self.__dict__.get("name", None)
        if name:
            return name
        if self.username:
            return self.username
        return self.__class__.__name__

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, BaseCharacter):
            return NotImplemented

        return self.name == __value.name

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    def username(self) -> str:
        return (
            self.__dict__.get("username")
            or self.__dict__.get("_username")
            or self.__dict__.get("name", "")
        )

    @property
    @abstractmethod
    def profile_pictures(self) -> tuple[str, ...]: ...

    @property
    def profile_picture(self) -> Optional[str]:
        try:
            return self._profile_pictures[0]
        except (AttributeError, IndexError):
            self.set_profile_pictures()

        try:
            return self._profile_pictures[0]
        except IndexError:
            return "characters/images/chloe/chloe.png"

    def set_profile_pictures(self) -> None:
        self._profile_pictures = self.profile_pictures

    # region Moods
    def has_mood(self, mood: Moods) -> bool:
        return mood in self.mood

    def reset_mood(self) -> None:
        self.mood = Moods.NORMAL

    def add_mood(self, mood: Moods) -> None:
        if self.mood == Moods.NORMAL:
            self.mood = mood
            return

        self.mood |= mood

    def remove_mood(self, mood: Moods) -> None:
        self.mood &= ~mood

    def is_mad(self) -> bool:
        return self.mood == Moods.MAD

    def is_threatened(self) -> bool:
        return self.mood == Moods.THREATENED

    # endregion Moods
    # region Relationships
    def get_relationship(self, target: "BaseCharacter") -> "Relationship":
        return self.relationships.setdefault(target, Relationship.FRIEND)

    def has_relationship(
        self, relationship: "Relationship", target: "BaseCharacter"
    ) -> bool:
        return self.get_relationship(target) == relationship

    def is_exclusive_girlfriend(self, target: "BaseCharacter") -> bool:
        return any(
            character.is_girlfriend(target)
            for character in target.relationships
            if character != self
        )

    def is_girlfriend(self, target: "BaseCharacter") -> bool:
        return self.has_relationship(Relationship.GIRLFRIEND, target)

    def is_exclusive(self, target: "BaseCharacter") -> bool:
        return any(
            character.is_girlfriend(target) or character.is_fwb(target)
            for character in target.relationships
            if character != self
        )

    def is_fwb(self, target: "BaseCharacter") -> bool:
        return self.has_relationship(Relationship.FWB, target)

    def is_friend(self, target: "BaseCharacter") -> bool:
        return self.has_relationship(Relationship.FRIEND, target)

    def is_ex(self, target: "BaseCharacter") -> bool:
        return self.has_relationship(Relationship.EX, target)

    def any_fwb(self, *characters: "BaseCharacter") -> bool:
        return any(self.is_fwb(character) for character in characters)

    # endregion Relationships

    # region Kings Minigame
    @property
    def kings(self) -> "KingsData":
        try:
            self._kings_data
        except AttributeError:
            self._kings_data = KingsData()

        if self._kings_data is None:
            self._kings_data = KingsData()

        return self._kings_data

    # endregion Kings Minigame
