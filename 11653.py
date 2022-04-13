if __name__ == "__main__":
    n = int(input())

    prime_factor = 2
    while prime_factor <= n:
        if n % prime_factor == 0:
            print(prime_factor)
            n = n // prime_factor
            prime_factor = 2
        else:
            prime_factor += 1