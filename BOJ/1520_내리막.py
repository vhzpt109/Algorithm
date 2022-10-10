from collections import deque


def bfs(map_array, start):
    queue = deque()
    queue.append((start[0], start[1]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if map_array[yy][xx] == 1 or map_array[yy][xx] == -1:
                continue
            elif map_array[yy][xx] == 0:
                map_array[yy][xx] = map_array[y][x] + 1
                queue.append((xx, yy))


if __name__ == "__main__":
    m, n = map(int, input().split())
    map_array = []
    for _ in range(m):
        map_array.append(list(map(int, input().split())))

    bfs(map_array, (0, 0))
