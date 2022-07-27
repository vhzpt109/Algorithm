if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * n for _ in range(9)]

    for i in range(n - 1):
        substract = abs(A[i] - A[i + 1])
        dp[substract - 1][i] = max(dp[substract - 1]) + 1

    print(max(map(max, dp)) + 1)