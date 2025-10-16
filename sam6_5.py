# Задача: Найти сумму элементов между первым и последним вхождением заданного числа в кортеже
def sum_between(tuple_data, element):
    if element not in tuple_data:
        return 0

    first_index = tuple_data.index(element)
    last_index = len(tuple_data) - 1 - tuple_data[::-1].index(element)

    if first_index == last_index:
        return 0

    return sum(tuple_data[first_index + 1:last_index])

test1 = ((1, 2, 3, 4, 5, 3, 6, 7), 3)  # Между 3 и 3: [4, 5] = 9
test2 = ((1, 2, 3, 4, 5), 6)  # Элемента нет = 0
test3 = ((5, 1, 5, 2, 5, 3, 5), 5)  # Между первым и последним 5: [1, 5, 2, 5, 3] = 16

print(sum_between(*test1))
print(sum_between(*test2))
print(sum_between(*test3))