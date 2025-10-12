import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_triangle = [max(one), max(two), max(three)]
min_triangle = [min(one), min(two), min(three)]

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

area_max = triangle_area(max_triangle[0], max_triangle[1], max_triangle[2])
area_min = triangle_area(min_triangle[0], min_triangle[1], min_triangle[2])

print("Треугольник из максимальных элементов:", max_triangle)
print("Площадь треугольника из максимальных элементов:", round(area_max, 2))

print("Треугольник из минимальных элементов:", min_triangle)
print("Площадь треугольника из минимальных элементов:", round(area_min, 2))