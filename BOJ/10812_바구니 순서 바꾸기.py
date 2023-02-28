def rotate(arr, n):
    mid = n

    begin = arr[:mid]
    end = arr[mid:]

    return end + begin


if __name__ == "__main__":
    n, m = map(int, input().split())

    basket = [number + 1 for number in range(n)]

    for _ in range(m):
        i, j, k = map(int, input().split())
        temp = basket[i - 1:j]
        temp = rotate(temp, k - i)
        for idx in range(j - i + 1):
            basket[i - 1 + idx] = temp[idx]

    print(*basket)