from PlayableCharacters_ren import PlayableCharacter
from Frat_ren import Frat
from game.minigames.kings.kings_data_ren import KingsData

name = "Alex"

"""renpy
init python:
"""


class MainCharacter(PlayableCharacter, object):
    def __init__(self) -> None:
        self._username = name
        self.daddy_name = "Daddy"
        self._profile_picture = self.profile_pictures[0]
        self.money = 0
        self.frat = Frat.WOLVES

        self.relationships = {}
        self.inventory = []

        self._kings_data = KingsData()

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def kings(self) -> "KingsData":
        if self._kings_data is None:
            self._kings_data = KingsData()

        return self._kings_data