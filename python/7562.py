from collections import deque


def bfs(board, night_coordinate, target_coordinate):
    queue = deque()

    queue.append((night_coordinate[0], night_coordinate[1], 0))

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    while queue:
        x, y, count = queue.popleft()
        if x == target_coordinate[0] and y == target_coordinate[1]:
            return count
        for i in range(8):
            x_move = x + dx[i]
            y_move = y + dy[i]
            if x_move < 0 or x_move >= l or y_move < 0 or y_move >= l:
                continue
            if not board[y_move][x_move]:
                board[y_move][x_move] = True
                queue.append((x_move, y_move, count + 1))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l = int(input())
        board = [[False] * l for _ in range(l)]
        night_coordinate = list(map(int, input().split()))
        target_coordinate = list(map(int, input().split()))

        print(bfs(board, night_coordinate, target_coordinate))