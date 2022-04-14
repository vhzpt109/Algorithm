import math

def SieveOfEratosthenes():
    list = [0] * 246912
    for i in range(1, len(list)):
        list[i] = i + 1

    for i in range(len(list)):
        if list[i] == 0:
            continue
        for j in range(i + 1, int(math.sqrt(len(list))) + 1):
            if list[j] % (i + 1) == 0:
                list[j] = 0
    return list

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    list = SieveOfEratosthenes()
    n = int(input())
    while n != 0:
        cnt = 0
        list_n_2n = list[n - 1: n * 2]
        for i in range(n, n * 2 + 1):
            if i in list_n_2n:
                cnt += 1
        print(cnt)
        n = int(input())