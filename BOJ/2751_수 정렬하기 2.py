import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    list = []

    for _ in range(n):
        list.append(int(sys.stdin.readline()))
    list.sort()

    for number in list:
        print(number)