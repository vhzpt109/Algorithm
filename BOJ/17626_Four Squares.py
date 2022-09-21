import math

if __name__ == "__main__":
    n = int(input())

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        minval = 1e9
        for j in range(1, int(math.sqrt(i)) + 1):
            minval = min(minval, dp[i - (j**2)])
        dp[i] = minval + 1
    print(dp[n])