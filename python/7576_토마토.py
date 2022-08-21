from collections import deque


def bfs(storage, tomato_coordinates):
    queue = deque()
    for coordinate in tomato_coordinates:
        queue.append((coordinate[0], coordinate[1]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if storage[yy][xx] == 1 or storage[yy][xx] == -1:
                continue
            elif storage[yy][xx] == 0:
                storage[yy][xx] = storage[y][x] + 1
                queue.append((xx, yy))


if __name__ == "__main__":
    m, n = map(int, input().split())
    storage = []
    for _ in range(n):
        storage.append(list(map(int, input().split())))

    tomato_coordinates = [(x, y) for y in range(n) for x in range(m) if storage[y][x] == 1]

    bfs(storage, tomato_coordinates)

    max_day = 0
    is_raw_tomato = False
    for row in storage:
        max_row = max(row)
        max_day = max(max_day, max_row)
        is_raw_tomato = is_raw_tomato or (True if row.count(0) > 0 else False)

    if is_raw_tomato:
        print(-1)
    else:
        print(max_day - 1)