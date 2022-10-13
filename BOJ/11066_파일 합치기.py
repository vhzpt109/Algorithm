if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        file_size = list(map(int, input().split()))
        dp = [[0] * (k + 1) for _ in range(k + 1)]

        for i in range(k - 1):
            dp[i][i + 1] = file_size[i] + file_size[i + 1]
            for j in range(i + 2, k):
                dp[i][j] = dp[i][j - 1] + file_size[j]

        for v in range(2, k):
            for i in range(k - v):
                j = i + v
                dp[i][j] += min([dp[i][z] + dp[z + 1][j] for z in range(i, j)])

        print(dp[0][k - 1])