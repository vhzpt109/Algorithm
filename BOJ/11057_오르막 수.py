if __name__ == "__main__":
    n = int(input())

    dp = [[1 for _ in range(10)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, 10):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    print(dp[n][9] % 10007)