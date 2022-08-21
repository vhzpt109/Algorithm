import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    stack = []
    result = [-1 for i in range(n)]

    for i in range(len(A)):
        while stack and A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
        stack.append(i)

    print(*result)