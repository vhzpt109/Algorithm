import math

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def GetPrimeList():
    n_list = list(range(2, 246912))
    prime_list = []

    for i in n_list:
        if isPrime(i):
            prime_list.append(i)

    return prime_list

if __name__ == "__main__":
    prime_list = GetPrimeList()
    n = int(input())
    while n != 0:
        cnt = 0
        for i in prime_list:
            if n < i <= 2 * n:
                cnt += 1
        print(cnt)
        n = int(input())