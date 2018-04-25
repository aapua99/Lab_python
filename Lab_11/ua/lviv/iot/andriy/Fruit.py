from ua.lviv.iot.andriy.Enum import FruitType, FruitColor, Season, BerryLocationType
from ua.lviv.iot.andriy.Date import Date


class Fruit:
    def __init__(self, weight=0, name=FruitType.NONAME, color=FruitColor.BLACK, date=Date(), season=Season.WINTER):
        self.weight = weight;
        self.name = name
        self.color = color
        self.date = date
        self.season = season

    def to_string(self):
        print("name: " + str(self.name.value) + " weight: " + str(self.weight) + " color: " + str(self.color))


class Citrus(Fruit):
    def __init__(self, weight=0, name=FruitType.NONAME, color=FruitColor.BLACK, date=Date(), season=Season.WINTER):
        super(Citrus, self).__init__(weight, name, color, date, season)
        self.type = type


class Berry(Fruit):
    def __init__(self, weight=0, name=FruitType.NONAME, color=FruitColor.BLACK, date=Date(),
                 type=FruitType.NONAME, location=BerryLocationType.FOREST, season=Season.WINTER):
        super(Berry, self).__init__(weight, name, color, date, season)
        self.type = type
        self.location = location
