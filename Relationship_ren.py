from __future__ import annotations
from enum import Enum

"""renpy
init python:
"""


class Relationship(Enum):
    STRANGER = -6
    EX = -5
    MAD = -4  # Deprecated, Resolves to Moods.MAD
    THREATEN = -3  # Deprecated, Resolves to Friend
    MAKEFUN = -2  # Deprecated, Resolves to Friend
    AWKWARD = -1  # Deprecated, Resolves to Friend
    FRIEND = 0
    KISSED = 0.5
    MOVE = 1  # Deprecated, Resolves to Friend
    DATE = 2  # Deprecated, Resolves to Dating
    DATING = 2.5
    LIKES = 3  # Deprecated, Resolves to Dating
    TRUST = 4  # Deprecated, Resolves to Dating
    BRO = 5  # Deprecated, Resolves to Friend
    KISS = 6  # Deprecated, Resolves to Kissed
    FWB = 7
    LOYAL = 8  # Deprecated, Resolves to FWB if had sex, else Friend
    TAMED = 9  # Deprecated, Resolves to FWB if had sex, else Friend
    GIRLFRIEND = 10

    @classmethod
    def _missing_(cls, value: object) -> Relationship:
        return cls.FRIEND
