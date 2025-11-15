import time

# Создаем собственный декоратор "Замедлитель"
class SlowDown:
    """
    Декоратор, который искусственно замедляет выполнение функции
    на указанное количество секунд
    """
    def __init__(self, delay=1):
        self.delay = delay  # время задержки в секундах

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Функция '{func.__name__}' замедлена на {self.delay} секунду...")
            time.sleep(self.delay)  # искусственная задержка
            result = func(*args, **kwargs)
            print(f"Функция '{func.__name__}' выполнена!")
            return result

        return wrapper

# Первая функция - калькулятор для двух чисел
@SlowDown(delay=2)  # замедляем на 2 секунды
def simple_calculator(a, b):
    print(f"\nКалькулятор работает с числами: {a} и {b}")
    print(f"Сложение: {a} + {b} = {a + b}")
    print(f"Вычитание: {a} - {b} = {a - b}")
    print(f"Умножение: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Деление: {a} / {b} = {a / b:.2f}")
    else:
        print("Деление: на ноль делить нельзя!")
    return a + b  # возвращаем сумму для примера

# Вторая функция - генератор приветствий
@SlowDown(delay=1)  # замедляем на 1 секунду
def greeting_generator(name, time_of_day="день"):
    """
    Функция генерирует персонализированные приветствия
    """
    greetings = {
        "утро": f"Доброе утро, {name}!",
        "день": f"Добрый день, {name}!",
        "вечер": f"Добрый вечер, {name}!",
        "ночь": f"Доброй ночи, {name}!"
    }

    message = greetings.get(time_of_day, f"Привет, {name}!")
    print(f"\n{message}")
    return message


# Демонстрация работы декоратора
if __name__ == "__main__":
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ДЕКОРАТОРА 'SLOWDOWN'")

    # Тестируем первую функцию
    print("\n1. ТЕСТИРУЕМ КАЛЬКУЛЯТОР:")
    result1 = simple_calculator(10, 5)
    print(f"Результат функции: {result1}")

    # Тестируем вторую функцию
    print("\n2. ТЕСТИРУЕМ ГЕНЕРАТОР ПРИВЕТСТВИЙ:")
    result2 = greeting_generator("Анна", "утро")
    print(f"Результат функции: '{result2}'")

    # Еще один тест с другими параметрами
    print("\n3. ТЕСТИРУЕМ С ДРУГИМИ ПАРАМЕТРАМИ:")
    result3 = greeting_generator("Иван")
    print(f"Результат функции: '{result3}'")

    print("\nВСЕ ФУНКЦИИ ВЫПОЛНЕНЫ УСПЕШНО!")