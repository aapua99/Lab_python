class Sofa:
    __number = 0

    def __init__(self, name = "no_name", width = 0, height = 0, year = 0):
        self.__height = height
        self.__width = width
        self.__year = year
        self.__name = name
        Sofa.__number += 1


    def print_static_sum():
        print(Sofa.__number)

    def print_sum(self):
        print(self.__width)

    def to_string(self):
        print("Name: " + str(self.__name) + ", width: " + str(self.__width) + ", height: " + str(
            self.__height) + ", year: "
              + str(self.__year))


if __name__ == "__main__":
    sofa = Sofa("Sofa_1", 58, 56, 2007)
    sofa.to_string()
    sofa.print_sum()
    Sofa.print_static_sum()

    sofa2 = Sofa("Sofa_2", 45, 54)
    sofa2.to_string()
    sofa2.print_sum()
    Sofa.print_static_sum()
