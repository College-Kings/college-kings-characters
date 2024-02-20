from typing import Iterable, Optional, Union

from renpy import store
import renpy.exports as renpy

from game.characters.character_ren import Character
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter
from game.characters.main_character_ren import MainCharacter
from game.characters.Relationship_ren import Relationship
from game.characters.Moods_ren import Moods
from game.characters.PlayableCharacters_ren import PlayableCharacter

mc: MainCharacter
"""renpy
init python:
"""


class CharacterService:
    @staticmethod
    def get_user_by_str(name: str) -> Character:
        try:
            return getattr(store, name.lower().replace(" ", "_"))
        except AttributeError:
            raise AttributeError(f"{name} is not a valid character.")

    @staticmethod
    def get_user(character: Union[Character, str]) -> Character:
        if isinstance(character, str):
            return CharacterService.get_user_by_str(character)

        try:
            if isinstance(character, PlayableCharacter):
                return mc
            else:
                return getattr(store, character.name.lower().replace(" ", "_"))
        except AttributeError:
            raise AttributeError(f"{character} is not a valid character.")

    @staticmethod
    def get_relationship(
        character: Character, target: Optional[Character] = None
    ) -> "Relationship":
        if target is None:
            target = mc

        if not hasattr(character, "relationships"):
            character.relationships = {}

        return character.relationships.setdefault(target, Relationship.FRIEND)

    @staticmethod
    def has_relationship(
        character: Character,
        relationship: "Relationship",
        target: Optional[Character] = None,
    ) -> bool:
        if target is None:
            target = mc

        return CharacterService.get_relationship(character, target) == relationship

    @staticmethod
    def set_relationship(
        character: Character,
        relationship: "Relationship",
        target: Optional[Character] = None,
    ) -> None:
        if target is None:
            target = mc

        if not hasattr(character, "relationships"):
            character.relationships = {}

        if not hasattr(target, "relationships"):
            target.relationships = {}

        if isinstance(target.relationships, set):
            target.relationships = {r: Relationship.FWB for r in target.relationships}

        if (
            character.relationships.setdefault(target, Relationship.FRIEND)
            == relationship
        ):
            return

        character.relationships[target] = relationship
        target.relationships[character] = relationship

    @staticmethod
    def get_mood(character: "NonPlayableCharacter") -> "Moods":
        return character.mood

    @staticmethod
    def has_mood(character: "NonPlayableCharacter", mood: "Moods") -> bool:
        return mood == character.mood or character.mood & mood == mood

    @staticmethod
    def set_mood(character: "NonPlayableCharacter", mood: "Moods") -> None:
        if mood == character.mood:
            return

        character.mood = mood

    @staticmethod
    def reset_mood(character: "NonPlayableCharacter") -> None:
        character.mood = Moods.NORMAL

    @staticmethod
    def add_mood(character: "NonPlayableCharacter", mood: "Moods") -> None:
        if mood == character.mood:
            return

        if character.mood == Moods.NORMAL:
            character.mood = mood
            return

        character.mood |= mood

    @staticmethod
    def remove_mood(character: "NonPlayableCharacter", mood: "Moods") -> None:
        character.mood &= ~mood

    @staticmethod
    def get_profile_pictures(character_name: str) -> tuple[str, ...]:
        directory: str = f"characters/images/{character_name.lower()}"

        try:
            return tuple(
                file for file in renpy.list_files() if file.startswith(directory)
            )
        except OSError:
            return tuple(
                file
                for file in renpy.list_files()
                if file.startswith("characters/images/chloe")
            )

    @staticmethod
    def is_exclusive_girlfriend(
        character: Character, target: Optional[Character] = None
    ) -> bool:
        if target is None:
            target = mc

        return any(
            CharacterService.is_girlfriend(npc)
            for npc in target.relationships
            if npc != character
        )

    @staticmethod
    def is_girlfriend(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(
            character, Relationship.GIRLFRIEND, target
        )

    @staticmethod
    def is_girlfriends(
        characters: Iterable[Character],
        target: Optional[Character] = None,
    ) -> bool:
        if target is None:
            target = mc

        return all(
            CharacterService.is_girlfriend(character, target)
            for character in characters
        )

    @staticmethod
    def is_exclusive(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return any(
            CharacterService.is_girlfriend(npc) or CharacterService.is_fwb(npc)
            for npc in target.relationships
            if npc != character
        )

    @staticmethod
    def is_fwb(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(character, Relationship.FWB, target)

    @staticmethod
    def is_fwbs(
        characters: Iterable[Character],
        target: Optional[Character] = None,
    ) -> bool:
        if target is None:
            target = mc

        return all(
            CharacterService.is_fwb(character, target) for character in characters
        )

    @staticmethod
    def is_dating(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(character, Relationship.DATING, target)

    @staticmethod
    def is_kissed(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(character, Relationship.KISSED, target)

    @staticmethod
    def is_friend(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(character, Relationship.FRIEND, target)

    @staticmethod
    def is_friends(
        characters: Iterable[Character],
        target: Optional[Character] = None,
    ) -> bool:
        if target is None:
            target = mc

        return all(
            CharacterService.is_friend(character, target) for character in characters
        )

    @staticmethod
    def is_ex(character: Character, target: Optional[Character] = None) -> bool:
        if target is None:
            target = mc

        return CharacterService.has_relationship(character, Relationship.EX, target)

    @staticmethod
    def is_exes(
        characters: Iterable[Character],
        target: Optional[Character] = None,
    ):
        if target is None:
            target = mc

        return all(
            CharacterService.is_ex(character, target) for character in characters
        )

    @staticmethod
    def is_mad(character: "NonPlayableCharacter") -> bool:
        return CharacterService.has_mood(character, Moods.MAD)

    @staticmethod
    def is_threatened(character: "NonPlayableCharacter") -> bool:
        return CharacterService.has_mood(character, Moods.THREATENED)
