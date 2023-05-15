from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        num_of_islands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if visited[y][x] is False and grid[y][x] == '1':
                    num_of_islands += 1
                    self.dfs(grid, x, y, visited)

        return num_of_islands

    def dfs(self, grid, x, y, visited):
        visited[y][x] = True

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                continue
            if visited[ny][nx]:
                continue
            if grid[ny][nx] == '0':
                continue

            self.dfs(grid, nx, ny, visited)


if __name__ == "__main__":
    obj = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(obj.numIslands(grid))