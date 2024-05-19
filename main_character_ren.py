from PlayableCharacters_ren import PlayableCharacter
from Frat_ren import Frat

name: str

"""renpy
init python:
"""


class MainCharacter(PlayableCharacter, object):
    def __init__(self) -> None:
        self._username = name
        self._profile_picture = self.profile_pictures[0]
        self.frat = Frat.WOLVES

        self.relationships = {}
        self.inventory = []
