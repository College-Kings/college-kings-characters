from abc import abstractmethod
from typing import Protocol, runtime_checkable
from game.characters.Relationship_ren import Relationship

from renpy import config

chloe: "CharacterProtocol"

"""renpy
init python:
"""


@runtime_checkable
class CharacterProtocol(Protocol):
    relationships: dict["CharacterProtocol", Relationship]

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CharacterProtocol):
            return NotImplemented

        return self.name == __value.name

    @property
    @abstractmethod
    def name(self) -> str:
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
