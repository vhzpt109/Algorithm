import sys
import copy

sys.setrecursionlimit(10**6)


def dfs(area_height, visited, threshold, x, y):
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
        if area_height[yy][xx] < threshold:
            continue

        dfs(area_height, visited, threshold, xx, yy)

    return 1


if __name__ == "__main__":
    n = int(input())
    area_height_prototype = [list(map(int, input().split())) for _ in range(n)]
    visited_prototype = [[False for _ in range(n)] for _ in range(n)]

    max_count = 0
    for threshold in range(1, 101):
        area_height = copy.deepcopy(area_height_prototype)
        visited = copy.deepcopy(visited_prototype)
        count = 0
        for y in range(n):
            for x in range(n):
                if not visited[y][x] and area_height[y][x] >= threshold:
                    dfs(area_height, visited, threshold, x, y)
                    count += 1
        max_count = max(max_count, count)
    print(max_count)