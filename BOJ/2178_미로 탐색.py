from collections import deque

def bfs(maze, x, y):
    queue = deque()
    queue.append((x, y))

    global n
    global m
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue

            if maze[xx][yy] == 0:
                continue
            elif maze[xx][yy] == 1:
                maze[xx][yy] = maze[x][y] + 1
                queue.append((xx, yy))
    return maze[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())

    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))

    print(bfs(maze, 0, 0))