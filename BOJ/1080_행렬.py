def flip(matrix, x, y):
    for yy in range(y, y + 3):
        for xx in range(x, x + 3):
            if matrix[yy][xx] == 0:
                matrix[yy][xx] = 1
            else:
                matrix[yy][xx] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix_a = [list(map(int, list(input()))) for _ in range(n)]
    matrix_b = [list(map(int, list(input()))) for _ in range(n)]

    count = 0
    if (n < 3 or m < 3) and matrix_a != matrix_b:
        count = -1
    else:
        for y in range(n - 2):
            for x in range(m - 2):
                if matrix_a[y][x] != matrix_b[y][x]:
                    count += 1
                    flip(matrix_a, x, y)

    if count != -1:
        if matrix_a != matrix_b:
            count = -1

    print(count)