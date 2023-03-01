if __name__ == "__main__":
    n, k = map(int, input().split())

    count = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            count += 1
        if count == k:
            print(i)
            exit(0)
    count += 1
    if count == k:
        print(n)
    else:
        print(0)