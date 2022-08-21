import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    list_number = [0] * 10001
    for _ in range(n):
        list_number[int(sys.stdin.readline())] += 1

    for i in range(len(list_number)):
        for _ in range(list_number[i]):
            print(i)