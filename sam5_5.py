list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def create_special_set(lst):
    result_set = set()

    for num in set(lst):
        count = lst.count(num)
        result_set.add(num)
        for repeat_count in range(2, count + 1):
            result_set.add(str(num) * repeat_count)

    return result_set

set_1 = create_special_set(list_1)
set_2 = create_special_set(list_2)
set_3 = create_special_set(list_3)

print("Множество 1:", set_1)
print("Множество 2:", set_2)
print("Множество 3:", set_3)