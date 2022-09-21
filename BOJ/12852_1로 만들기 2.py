if __name__ == "__main__":
    X = int(input())

    dp = [[0, []] for _ in range(X + 1)]
    dp[1][1] = [1]

    for i in range(2, X + 1):
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = dp[i - 1][1] + [i]

        if i % 2 == 0 and dp[i][0] > dp[i // 2][0] + 1:
            dp[i][0] = dp[i // 2][0] + 1
            dp[i][1] = dp[i // 2][1] + [i]

        if i % 3 == 0 and dp[i][0] > dp[i // 3][0] + 1:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = dp[i // 3][1] + [i]

    print(dp[X][0])
    print(*reversed(dp[X][1]))