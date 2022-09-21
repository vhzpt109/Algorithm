import math


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def GetPrimeList():
    n_list = list(range(2, 10001))
    prime_list = []

    for i in n_list:
        if isPrime(i):
            prime_list.append(i)

    return prime_list


if __name__ == "__main__":
    t = int(input())
    prime_list = GetPrimeList()

    partition = [0] * 10001

    for i in range(len(prime_list)):
        for j in range(i, len(prime_list)):
            if prime_list[i] + prime_list[j] > 10000:
                break
            partition[prime_list[i] + prime_list[j]] = (prime_list[i], prime_list[j])

    for _ in range(t):
        n = int(input())
        print(partition[n][0], partition[n][1])