import sys


input = sys.stdin.readline
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        A = list(map(int, input().split()))
        A.sort()
        print(A[-3])