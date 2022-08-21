import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    list_coordinate = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        list_coordinate.append((a, b))
    list_coordinate.sort()

    for coordinate in list_coordinate:
        print(coordinate[0], coordinate[1])