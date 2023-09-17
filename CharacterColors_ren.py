"""renpy
init python:
"""


MASCULINE_COLORS: tuple[str, ...] = (
    "#0055ff",  # Bright Blue
    "#046307",  # Dark Green
    "#147efb",  # Sky Blue
    "#15b42a",  # Bright Green
    "#3fcf08",  # Lime Green
    "#5fc9f8",  # Light Sky Blue
    "#8b0000",  # Dark Red
    "#a50615",  # Crimson Red
    "#db6f1c",  # Dark Orange/Brown
    "#fd9426",  # Bright Orange
    "#ffb210",  # Gold/Yellow
)

FEMININE_COLORS: tuple[str, ...] = (
    "#e75480",  # Dark Pink
    "#ff1694",  # Bright Pink
    "#ff2aff",  # Neon Pink
    "#ff00ea",  # Magenta
    "#a815f2",  # Bright Violet
    "#800080",  # Purple
    "#ff8afb",  # Lavender Pink
    "#f197f3",  # Pink
    "#f49ac2",  # Pastel Pink
    "#ffb6c1",  # Light Pink
    "#ecd9c9",  # Blush Pink
    "#05F0D5",  # Turquoise
    "#a3a3a3",  # Silver
)


class CharacterColor:
    index = 0

    @classmethod
    def _get_color(cls, colors: tuple[str, ...]) -> str:
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
