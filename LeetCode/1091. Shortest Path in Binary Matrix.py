from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.dx = [1, -1, 0, 0, 1, 1, -1, -1]
        self.dy = [0, 0, 1, -1, 1, -1, -1, 1]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.bfs(grid, visited, (0, 0, 2))

    def bfs(self, grid, visited, start):
        if grid[start[1]][start[0]] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1

        queue = deque([start])

        while queue:
            x, y, c = queue.popleft()
            visited[y][x] = True
            for i in range(8):
                xx = x + self.dx[i]
                yy = y + self.dy[i]

                if xx < 0 or xx >= len(grid[0]) or yy < 0 or yy >= len(grid):
                    continue
                if visited[yy][xx]:
                    continue
                if grid[yy][xx] == 1:
                    continue
                if xx == len(grid[0]) - 1 and yy == len(grid) - 1:
                    return c

                grid[yy][xx] = c
                queue.append((xx, yy, c + 1))

        if grid[-1][-1] == 0 or grid[-1][-1] == 1:
            return -1

        return grid[-1][-1] - 1


if __name__ == "__main__":
    obj = Solution()
    grid = [[0]]
    # grid = [[0, 1], [1, 0]]
    # grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    # grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(obj.shortestPathBinaryMatrix(grid))
