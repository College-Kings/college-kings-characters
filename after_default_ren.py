from renpy import config, store

"""renpy
init python:
"""


def npc_setup() -> None:
    store.chloe.is_competitive = True
    store.chloe.vindictive_characters = (store.nora,)

    store.amber.is_competitive = True
    store.amber.is_talkative = True
    store.amber.vindictive_characters = (store.riley,)

    store.riley.is_competitive = True
    store.riley.is_talkative = True

    store.lindsey.is_competitive = True
    store.lindsey.is_talkative = True
    store.lindsey.vindictive_characters = (store.chloe,)

    store.nora.is_talkative = True
    store.nora.vindictive_characters = (store.chris, store.chloe)

    store.aubrey.is_competitive = True

    store.ryan.vindictive_characters = (store.imre,)

    store.imre.vindictive_characters = (store.ryan,)

    store.charli.is_competitive = True

    store.josh.is_competitive = True


config.after_default_callbacks.append(npc_setup)
