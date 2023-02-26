if __name__ == "__main__":
    n = int(input())

    for i in range(n, 0, -1):
        for _ in range(i - 1):
            print(" ", end='')
        for _ in range(n - i + 1):
            print("*", end='')
        for _ in range(n - i):
            print("*", end='')
        print("")
    for i in range(2, n + 1):
        for _ in range(i - 1):
            print(" ", end='')
        for _ in range(n - i + 1):
            print("*", end='')
        for _ in range(n - i):
            print("*", end='')
        print("")