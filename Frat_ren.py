import enum
from enum import Enum

"""renpy
init python:
"""


class Frat(Enum):
    APES = enum.auto()
    WOLVES = enum.auto()

    @classmethod
    def _missing_(cls, value):
        return cls.WOLVES
