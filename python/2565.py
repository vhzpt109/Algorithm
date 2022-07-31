import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    power_line = []
    for _ in range(n):
        a, b = map(int, input().split())
        power_line.append((a, b))
    power_line.sort()

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if power_line[i][1] > power_line[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))