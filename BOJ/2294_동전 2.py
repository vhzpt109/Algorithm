if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))
    coins.sort()

    dp = [i for i in range(k + 1)]

    for i in range(min(coins), k + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i % coin] + i // coin)

    if dp[k] == k:
        print(-1)
    else:
        print(dp[k])