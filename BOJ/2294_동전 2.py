if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))
    coins = [coin for coin in coins if coin <= k]

    dp = [10001 for _ in range(k + 1)]
    dp[0] = 0

    for i in range(min(coins), k + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[k] == 10001:
        print(-1)
    else:
        print(dp[k])