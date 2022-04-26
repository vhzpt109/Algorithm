import sys


def NGE(A, Ai):
    for a in A:
        if a > Ai:
            return a
    else:
        return -1


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    A = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        print(NGE(A[i + 1:], A[i]), end=" ")