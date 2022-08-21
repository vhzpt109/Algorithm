import math

if __name__ == "__main__":
    n = int(input())

    count = 0
    while n > 0:
        if math.sqrt(n) > 1:
            n -= int(math.sqrt(n))**2
            count += 1
        else:
            count += 1
            break
    print(count)