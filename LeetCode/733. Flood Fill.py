from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        targetColor = image[sr][sc]
        self.dfs(image, sc, sr, visited, color, targetColor)

        return image

    def dfs(self, image, x, y, visited, color, targetColor):
        visited[y][x] = True
        image[y][x] = color

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(image[0]) or ny < 0 or ny >= len(image):
                continue
            if visited[ny][nx]:
                continue
            if image[ny][nx] != targetColor:
                continue

            self.dfs(image, nx, ny, visited, color, targetColor)


if __name__ == "__main__":
    obj = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(obj.floodFill(image, sr, sc, color))
