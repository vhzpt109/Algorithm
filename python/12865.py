import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    belongings = [[0, 0]]

    for _ in range(n):
        w, v = map(int, input().split())
        belongings.append((w, v))

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            weight = belongings[i][0]
            value = belongings[i][1]

            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

    print(dp[n][k])