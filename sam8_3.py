class Toy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toyChar(self):
        print(f"name of toy is {self.name}, {self.age} years old")

class Car(Toy):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def toyChar(self):
        print(f"name of toy is {self.name}, {self.age} years old", "and my speed is",self.speed)

Formula = Car("formula 2", 1, 120)
Formula.toyChar()
