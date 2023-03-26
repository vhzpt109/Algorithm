def SieveOfEratosthenes(n, k):
    isPrime = [True for _ in range(n + 1)]
    isPrime[0], isPrime[1] = False, False

    count = 0
    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i, n + 1, i):
                if isPrime[j]:
                    isPrime[j] = False
                    count += 1
                    if count == k:
                        print(j)
                        exit(0)


if __name__ == "__main__":
    n, k = map(int, input().split())
    SieveOfEratosthenes(n, k)