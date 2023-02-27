def rotate(arr, n):
    if not arr:
        return arr
    n %= len(arr)
    if not n:
        return arr

    left = arr[:-n]
    right = arr[-n:]

    return right + left


if __name__ == "__main__":
    n, m = map(int, input().split())

    basket = [number + 1 for number in range(n)]

    for _ in range(m):
        i, j, k = map(int, input().split())
        temp = basket[i - 1:j]
        temp = rotate(basket, k)
        for idx in range(j - i + 1):
            basket[i - 1 + idx] = temp[idx]

    print(*basket)