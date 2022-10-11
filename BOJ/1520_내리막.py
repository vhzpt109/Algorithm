import sys

sys.setrecursionlimit(10 ** 6)

def dfs(map_array, x, y):
    if x == n - 1 and y == m - 1:
        return 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if map_array[yy][xx] < map_array[y][x]:
            dp[y][x] += dfs(map_array, xx, yy)
    return dp[y][x]


if __name__ == "__main__":
    m, n = map(int, input().split())
    dp = [[-1] * n for _ in range(m)]

    map_array = []
    for _ in range(m):
        map_array.append(list(map(int, input().split())))

    print(dfs(map_array, 0, 0))