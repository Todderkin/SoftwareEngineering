class Toy:
    def __init__(self, name, age, speed):
        self.name = name
        self._age = age
        self.__speed = speed

    def toyChar(self):
        print(f"name of toy is {self.name}, {self._age} years old and {self.__speed} km/h")

Formula = Toy("formula 2", 1, 120)
print(Formula._age)
Formula.toyChar()
