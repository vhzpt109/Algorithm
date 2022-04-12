import math

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())

    list = list(map(int, input().split()))

    prime_cnt = 0
    for number in list:
        if isPrime(number):
            prime_cnt += 1
    print(prime_cnt)