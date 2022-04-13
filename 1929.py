import math


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    m, n = map(int, input().split())

    for i in range(m, n + 1):
        if isPrime(i):
            print(i)