import math

if __name__ == "__main__":
    a, b, v = map(int, input().split())

    day = math.ceil((v - a) / (a - b)) + 1

    print(day)