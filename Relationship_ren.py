import enum
from enum import Enum

"""renpy
init python:
"""


class Relationship(Enum):
    STRANGER = enum.auto()
    EX = enum.auto()
    MAD = enum.auto()  # Deprecated, Resolves to Moods.MAD
    THREATEN = enum.auto()  # Deprecated, Resolves to Friend
    MAKEFUN = enum.auto()  # Deprecated, Resolves to Friend
    AWKWARD = enum.auto()  # Deprecated, Resolves to Friend
    FRIEND = enum.auto()
    KISSED = enum.auto()
    MOVE = enum.auto()  # Deprecated, Resolves to Friend
    DATE = enum.auto()  # Deprecated, Resolves to Dating
    DATING = enum.auto()
    LIKES = enum.auto()  # Deprecated, Resolves to Dating
    TRUST = enum.auto()  # Deprecated, Resolves to Dating
    BRO = enum.auto()  # Deprecated, Resolves to Friend
    KISS = enum.auto()  # Deprecated, Resolves to Kissed
    FWB = enum.auto()
    LOYAL = enum.auto()  # Deprecated, Resolves to FWB if had sex, else Friend
    TAMED = enum.auto()  # Deprecated, Resolves to FWB if had sex, else Friend
    GIRLFRIEND = enum.auto()

    @classmethod
    def _missing_(cls, value):
        return cls.FRIEND
