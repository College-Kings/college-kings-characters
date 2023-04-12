"""renpy
init python:
"""

import enum
from enum import IntEnum


class Relationship(IntEnum):
    EX = enum.auto()
    MAD = enum.auto()  # Deprecated, Resolves to Moods.MAD
    THREATEN = enum.auto()  # Deprecated, Resolves to Friend
    MAKEFUN = enum.auto()  # Deprecated, Resolves to Friend
    AWKWARD = enum.auto()  # Deprecated, Resolves to Friend
    FRIEND = enum.auto()
    MOVE = enum.auto()  # Deprecated, Resolves to Friend
    DATE = enum.auto()
    LIKES = enum.auto()
    TRUST = enum.auto()
    BRO = enum.auto()
    KISS = enum.auto()  # Deprecated, Resolves to Friend
    FWB = enum.auto()
    LOYAL = enum.auto()
    TAMED = enum.auto()
    GIRLFRIEND = enum.auto()
