from typing import Optional
from renpy.character import ADVCharacter

from game.characters.Gender_ren import Gender
from game.characters.CharacterColors_ren import CharacterColor

"""renpy
init python:
"""


class Speaker(ADVCharacter):
    def __init__(
        self, name: Optional[str], kind: None = None, **properties: object
    ) -> None:
        properties.setdefault("who_outlines", [(2, "#000")])
        properties.setdefault("what_outlines", [(2, "#000")])

        if "who_color" not in properties:
            who_color: str = CharacterColor.get_any_color()

            if "gender" in properties:
                gender: object = properties.pop("gender")

                if gender == Gender.MALE:
                    who_color = CharacterColor.get_masculine_color()
                elif gender == Gender.FEMALE:
                    who_color = CharacterColor.get_feminine_color()

            properties["who_color"] = who_color

        super().__init__(name, kind, **properties)
