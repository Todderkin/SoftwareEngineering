import random

def cubic():
    value = random.randint(1, 6)

    print(f"Выпало: {value}")

    if value == 5 or value == 6:
        print("Вы победили")
    elif value == 3 or value == 4:
        print("Бросаем еще раз...")
        cubic()
    elif value == 1 or value == 2:
        print("Вы проиграли")

if __name__ == "__main__":
    cubic()