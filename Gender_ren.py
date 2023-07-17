from enum import Enum
import enum

"""renpy
init python:
"""


class Gender(Enum):
    ANY = enum.auto()
    MALE = enum.auto()
    FEMALE = enum.auto()
