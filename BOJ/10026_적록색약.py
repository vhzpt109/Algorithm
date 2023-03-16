import sys
import copy
sys.setrecursionlimit(10**6)


def dfs(figure, visited, x, y):
    visited[y][x] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
        if visited[yy][xx]:
            continue
        if figure[y][x] != figure[yy][xx]:
            continue

        dfs(figure, visited, xx, yy)

    return 1


if __name__ == "__main__":
    n = int(input())
    figure = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    figure_blind = copy.deepcopy(figure)
    visited_blind = copy.deepcopy(visited)

    count = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                dfs(figure, visited, x, y)
                count += 1
    print(count, end=" ")

    for y in range(n):
        for x in range(n):
            if figure_blind[y][x] == 'R':
                figure_blind[y][x] = 'G'
    blind_count = 0
    for y in range(n):
        for x in range(n):
            if not visited_blind[y][x]:
                dfs(figure_blind, visited_blind, x, y)
                blind_count += 1
    print(blind_count)