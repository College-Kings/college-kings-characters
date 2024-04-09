from typing import Any
from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

"""renpy
init python:
"""


class Perry(NonPlayableCharacter, object):
    def __init__(self) -> None:
        self.relationships = {}

        self.pending_text_messages = []
        self.text_messages = []

        self.pending_simplr_messages = []
        self.simplr_messages = []

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__init__()

        self.__dict__.update(state)

    @property
    def name(self) -> str:
        return _("Perry")

    @property
    def username(self) -> str:
        return _("Perry")
