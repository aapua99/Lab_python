class Shop:

    def __init__(self, name="no_name", area=0, adress="no", list_fruit=[]):
        self.name = name
        self.area = area
        self.adress = adress
        self.list_fruit = list_fruit

    def sell_fruit(self, fruit):
        for i in self.list_fruit:
            if i.name == fruit.name:
                i.weight -= fruit.weight
                return
        return 0

    def add_fruit(self, fruit):
        for i in self.list_fruit:
            if i.name == fruit.name:
                i.weight += fruit.weight
                return
        self.list_fruit.append(fruit)

    def sort_by_color(self, list_fruit):
        return sorted(list_fruit, key=lambda fruit: str(fruit.color))

    def search_fruit_by_season(self, season):
        result = []
        for i in self.list_fruit:
            if i.season == season:
                result.append(i)
        return result

    def print_list_fruit(self):
        for i in self.list_fruit:
            i.to_string()
