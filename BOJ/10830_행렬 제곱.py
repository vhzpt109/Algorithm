import sys


def mul(matrix_a, matrix_b):
    size_row = len(matrix_a)
    result_matrix = [[0] * size_row for _ in range(size_row)]

    for row in range(size_row):
        for col in range(size_row):
            matrix_multiply = 0
            for i in range(size_row):
                matrix_multiply += matrix_a[row][i] * matrix_b[i][col]
            result_matrix[row][col] = matrix_multiply % 1000

    return result_matrix


def square(matrix_a, power):
    if power == 1:
        for row in range(len(matrix_a)):
            for col in range(len(matrix_a)):
                matrix_a[row][col] %= 1000
        return matrix_a

    temp = square(matrix_a, power // 2)
    if power % 2:
        return mul(mul(temp, temp), matrix_a)
    else:
        return mul(temp, temp)


input = sys.stdin.readline
if __name__ == "__main__":
    n, b = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    result_matrix = square(matrix, b)
    for row in result_matrix:
        print(*row)