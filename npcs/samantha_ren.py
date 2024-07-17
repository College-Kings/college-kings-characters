from game.characters.Frat_ren import Frat
from game.characters.Moods_ren import Moods
from game.reputation.Reputations_ren import Reputations
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

"""renpy
init python:
"""


class Samantha(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.points = 0

        self.relationships = {}
        self.mood = Moods.NORMAL

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

    @property
    def name(self) -> str:
        return _("Samantha")

    @property
    def username(self) -> str:
        return _("SamFromSpaceJam")

    @property
    def preferred_reputation(self) -> "Reputations":
        return Reputations.LOYAL

    @property
    def frat_requirement(self) -> "Frat":
        return Frat.APES
