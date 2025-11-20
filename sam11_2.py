def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    with open("fib.txt", "w", encoding="utf-8") as file:
        for i, num in enumerate(fib(201)):
            file.write(f"{num}\n")
            if i == 200:
                fibonacci_200 = num

    print(f"200-е число Фибоначчи: {fibonacci_200}")
    print("Все числа записаны в файл 'fib.txt'")