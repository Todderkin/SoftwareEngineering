class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value): #Установка значения атрибута
        self._value = value

    def get_value(self): #Получение значения атрибута
        return self._value

    def del_value(self): #Удаление атрибута
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(50)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
#Будет ошибка из-за попытки вызвать метод get_value() для получения значения удаленного выше атрибута, которого теперь не существует
print(obj.get_value())