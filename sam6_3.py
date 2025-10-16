def top_three():
    digit_string = input("Введите последовательность цифр (минимум 15 символов): ")

    if len(digit_string) < 15:
        print("Ошибка: строка должна содержать минимум 15 символов!")
        return

    count_dict = {}

    for char in digit_string:
        num = int(char)
        count_dict[num] = count_dict.get(num, 0) + 1

    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    topThree = dict(sorted_items[:3])

    print("\nТоп-3 самых частых чисел:")
    for number in sorted(topThree.keys()):
        print(f"Цифра {number}: {topThree[number]} раз")

    print(f"\nСловарь результата: {topThree}")
    return topThree

top_three()