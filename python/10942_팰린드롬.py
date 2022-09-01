import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if n_list[i] == n_list[i + 1]:
            dp[i][i + 1] = 1

    for i in range(2, n):
        for j in range(n - i):
            if n_list[j] == n_list[i + j] and dp[j + 1][i + j - 1] == 1:
                dp[j][i + j] = 1

    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])