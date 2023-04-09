if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = [int(input()) for _ in range(n)]

    dp = [1 for _ in range(k + 1)]
    dp[1] = 1

    for i in range(2, k + 1):
        for coin in coins:
            if i % coin == 0:
                dp[i] = dp[i // coin] + 1

    if dp[k] == 0:
        print(-1)
    else:
        print(dp[k])