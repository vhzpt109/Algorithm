import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().split())))

    dp = [[0] * i for i in range(n + 1)]
    dp[1][0] = triangle[0][0]
    if n == 1:
        print(dp[1][0])
        exit(0)

    dp[2][0] = triangle[0][0] + triangle[1][0]
    dp[2][1] = triangle[0][0] + triangle[1][1]

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + triangle[i - 1][0]
        for j in range(1, len(dp[i]) - 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i - 1][j]
        dp[i][-1] = dp[i - 1][-1] + triangle[i - 1][-1]

    print(max(dp[-1]))