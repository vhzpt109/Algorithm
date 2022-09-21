import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(n)]

    m, k = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(m)]

    for i in range(n):
        matrix = []
        for y in range(k):
            matrix_multiply = 0
            for x in range(m):
                matrix_multiply += A[i][x] * B[x][y]
            matrix.append(matrix_multiply)
        print(*matrix)