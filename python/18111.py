import sys

if __name__ == "__main__":
    n, m, b = map(int, sys.stdin.readline().split())

    block = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    print(block)