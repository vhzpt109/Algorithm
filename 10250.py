import math

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        h, w, n = map(int, input().split())

        floors = n % h if n % h != 0 else h
        rooms = math.ceil(n / h)

        print(str(floors) + "{0:02d}".format(rooms))