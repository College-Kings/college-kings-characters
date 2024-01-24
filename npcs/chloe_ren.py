from renpy.minstore import _

from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

"""renpy
init python:
"""


class Chloe(NonPlayableCharacter):
    @property
    def name(self) -> str:
        return _("Chloe")

    @property
    def username(self) -> str:
        return _("Chloe101")
