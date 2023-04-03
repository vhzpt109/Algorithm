import sys
import copy

from collections import deque


def bfs(_map, visited, x, y):
    queue = deque([(x, y, 1)])
    visited[y][x] = True

    while queue:
        x, y, distance = queue.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if visited[yy][xx]:
                continue
            if _map[yy][xx] == 1:
                continue

            _map[yy][xx] = distance + 1
            queue.append((xx, yy, distance + 1))
            visited[yy][xx] = True


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())

    _map = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    wall_list = [(x, y) for x in range(m) for y in range(n) if _map[y][x] == 1]
    wall_list.insert(0, (0, 0))

    min_distance = 1415
    for wall in wall_list:
        _map_clone = copy.deepcopy(_map)
        _map_clone[wall[1]][wall[0]] = 0
        visited_clone = copy.deepcopy(visited)
        bfs(_map_clone, visited_clone, 0, 0)
        if _map_clone[n - 1][m - 1] != 0:
            min_distance = min(min_distance, _map_clone[n - 1][m - 1])

    print(min_distance if min_distance != 1415 else -1)