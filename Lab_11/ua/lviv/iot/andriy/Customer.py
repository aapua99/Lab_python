from ua.lviv.iot.andriy.Shop import Shop


class Customer:
    def __init__(self, name="no_name", age=0, shop=Shop()):
        self.name = name
        self.age = age
        self.shop = shop

    def buy_fruit(self, fruit):
        self.shop.sell_fruit(fruit)
