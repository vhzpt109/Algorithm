def fib(n):
    global func1_count
    if n == 1 or n == 2:
        func1_count += 1
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global func2_count
    f = [0] * 41
    f[1] = 1
    f[2] = 1
    for i in range(3, n):
        func2_count += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]


if __name__ == "__main__":
    n = int(input())

    func1_count = 0
    func2_count = 0
    fib(n)
    fibonacci(n)

    print(func1_count, func2_count + 1)