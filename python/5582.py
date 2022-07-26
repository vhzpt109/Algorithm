if __name__ == "__main__":
    s1 = input().rstrip()
    s2 = input().rstrip()

    dp = [[0] * len(s2) for _ in range(len(s1))]

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1

    print(max(map(max, dp)))