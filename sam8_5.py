class Toy:
    def sound(self):
        pass

class toyota(Toy):
    def sound(self):
        print("vrom-vrom")

class mercedes(Toy):
    def sound(self):
        print("vro00m-vro00m")

toys = [toyota(),mercedes()]
for toy in toys:
    toy.sound()