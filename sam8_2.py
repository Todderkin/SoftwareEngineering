class Toy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toyChar(self):
        print(f"name of toy is {self.name}, {self.age} years old")

firstToy = Toy("teddy", 2)
firstToy.toyChar()