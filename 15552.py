import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)