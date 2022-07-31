import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for j in range(n):
        w, v = map(int, input().split())
        for i in range(w):
            if w + i <= k:
                dp[i][j] = max(dp[i][j - 1], dp[i][j - 1] + v)
            else:
                dp[i][j] = dp[i][j - 1]
    de = 10
    print(dp[k][n])