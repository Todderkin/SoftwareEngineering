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

#Создание экземпляра класса Car с производителем Toyota и моделью Corolla
my_car = Car("Toyota", "Corolla")
#Вызов метода drive() у объекта my_car
my_car.drive()