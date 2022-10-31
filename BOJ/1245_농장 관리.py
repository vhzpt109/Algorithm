import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(farm, x, y):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    global mountain_peak
    visited[y][x] = True

    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]

        if -1 < x < n and -1 < y < m:
            if farm[yy][xx] < farm[y][x]:
                mountain_peak = False
            if not visited[y][x] and farm[yy][xx] == farm[y][x]:
                dfs(farm, xx, yy)


if __name__ == "__main__":
    n, m = map(int, input().split())

    farm = []
    for _ in range(n):
        farm.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    count = 0
    for y in range(m):
        for x in range(n):
            if farm[y][x] > 0 and not visited[y][x]:
                mountain_peak = True
                dfs(farm, x, y)

                if mountain_peak:
                    count += 1
    print(count)