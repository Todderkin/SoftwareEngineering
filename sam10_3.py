def plusTwo():
    value = input("Введите число: ")
    try:
        result = 2 + float(value)
        print(f"Результат: {result}")
    except ValueError:
        print('Неподходящий тип данных. Ожидалось число.')

plusTwo()
plusTwo()
plusTwo()