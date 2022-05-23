if __name__ == "__main__":
    factorial = [0] * 30
    factorial[0] = 1
    factorial[1] = 1
    for i in range(2, len(factorial)):
        factorial[i] = factorial[i - 1] * i

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        print(int(factorial[m] / (factorial[m - n] * factorial[n])))