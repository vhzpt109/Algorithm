def dfs(room, visited, x, y):
    visited[y][x] = True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= (m - 1) or yy < 0 or yy >= (n - 1):
            continue
        if visited[yy][xx]:
            continue
        if room[yy][xx] == 1:
            continue

        dfs(room, visited, xx, yy)


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    room = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    dfs(room, visited, r - 1, c - 1)
    count = 0
    for i in range(n):
        count += visited[i].count(True)
    print(count)





