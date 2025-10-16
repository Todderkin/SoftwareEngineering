def get_sequence(tuple_data, element):
    if element not in tuple_data:
        return ()

    first = tuple_data.index(element)
    second = tuple_data.index(element, first + 1) if tuple_data.count(element) > 1 else len(tuple_data)

    return tuple_data[first:second + 1]

test = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

for tpl, elem in test:
    result = get_sequence(tpl, elem)
    print(result)