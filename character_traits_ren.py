from enum import Flag
import enum

"""renpy
init python:
"""


class CharacterTrait(Flag):
    COMPETITIVE = enum.auto()
    TALKATIVE = enum.auto()
