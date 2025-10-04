def avg(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    result1 = avg(10, 20, 30)
    print(f"Среднее чисел 10, 20, 30: {result1}")

    result2 = avg(1, 2, 3, 4, 5)
    print(f"Среднее чисел 1, 2, 3, 4, 5: {result2}")