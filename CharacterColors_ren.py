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
    "#05F0D5",  # Turquoise
    "#800080",  # Purple
    "#a3a3a3",  # Silver
    "#a815f2",  # Bright Violet
    "#ecd9c9",  # Blush Pink
    "#f197f3",  # Pink
    "#ff2aff",  # Neon Pink
    "#ff8afb",  # Lavender Pink
    "#ff00ea",  # Magenta
    "#ffb6c1",  # Light Pink
    "#f49ac2",  # Pastel Pink
    "#e75480",  # Dark Pink
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
