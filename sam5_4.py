list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

marks_without2 = []
for mark in list3:
    if mark != 2:
        marks_without2.append(mark)

for i in range(len(marks_without2)):
    if marks_without2[i] == 3:
        marks_without2[i] = 4

print("Оригинальный список:\n", list3)
print("Список, где нет двоек и 3-ки заменены на 4-ки:\n", marks_without2)


