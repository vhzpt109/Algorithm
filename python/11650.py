import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    list_coordinate = []
    for _ in range(n):
        list_coordinate.append(sys.stdin.readline().split())
    list_coordinate.sort()

    for coordinate in list_coordinate:
        print(coordinate[0], coordinate[1])