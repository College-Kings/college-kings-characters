from __future__ import annotations
import enum
from enum import Enum

from renpy import config

_version: tuple[int, int, int]

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
    def _missing_(cls, value: object) -> Relationship:
        if isinstance(_version, str) or _version < config.version:  # type: ignore
            if value == -5:
                return cls.EX
            elif value == -4:
                return cls.MAD
            elif value == -3:
                return cls.THREATEN
            elif value == -2:
                return cls.MAKEFUN
            elif value == -1:
                return cls.AWKWARD
            elif value == 0:
                return cls.FRIEND

        return cls.FRIEND
