def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    for i, num in enumerate(fib(201)):
        if i == 200:
            print(num)