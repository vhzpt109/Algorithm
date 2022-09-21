import sys


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())

    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    B = []
    for _ in range(n):
        B.append(list(map(int, input().split())))

    for row in range(n):
        for col in range(m):
            print(A[row][col] + B[row][col], end=" ")
        print()