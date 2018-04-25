from enum import Enum


class FruitType(Enum):
    LEMON = "Lemon"
    ORANGE = "Orange"
    MANDARIN = "Mandarin"
    STRAWBERRIE = "Strawberrie"
    BLACKBERRIE = "Blackberrie"
    NONAME = "no_name"


class FruitColor(Enum):
    RED = "Red"
    GREEN = "Green"
    WHITE = "White"
    YELLOW = "Yellow"
    PURPLE = "Purple"
    BLUE = "Blue"
    ORANGE = "Orange"
    BLACK = "Black"


class Season(Enum):
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"
    SPRING = "Spring"


class BerryLocationType(Enum):
    FOREST = "Forest"
    BACKYARD = "Backyard"
