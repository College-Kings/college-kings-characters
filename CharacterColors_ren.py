"""renpy
init python:
"""


MASCULINE_COLORS: tuple[str, ...] = (
    "#0055ff",
    "#046307",
    "#147efb",
    "#15b42a",
    "#3fcf08",
    "#8b0000",
    "#a50615",
    "#db6f1c",
    "#fd9426",
    "#ffb210",
    "#ff1694",
    "#5fc9f8",
)

FEMININE_COLORS: tuple[str, ...] = (
    "#05F0D5",
    "#800080",
    "#a3a3a3",
    "#a815f2",
    "#ecd9c9",
    "#f197f3",
    "#ff2aff",
    "#ff8afb",
    "#ff00ea",
)


class CharacterColor:
    index = 0

    @classmethod
    def _get_color(cls, colors: tuple[str]) -> str:
        color: str = colors[cls.index % len(colors)]
        cls.index += 1
        return color

    @classmethod
    def get_any_color(cls) -> str:
        return cls._get_color(MASCULINE_COLORS + FEMININE_COLORS)

    @classmethod
    def get_masculine_color(cls) -> str:
        return cls._get_color(MASCULINE_COLORS)

    @classmethod
    def get_feminine_color(cls) -> str:
        return cls._get_color(FEMININE_COLORS)
