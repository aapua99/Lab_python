from ua.lviv.iot.andriy.Fruit import Citrus, Berry
from ua.lviv.iot.andriy.Date import Date
from ua.lviv.iot.andriy.Customer import Customer
from ua.lviv.iot.andriy.Shop import Shop
from ua.lviv.iot.andriy.Enum import BerryLocationType, FruitType, FruitColor, Season

if __name__ == "__main__":
    shop = Shop("Shop_Amdriy", 256, "Lviv")
    shop.add_fruit(Citrus(25, FruitType.LEMON, FruitColor.YELLOW, Date(12, 12, 2018), season=Season.SUMMER))
    shop.add_fruit(Berry(65, FruitType.STRAWBERRIE, FruitColor.RED, season=Season.SPRING))
    shop.add_fruit(Citrus(89, FruitType.MANDARIN, FruitColor.ORANGE, season=Season.WINTER))
    shop.add_fruit(Berry(50, FruitType.NONAME, FruitColor.BLACK, season=Season.AUTUMN))
    list=shop.sort_by_color(shop.list_fruit)
    for i in list:
        print(i.to_string())
    customer=Customer("Andriy",18,shop)
    print()
    customer.buy_fruit(Berry(5,FruitType.STRAWBERRIE))
    shop.print_list_fruit()
    print()
    shop.add_fruit(Citrus(1, FruitType.MANDARIN))
    shop.print_list_fruit()
    print()
    for i in shop.search_fruit_by_season(Season.SUMMER):
        print(i.to_string())
