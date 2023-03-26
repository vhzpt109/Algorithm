import sys

sys.setrecursionlimit(10 ** 6)

count = 0


def dfs(room, x, y, d):
    if room[y][x] == 0:
        global count
        count += 1
        room[y][x] = 2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for _ in range(4):
        dd = (d + 3) % 4
        xx = x + dx[dd]
        yy = y + dy[dd]

        if room[yy][xx] == 0:
            dfs(room, xx, yy, dd)
            return
        d = dd

    dd = (d + 2) % 4
    xx = x + dx[dd]
    yy = y + dy[dd]

    if room[yy][xx] == 1:
        return
    dfs(room, xx, yy, d)


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    room = [list(map(int, input().split())) for _ in range(n)]

    dfs(room, c, r, d)
    print(count)