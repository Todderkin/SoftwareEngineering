def remove(tuple_data, element):
    temp_list = list(tuple_data)

    if element in temp_list:
        temp_list.remove(element)

    return tuple(temp_list)

test = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

for i, (tpl, elem) in enumerate(test, 1):
    result = remove(tpl, elem)
    print(f"Тест {i}: {tpl, elem} = {result}")