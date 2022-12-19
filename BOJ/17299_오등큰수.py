import sys
from collections import Counter

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    A_nums_count = Counter(A)

    stack = []
    result = [-1 for i in range(n)]

    for i in range(len(A)):
        while stack and A_nums_count[A[stack[-1]]] < A_nums_count[A[i]]:
            result[stack.pop()] = A[i]
        stack.append(i)

    print(*result)