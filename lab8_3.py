#Создание класса Car
class Car:
    #Метод инициализации класса
    def __init__(self, make, model):
        #Присваивание параметров make и model атрибутам экземпляра
        self.make = make
        self.model = model

    #Метод, выводящий в консоль информацию о производителе и модели автомобиля
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

#Создание класса ElectricCar, наследующего атрибуты и методы родительского класса Car
class ElectricCar(Car):
    # Метод инициализации класса
    def __init__(self, make, model, battery_capacity):
        #Вызов конструктора родительского класса
        super().__init__(make, model)
        #Присваивание параметра battery_capacity атрибуту емкости батареи
        self.battery_capacity = battery_capacity

    #Метод зарядки автомобиля
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

#Создание экземпляра класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)
#Вызов метода drive() у объекта my_electric_car
my_electric_car.drive()
#Вызов метода charge() у объекта my_electric_car для зарядки автомобиля
my_electric_car.charge()