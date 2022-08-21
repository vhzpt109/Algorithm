import sys
import math

if __name__ == "__main__":
    n, w, h = map(int, sys.stdin.readline().split())
    size_threshold = math.sqrt(w**2 + h**2)

    for _ in range(n):
        s = int(sys.stdin.readline())
        if s > size_threshold:
            print("NE")
        else:
            print("DA")