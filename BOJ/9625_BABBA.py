if __name__ == "__main__":
    k = int(input())

    dp = [0 for _ in range(k + 2)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, k + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[k - 2], dp[k - 1])