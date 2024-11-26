from game.characters.Moods_ren import Moods
from game.characters.character_traits_ren import CharacterTrait
from game.characters.npcs.riley_ren import Riley
from game.minigames.kings.kings_data_ren import KingsData
from game.reputation.Reputations_ren import Reputations
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

riley = Riley()

"""renpy
init python:
"""


class Aubrey(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.points = 0

        self.relationships = {}
        self.mood = Moods.NORMAL

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

        self._kings_data = KingsData()

    @property
    def name(self) -> str:
        return _("Aubrey")

    @property
    def username(self) -> str:
        return _("Aubs123")

    @property
    def traits(self) -> CharacterTrait:
        return CharacterTrait.COMPETITIVE | CharacterTrait.TALKATIVE

    @property
    def vindictive_characters(self) -> tuple[NonPlayableCharacter, ...]:
        return (riley,)

    @property
    def preferred_reputation(self) -> "Reputations":
        return Reputations.POPULAR
    
    @property
    def kings(self) -> "KingsData":
        try:
            self._kings_data
        except AttributeError:
            self._kings_data = KingsData()

        if self._kings_data is None:
            self._kings_data = KingsData()

        return self._kings_data