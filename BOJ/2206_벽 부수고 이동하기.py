import sys

from collections import deque


def bfs(_map, visited, x, y, z, distance):
    queue = deque([(x, y, z, distance)])
    visited[y][x][z] = True

    while queue:
        x, y, z, distance = queue.popleft()
        if x == m - 1 and y == n - 1:
            return distance

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if _map[yy][xx] == 1 and z == 0:
                visited[yy][xx][1] = True
                queue.append((xx, yy, 1, distance + 1))
            elif _map[yy][xx] == 0 and visited[yy][xx][z] is False:
                visited[yy][xx][z] = True
                queue.append((xx, yy, z, distance + 1))

    return -1


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())

    _map = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    print(bfs(_map, visited, 0, 0, 0, 1))