#Создание класса Car
class Car:
    #Метод инициализации класса
    def __init__(self, make, model):
        #Присваивание параметров make и model атрибутам экземпляра
        self._make = make
        self.__model = model

    #Метод, выводящий в консоль информацию о производителе и модели автомобиля
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

#Создание экземпляра класса Car с производителем Toyota и моделью Corolla
my_car = Car("Toyota", "Corolla")
#Доступ к защищенному атрибуту
print(my_car._make)
# print(my_car.__model) - будет ошибка, т.к. приватный атрибут не доступен
#Вызов метода drive() у объекта my_car
my_car.drive()