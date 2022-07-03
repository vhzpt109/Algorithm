from collections import deque


def bfs(storage, tomato_coordinates):
    queue = deque()
    for coordinate in tomato_coordinates:
        queue.append((coordinate[0], coordinate[1], coordinate[2]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dz = [-1, 1]

    while queue:
        z, x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if storage[z][yy][xx] == 1 or storage[z][yy][xx] == -1:
                continue
            elif storage[z][yy][xx] == 0:
                storage[z][yy][xx] = storage[z][y][x] + 1
                queue.append((z, xx, yy))
        for i in range(2):
            zz = z + dz[i]
            if zz < 0 or zz >= h:
                continue
            if storage[zz][y][x] == 1 or storage[zz][y][x] == -1:
                continue
            elif storage[zz][y][x] == 0:
                storage[zz][y][x] = storage[z][y][x] + 1
                queue.append((zz, x, y))


if __name__ == "__main__":
    m, n, h = map(int, input().split())
    storage = []
    for i in range(h):
        sub_storage = []
        for _ in range(n):
            sub_storage.append(list(map(int, input().split())))
        storage.append(sub_storage)

    tomato_coordinates = [(z, x, y) for z in range(h) for y in range(n) for x in range(m) if storage[z][y][x] == 1]

    bfs(storage, tomato_coordinates)

    max_day = 0
    is_raw_tomato = False
    for channel in storage:
        for row in channel:
            max_row = max(row)
            max_day = max(max_day, max_row)
            is_raw_tomato = is_raw_tomato or (True if row.count(0) > 0 else False)

    if is_raw_tomato:
        print(-1)
    else:
        print(max_day - 1)