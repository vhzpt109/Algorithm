import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n + 1)]

    dp[1][0] = n_list[0][0]
    dp[1][1] = n_list[0][1]
    dp[1][2] = n_list[0][2]

    for i in range(2, n + 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + n_list[i - 1][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + n_list[i - 1][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + n_list[i - 1][2]

    print(min(dp[-1]))