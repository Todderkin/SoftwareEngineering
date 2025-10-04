from sam4_5_1 import geron

def polzovatel():
    a = float(input("Введите первую сторону: "))
    b = float(input("Введите вторую сторону: "))
    c = float(input("Введите третью  сторону: "))
    return a, b, c

def main():
    sides = polzovatel()

    area = geron(sides[0], sides[1], sides[2])

    print(f"Площадь треугольника: {area:.2f}")

if __name__ == "__main__":
    main()