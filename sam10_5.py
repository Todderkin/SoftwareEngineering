# Собственное исключение для проверки возраста
class InvalidAgeError(Exception):
    """Исключение для недопустимого возраста"""

    def __init__(self, age, message="Недопустимый возраст"):
        self.age = age
        self.message = f"{message}: {age}"
        super().__init__(self.message)


# Функция 1 - проверка входа в клуб
def check_club_entry(age):
    print(f"Проверка входа в клуб для возраста {age}...")

    if age < 18:
        raise InvalidAgeError(age, "Для входа в клуб нужно быть старше 18 лет")
    elif age > 80:
        raise InvalidAgeError(age, "Слишком большой возраст для клуба")
    else:
        print("Добро пожаловать в клуб!")
        return True


# Функция 2 - проверка получения прав
def check_driving_license(age):
    print(f"Проверка прав для возраста {age}...")

    if age < 16:
        raise InvalidAgeError(age, "Для получения прав нужно быть старше 16 лет")
    elif age > 75:
        raise InvalidAgeError(age, "Требуется медицинская проверка")
    else:
        print("Можно получить права!")
        return True


# Тестирование функций
def test_functions():
    print("ТЕСТИРОВАНИЕ ИСКЛЮЧЕНИЯ InvalidAgeError")

    test_ages = [15, 18, 82, 70]

    for age in test_ages:
        print(f"\nВозраст {age} лет:")

        # Тест входа в клуб
        try:
            check_club_entry(age)
        except InvalidAgeError as e:
            print(f"Клуб: {e}")

        # Тест получения прав
        try:
            check_driving_license(age)
        except InvalidAgeError as e:
            print(f"Права: {e}")


# Главная функция
if __name__ == "__main__":
    test_functions()
    print("\nТестирование завершено!")