from abc import abstractmethod
from typing import Protocol, runtime_checkable
from game.characters.CharacterProtocol_ren import CharacterProtocol
from game.characters.Relationship_ren import Relationship
from game.characters.character_traits_ren import CharacterTrait


from game.characters.CharacterService_ren import CharacterService
from game.characters.Moods_ren import Moods
from game.phone.Message_ren import Message

chloe: "NonPlayableCharacter"

"""renpy
init python:
"""


@runtime_checkable
class NonPlayableCharacter(CharacterProtocol, Protocol):
    relationships: dict[CharacterProtocol, Relationship]

    pending_text_messages: list[Message]
    text_messages: list[Message]

    pending_simplr_messages: list[Message]
    simplr_messages: list[Message]

    mood: Moods = Moods.NORMAL
    points: int = 0

    # is_competitive: bool = False
    # vindictive_characters: tuple[PlayableCharacter, ...] = ()
    # is_talkative: bool = False

    @property
    @abstractmethod
    def username(self) -> str:
        ...

    @property
    def profile_pictures(self) -> tuple[str, ...]:
        return CharacterService.get_profile_pictures(self.name.lower())

    @property
    @abstractmethod
    def traits(self) -> CharacterTrait:
        ...

    @property
    @abstractmethod
    def vindictive_characters(self) -> tuple["NonPlayableCharacter", ...]:
        ...

    def is_girlfriend(self, character: "CharacterProtocol") -> bool:
        return self.relationships[character] == Relationship.GIRLFRIEND

    def is_fwb(self, character: "CharacterProtocol") -> bool:
        return self.relationships[character] == Relationship.FWB


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
