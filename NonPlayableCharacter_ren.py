from dataclasses import dataclass, field
from typing import Optional

from game.characters.CharacterService_ren import CharacterService
from game.characters.ICharacter_ren import ICharacter
from game.characters.Moods_ren import Moods
from game.characters.Relationship_ren import Relationship
from game.phone.Message_ren import Message

chloe: "NonPlayableCharacter"

"""renpy
init python:
"""


@dataclass
class NonPlayableCharacter(ICharacter):
    name: str = ""
    _username: str = ""

    relationships: dict[ICharacter, "Relationship"] = field(default_factory=dict)
    mood: Moods = Moods.NORMAL

    _profile_pictures: list[str] = field(default_factory=list)
    points: int = 0
    has_had_sex_with_mc: bool = False

    is_competitive: bool = False
    vindictive_characters: tuple["ICharacter", ...] = ()
    is_talkative: bool = False

    _pending_text_messages: list["Message"] = field(default_factory=list)
    _text_messages: list["Message"] = field(default_factory=list)

    _pending_simplr_messages: list["Message"] = field(default_factory=list)
    _simplr_messages: list["Message"] = field(default_factory=list)

    @property
    def username(self) -> str:
        try:
            if not self._username:
                return self.name
            return self._username
        except AttributeError:
            return self.name

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def profile_pictures(self) -> list[str]:
        return CharacterService.get_profile_pictures(self.name.lower())

    @profile_pictures.setter
    def profile_pictures(self, value: list[str]) -> None:
        self._profile_pictures = CharacterService.get_profile_pictures(
            self.name.lower()
        )

    @property
    def pending_text_messages(self) -> list["Message"]:
        try:
            self._pending_text_messages
        except AttributeError:
            self._pending_text_messages = []

        return self._pending_text_messages

    @pending_text_messages.setter
    def pending_text_messages(self, value: list["Message"]) -> None:
        self._pending_text_messages = value

    @property
    def text_messages(self) -> list["Message"]:
        try:
            self._text_messages
        except AttributeError:
            self._text_messages = []

        return self._text_messages

    @text_messages.setter
    def text_messages(self, value: list["Message"]) -> None:
        self._text_messages = value

    @property
    def pending_simplr_messages(self) -> list["Message"]:
        try:
            self._pending_simplr_messages
        except AttributeError:
            self._pending_simplr_messages = []

        return self._pending_simplr_messages

    @pending_simplr_messages.setter
    def pending_simplr_messages(self, value: list["Message"]) -> None:
        self._pending_simplr_messages = value

    @property
    def simplr_messages(self) -> list["Message"]:
        try:
            self._simplr_messages
        except AttributeError:
            self._simplr_messages = []

        return self._simplr_messages

    @simplr_messages.setter
    def simplr_messages(self, value: list["Message"]) -> None:
        self._simplr_messages = value

    @property
    def profile_picture(self) -> Optional[str]:
        try:
            return self.profile_pictures[0]
        except (AttributeError, IndexError):
            return None

    @profile_picture.setter
    def profile_picture(self, value: str) -> None:
        return

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, NonPlayableCharacter):
            return NotImplemented

        return self.name == __value.name

    def is_girlfriend(self, character: ICharacter) -> bool:
        return (
            character.relationships.setdefault(self, Relationship.FRIEND)
            == Relationship.GIRLFRIEND
        )

    def is_fwb(self, character: ICharacter) -> bool:
        return (
            character.relationships.setdefault(self, Relationship.FRIEND)
            == Relationship.FWB
        )

    def is_friend(self, character: ICharacter) -> bool:
        return (
            character.relationships.setdefault(self, Relationship.FRIEND)
            == Relationship.FRIEND
        )

    def is_ex(self, character: ICharacter) -> bool:
        return (
            character.relationships.setdefault(self, Relationship.FRIEND)
            == Relationship.EX
        )


# # region Relationships
# # region Old CK1

# # region aubrey
# try:
#     if aubrey._relationship == Relationship.FWB:
#         CharacterService.set_relationship(aubrey, Relationship.FWB)
#     del aubrey.relationship
# except AttributeError:
#     pass
# # endregion aubrey

# # region autumn
# try:
#     if autumn._relationship == Relationship.MAD:
#         CharacterService.set_mood(autumn, Moods.MAD)
#     del autumn.relationship
# except AttributeError:
#     pass
# # endregion autumn

# # region cameron
# try:
#     if cameron._relationship == Relationship.BRO:
#         v0_cameron_and_mc_friends = True
#     del cameron.relationship
# except AttributeError:
#     pass
# # endregion cameron

# # region candy
# try:
#     if candy._relationship == Relationship.FWB:
#         CharacterService.set_relationship(candy, Relationship.FWB)
#     del candy.relationship
# except AttributeError:
#     pass
# # endregion candy

# # region chloe
# try:
#     if chloe._relationship == Relationship.MAD:
#         CharacterService.set_mood(chloe, Moods.MAD)
# except AttributeError:
#     pass

# try:
#     if chloe._relationship == Relationship.FWB:
#         CharacterService.set_relationship(chloe, Relationship.FWB)
# except AttributeError:
#     pass

# try:
#     if chloe._relationship == Relationship.GIRLFRIEND:
#         CharacterService.set_relationship(chloe, Relationship.GIRLFRIEND)
# except AttributeError:
#     pass

# try:
#     del chloe.relationship
# except AttributeError:
#     pass
# # endregion chloe

# # region chris
# try:
#     if chris._relationship == Relationship.MAD:
#         CharacterService.set_mood(chris, Moods.MAD)
#     del chris.relationship
# except AttributeError:
#     pass
# # endregion chris

# # region elijah
# try:
#     if elijah._relationship == Relationship.MAKEFUN:
#         CharacterService.set_mood(elijah, Moods.HURT)
#     del elijah.relationship
# except AttributeError:
#     pass
# # endregion elijah

# # region emily
# try:
#     if emily._relationship == Relationship.FWB:
#         CharacterService.set_relationship(emily, Relationship.FWB)
#     del emily.relationship
# except AttributeError:
#     pass
# # endregion emily

# # region emmy
# try:
#     if emmy._relationship == Relationship.FWB:
#         CharacterService.set_relationship(emmy, Relationship.FWB)
#     del emmy.relationship
# except AttributeError:
#     pass
# # endregion emmy

# # region evelyn
# try:
#     if evelyn._relationship == Relationship.MOVE:
#         v2_made_a_move_on_evelyn = True
# except AttributeError:
#     pass

# try:
#     if evelyn._relationship == Relationship.DATE:
#         CharacterService.set_relationship(evelyn, Relationship.DATING)
# except AttributeError:
#     pass

# try:
#     if evelyn._relationship == Relationship.LIKES:
#         v6_evelyn_successful_date = True
# except AttributeError:
#     pass

# try:
#     if evelyn._relationship == Relationship.KISS:
#         CharacterService.set_relationship(evelyn, Relationship.KISSED)
# except AttributeError:
#     pass

# try:
#     del evelyn.relationship
# except AttributeError:
#     pass
# # endregion evelyn

# # region imre
# try:
#     if imre._relationship == Relationship.MAD:
#         CharacterService.set_mood(imre, Moods.MAD)
#     del imre.relationship
# except AttributeError:
#     pass
# # endregion imre

# # region josh
# try:
#     if josh._relationship == Relationship.MAD:
#         CharacterService.set_mood(josh, Moods.MAD)
#     del josh.relationship
# except AttributeError:
#     pass
# # endregion josh

# # region lauren
# try:
#     if lauren._relationship == Relationship.MAD:
#         CharacterService.set_mood(lauren, Moods.MAD)
# except AttributeError:
#     pass

# try:
#     if lauren._relationship == Relationship.MOVE:
#         CharacterService.set_mood(lauren, Moods.AWKWARD)
# except AttributeError:
#     pass

# try:
#     if lauren._relationship == Relationship.KISS:
#         CharacterService.set_relationship(lauren, Relationship.KISSED)
# except AttributeError:
#     pass

# try:
#     if lauren._relationship == Relationship.GIRLFRIEND:
#         CharacterService.set_relationship(lauren, Relationship.GIRLFRIEND)
# except AttributeError:
#     pass

# try:
#     del lauren.relationship
# except AttributeError:
#     pass
# # endregion lauren

# # region lindsey
# try:
#     if lindsey._relationship == Relationship.FWB:
#         CharacterService.set_relationship(lindsey, Relationship.FWB)
# except AttributeError:
#     pass

# try:
#     if lindsey._relationship == Relationship.KISS:
#         CharacterService.set_relationship(lindsey, Relationship.KISSED)
# except AttributeError:
#     pass

# try:
#     del lindsey.relationship
# except AttributeError:
#     pass
# # endregion lindsey

# # region ms_rose
# try:
#     if ms_rose._relationship == Relationship.FWB:
#         CharacterService.set_relationship(ms_rose, Relationship.FWB)
# except AttributeError:
#     pass

# try:
#     if ms_rose._relationship == Relationship.KISS:
#         CharacterService.set_relationship(ms_rose, Relationship.KISSED)
# except AttributeError:
#     pass

# try:
#     del ms_rose.relationship
# except AttributeError:
#     pass
# # endregion ms_rose

# # region nora
# try:
#     if nora._relationship == Relationship.MOVE:
#         CharacterService.set_mood(nora, Moods.AWKWARD)
# except AttributeError:
#     pass

# try:
#     if nora._relationship == Relationship.LIKES:
#         v8_nora_likes_mc = True
#         CharacterService.set_relationship(nora, Relationship.FRIEND)
# except AttributeError:
#     pass

# try:
#     if nora._relationship == Relationship.FWB:
#         CharacterService.set_relationship(nora, Relationship.FWB)
# except AttributeError:
#     pass

# try:
#     if nora._relationship == Relationship.MAD:
#         CharacterService.set_mood(nora, Moods.MAD)
# except AttributeError:
#     pass

# try:
#     del nora.relationship
# except AttributeError:
#     pass
# # endregion nora

# # region penelope
# try:
#     if penelope._relationship == Relationship.LIKES:
#         CharacterService.set_relationship(penelope, Relationship.DATING)
#     del penelope.relationship
# except AttributeError:
#     pass
# # endregion penelope

# # region riley
# try:
#     if riley._relationship == Relationship.FWB:
#         CharacterService.set_relationship(riley, Relationship.FWB)
# except AttributeError:
#     pass

# try:
#     if riley._relationship == Relationship.MOVE:
#         CharacterService.set_relationship(riley, Relationship.KISSED)
# except AttributeError:
#     pass

# try:
#     if riley._relationship == Relationship.LIKES:
#         CharacterService.set_mood(riley, Moods.TEASED)
# except AttributeError:
#     pass

# try:
#     del riley.relationship
# except AttributeError:
#     pass
# # endregion riley

# # region samantha
# try:
#     if samantha._relationship == Relationship.MOVE:
#         CharacterService.set_relationship(samantha, Relationship.FWB)
#     del samantha.relationship
# except AttributeError:
#     pass
# # endregion samantha

# # region satin
# try:
#     if satin._relationship == Relationship.FWB:
#         CharacterService.set_relationship(satin, Relationship.FWB)
#     del satin.relationship
# except AttributeError:
#     pass
# # endregion satin
# # endregion Old CK1
# # endregion Relationships
