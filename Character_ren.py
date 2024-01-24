from typing import Optional
from renpy.character import ADVCharacter

from game.characters.Gender_ren import Gender
from game.characters.CharacterColors_ren import CharacterColor

"""renpy
init python:
"""


class Character(ADVCharacter):
    def __init__(
        self, name: Optional[str], kind: None = None, **properties: object
    ) -> None:
        properties.setdefault("who_outlines", [(2, "#000")])
        properties.setdefault("what_outlines", [(2, "#000")])

        if "gender" in properties and "who_color" not in properties:
            gender: object = properties.pop("gender")

            if gender == Gender.MALE:
                who_color: str = CharacterColor.get_masculine_color()
            elif gender == Gender.FEMALE:
                who_color = CharacterColor.get_feminine_color()
            elif gender == Gender.ANY:
                who_color = CharacterColor.get_any_color()
            else:
                raise ValueError('Incorrect value for "gender" property')

            properties["who_color"] = who_color

        super().__init__(name, kind, **properties)
