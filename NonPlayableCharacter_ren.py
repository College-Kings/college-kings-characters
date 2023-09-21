from dataclasses import dataclass, field

from renpy import store

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
    vindictive_characters: tuple["NonPlayableCharacter", ...] = ()
    is_talkative: bool = False

    pending_text_messages: list[Message] = field(default_factory=list)
    text_messages: list[Message] = field(default_factory=list)

    pending_simplr_messages: list[Message] = field(default_factory=list)
    simplr_messages: list[Message] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.username:
            self.username = self.name

        if not self.profile_pictures:
            self.profile_pictures = CharacterService.get_profile_pictures(
                self.name.lower()
            )

    @property
    def profile_picture(self) -> str:  # type: ignore
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

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, NonPlayableCharacter):
            return NotImplemented

        return self.name == __value.name

    def __setstate__(self, state: dict[str, object]) -> None:
        if "_relationship" in state and isinstance(
            state["_relationship"], Relationship
        ):
            if state["name"] == "Amber":
                if state["_relationship"] == Relationship.KISS:
                    CharacterService.set_relationship(self, Relationship.KISSED)

                if state["_relationship"] == Relationship.FWB:
                    CharacterService.set_relationship(self, Relationship.FWB)

                if state["_relationship"] == Relationship.FWB:
                    CharacterService.set_relationship(self, Relationship.FWB)

            if state["name"] == "Aryssa":
                if state["_relationship"] == Relationship.LIKES:
                    CharacterService.set_relationship(self, Relationship.FRIEND)

            if (
                state["name"] == "Elijah"
                and state["_relationship"] == Relationship.MAKEFUN
            ):
                CharacterService.set_mood(self, Moods.HURT)

            if state["name"] == "Evelyn":
                if state["_relationship"] == Relationship.MOVE:
                    store.v2_made_a_move_on_evelyn = True

                if state["_relationship"] == Relationship.LIKES:
                    store.v6_evelyn_successful_date = True

            if state["_relationship"] == Relationship.MAD:
                CharacterService.set_mood(self, Moods.MAD)
                CharacterService.set_relationship(self, Relationship.FRIEND)
            CharacterService.set_relationship(self, state["_relationship"])
            del state["_relationship"]

        if "pending_text_messages" not in state:
            state["pending_text_messages"] = []

        if "text_messages" not in state:
            state["text_messages"] = []

        if "pending_simplr_messages" not in state:
            state["pending_simplr_messages"] = []

        if "simplr_messages" not in state:
            state["simplr_messages"] = []

        if isinstance(state["name"], str):
            state["profile_picture"] = CharacterService.get_profile_pictures(
                state["name"].lower()
            )

        if "relationships" not in state:
            state["relationships"] = {}

        self.__dict__ = state


aaron: NonPlayableCharacter
adam: NonPlayableCharacter
amber: NonPlayableCharacter
anon: NonPlayableCharacter
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
faris: NonPlayableCharacter
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
perry: NonPlayableCharacter
polly: NonPlayableCharacter
riley: NonPlayableCharacter
ryan: NonPlayableCharacter
samantha: NonPlayableCharacter
satin: NonPlayableCharacter
sebastian: NonPlayableCharacter
tom: NonPlayableCharacter
trainer: NonPlayableCharacter
wolf: NonPlayableCharacter

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
