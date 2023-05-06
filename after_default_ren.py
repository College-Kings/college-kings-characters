from renpy import config

from game.characters.NonPlayableCharacter_ren import (
    chloe,
    amber,
    riley,
    lindsey,
    nora,
    aubrey,
    ryan,
    imre,
    charli,
    josh,
    chris,
)

"""renpy
init python:
"""


def npc_setup() -> None:
    chloe.is_competitive = True
    chloe.vindictive_characters = (nora,)

    amber.is_competitive = True
    amber.is_talkative = True
    amber.vindictive_characters = (riley,)

    riley.is_competitive = True
    riley.is_talkative = True

    lindsey.is_competitive = True
    lindsey.is_talkative = True
    lindsey.vindictive_characters = (chloe,)

    nora.is_talkative = True
    nora.vindictive_characters = (chris, chloe)

    aubrey.is_competitive = True

    ryan.vindictive_characters = (imre,)

    imre.vindictive_characters = (ryan,)

    charli.is_competitive = True

    josh.is_competitive = True


config.after_default_callbacks.append(npc_setup)
