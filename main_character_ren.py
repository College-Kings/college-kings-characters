from typing import Any
from PlayableCharacters_ren import PlayableCharacter

name: str

"""renpy
init python:
"""


class MainCharacter(PlayableCharacter, object):
    def __init__(self) -> None:
        self._username = name
        self._profile_picture = self.profile_pictures[0]

        self.relationships = {}
        self.inventory = []

    def __setstate__(self, state: Any) -> None:
        self.__init__()

        self.__dict__.update(state)
