from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x_axis_len = len(grid[0])
        y_axis_len = len(grid)
        dp = [[0 for _ in range(x_axis_len + 1)] for _ in range(y_axis_len + 1)]

        for x in range(x_axis_len):
            dp[1][x + 1] = grid[0][x] + dp[1][x]
        for y in range(y_axis_len):
            dp[y + 1][1] = grid[y][0] + dp[y][1]

        for y in range(2, y_axis_len + 1):
            for x in range(2, x_axis_len + 1):
                dp[y][x] = grid[y - 1][x - 1] + min(dp[y - 1][x], dp[y][x - 1])

        return dp[y_axis_len][x_axis_len]


if __name__ == "__main__":
    obj = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(obj.minPathSum(grid))
