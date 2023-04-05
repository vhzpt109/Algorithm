import sys

from collections import deque


def bfs(_map, visited, x, y, z):
    queue = deque([(x, y, z)])
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if _map[xx][yy] == 1 and z == 0:
                queue.append((xx, yy, 1))
                visited[xx][yy][1] = visited[x][y][0] + 1

            if _map[xx][yy] == 0 and visited[xx][yy][z] == 0:
                queue.append((xx, yy, z))
                visited[xx][yy][z] = visited[x][y][z] + 1

    return -1


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())

    _map = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    print(bfs(_map, visited, 0, 0, 0))