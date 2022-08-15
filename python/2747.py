def fibonacci(n):
    f = [0] * 46
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


if __name__ == "__main__":
    print(fibonacci(int(input())))