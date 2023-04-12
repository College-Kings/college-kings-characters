"""renpy
init python:
"""

import enum
from enum import Flag
from typing import Any


class Moods(Flag):
    NORMAL = enum.auto()
    AWKWARD = enum.auto()
    HURT = enum.auto()
    JEALOUS = enum.auto()
    LOYAL = enum.auto()
    MAD = enum.auto()
    THREATENED = enum.auto()
    TEASED = enum.auto()
    TRUSTING = enum.auto()
    # New enum MUST be added to the end of this list to preserve numbering

    def add_flag(self, other: Any):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} must be of type {self.__class__.__name__}.")

        return self | other

    def remove_flag(self, other: Any):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} must be of type {self.__class__.__name__}.")

        return self & ~other

    def has_flag(self, other: Any):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} must be of type {self.__class__.__name__}.")

        return other.value == self.value & other.value
