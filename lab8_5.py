# Создание основного класса Shape
class Shape:
    # Метод для подсчета площади фигуры
    def area(self):
        pass

# Создание класса Rectangle, который наследует методы и атрибуты от Shape
class Rectangle(Shape):
    # Метод инициализации класса
    def __init__(self, width, height):
        self.width = width # Ширина
        self.height = height # Высота

    # Метод для подсчета площади фигуры
    def area(self):
        return self.width * self.height

# Создание класса Circle, который наследует методы и атрибуты от Shape
class Circle(Shape):
    # Метод инициализации класса
    def __init__(self, radius):
        self.radius = radius # Радиус

    # Метод для подсчета площади фигуры
    def area(self):
        return 3.14 * self.radius * self.radius

# Список с фигурами
arr = [Rectangle(5, 8), Circle(4)]
# Вызов метода area для подсчета площади у каждой фигуры
for elem in arr:
    print(elem.area())