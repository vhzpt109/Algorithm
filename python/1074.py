number = 0


def Z(array, x, y, n):
    global number
    if n != 2:
        Z(array, x, y, n // 2)
        Z(array, x + n // 2, y, n // 2)
        Z(array, x, y + n // 2, n // 2)
        Z(array, x + n // 2, y + n // 2, n // 2)
    else:
        array[y][x] = number
        array[y][x + 1] = number + 1
        array[y + 1][x] = number + 2
        array[y + 1][x + 1] = number + 3
        number += 4


if __name__ == "__main__":
    n, r, c = map(int, input().split())

    array = [[0] * 2 ** n for _ in range(2 ** n)]

    Z(array, 0, 0, 2**n)

    print(array[r][c])