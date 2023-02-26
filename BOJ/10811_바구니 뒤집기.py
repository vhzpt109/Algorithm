if __name__ == "__main__":
    n, m = map(int, input().split())

    basket = [number + 1 for number in range(n)]

    for _ in range(m):
        i, j = map(int, input().split())
        temp = basket[i - 1:j]
        temp = temp[::-1]
        for idx in range(j - i + 1):
            basket[i - 1 + idx] = temp[idx]

    print(*basket)