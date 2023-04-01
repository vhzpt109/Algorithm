import math

if __name__ == "__main__":
    n = int(input())

    dp = [i for i in range(n + 1)]
    for i in range(4, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)

    print(dp[n])