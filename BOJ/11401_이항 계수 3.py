MOD = 1000000007


def pow(a, b):
    if b == 0:
        return 1
    elif b % 2 > 0:
        return (pow(a, b - 1) * a) % MOD
    else:
        temp = pow(a, b / 2) % MOD
        return (temp * temp) % MOD


if __name__ == "__main__":
    n, k = map(int, input().split())

    A = B = 1
    for i in range(1, n + 1):
        A *= i
        A %= MOD
    for i in range(1, k + 1):
        B *= i
        B %= MOD
    for i in range(1, n - k + 1):
        B *= i
        B %= MOD

    result = pow(B, MOD - 2)
    result *= A
    result %= MOD
    print(result)