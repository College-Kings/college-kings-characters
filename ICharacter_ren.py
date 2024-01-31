from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship
from game.phone.Message_ren import Message

"""renpy
init python:
"""


class ICharacter:
    name: str
    _username: str

    relationships: dict["ICharacter", "Relationship"]
    mood: "Moods"

    _profile_pictures: list[str]
    _profile_picture: str

    points: int
    has_had_sex_with_mc: bool

    is_competitive: bool
    vindictive_characters: tuple["ICharacter", ...]
    is_talkative: bool

    _pending_text_messages: list["Message"]
    _text_messages: list["Message"]

    _pending_simplr_messages: list["Message"]
    _simplr_messages: list["Message"]

    @property
    def username(self) -> str:
        if not self._username:
            return self.name
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def profile_pictures(self) -> list[str]:
        return self._profile_pictures

    @profile_pictures.setter
    def profile_pictures(self, value: list[str]) -> None:
        self._profile_pictures = value

    @property
    def profile_picture(self) -> str:
        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, value: str) -> None:
        self._profile_picture = value

    @property
    def pending_text_messages(self) -> list["Message"]:
        return self._pending_text_messages

    @pending_text_messages.setter
    def pending_text_messages(self, value: list["Message"]) -> None:
        self._pending_text_messages = value

    @property
    def text_messages(self) -> list["Message"]:
        return self._text_messages

    @text_messages.setter
    def text_messages(self, value: list["Message"]) -> None:
        self._text_messages = value

    @property
    def pending_simplr_messages(self) -> list["Message"]:
        return self._pending_simplr_messages

    @pending_simplr_messages.setter
    def pending_simplr_messages(self, value: list["Message"]) -> None:
        self._pending_simplr_messages = value

    @property
    def simplr_messages(self) -> list["Message"]:
        return self._simplr_messages

    @simplr_messages.setter
    def simplr_messages(self, value: list["Message"]) -> None:
        self._simplr_messages = value
