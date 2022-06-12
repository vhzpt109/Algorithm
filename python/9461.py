if __name__ == "__main__":
    t = int(input())

    dp = [0] * 100
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, 100):
        dp[i] = dp[i - 2] + dp[i - 3]

    for _ in range(t):
        n = int(input())
        print(dp[n - 1])