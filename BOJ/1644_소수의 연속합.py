def SieveOfEratosthenes():
    sieve = [True] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i] == True]


if __name__ == "__main__":
    n = int(input())
    prime_list = SieveOfEratosthenes()

    start, end = 0, 0
    count = 0
    while end <= len(prime_list):
        prime_subtotal = sum(prime_list[start:end])
        if prime_subtotal == n:
            count += 1
            start += 1
            end += 1
        elif prime_subtotal < n:
            end += 1
        else:
            start += 1
    print(count)