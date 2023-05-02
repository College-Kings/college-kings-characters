import enum
from enum import Flag

"""renpy
init python:
"""


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
