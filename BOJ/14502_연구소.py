import sys
import copy

from itertools import combinations
from collections import deque


def bfs(_map, virus) -> list:
    queue = deque()
    queue.extend(virus)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue

            if _map[yy][xx] == 1 or _map[yy][xx] == 2:
                continue
            else:
                _map[yy][xx] = 2
                queue.append((xx, yy))
    return _map


def countSafeArea(_map) -> int:
    count = 0
    for row in _map:
        count += row.count(0)
    return count


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    _map = []
    for _ in range(n):
        _map.append(list(map(int, input().split())))

    max_count = 0
    safe_area = [(x, y) for x in range(m) for y in range(n) if _map[y][x] == 0]
    wall_positions_combination = combinations(safe_area, 3)
    for wall_positions in wall_positions_combination:
        _map_clone = copy.deepcopy(_map)
        _map_clone[wall_positions[0][1]][wall_positions[0][0]] = 1
        _map_clone[wall_positions[1][1]][wall_positions[1][0]] = 1
        _map_clone[wall_positions[2][1]][wall_positions[2][0]] = 1

        virus = [(x, y) for x in range(m) for y in range(n) if _map[y][x] == 2]
        _map_clone = bfs(_map_clone, virus)
        count = countSafeArea(_map_clone)
        max_count = max(max_count, count)

    print(max_count)