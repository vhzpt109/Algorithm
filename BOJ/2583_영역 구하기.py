import sys
sys.setrecursionlimit(10**6)


def draw_rectangle(graph_paper, x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph_paper[y][x] = 1


def dfs(graph_paper, x, y, visited):
    visited[y][x] = True

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if visited[yy][xx]:
            continue
        if graph_paper[yy][xx] == 1:
            continue

        global count
        count += 1
        dfs(graph_paper, xx, yy, visited)


if __name__ == "__main__":
    m, n, k = map(int, input().split())

    graph_paper = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        draw_rectangle(graph_paper, x1, y1, x2, y2)

    count_list = []
    count = 0
    for y in range(m):
        for x in range(n):
            if not visited[y][x] and graph_paper[y][x] != 1:
                count += 1
                dfs(graph_paper, x, y, visited)
                count_list.append(count)
                count = 0

    count_list.sort()
    print(len(count_list))
    print(*count_list)