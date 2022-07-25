if __name__ == "__main__":
    s1 = list(input())
    s2 = list(input())

    dp = [[0] * (len(s1)) for _ in range(len(s2))]

    for i in range(len(s2)):
        for j in range(len(s1)):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[j] == s2[i]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

    print(max(map(max, dp)))