from collections import deque


def bfs(start, visited):
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        position, time = queue.popleft()
        if position == k:
            return time

        for position_move in (position - 1, position + 1, position * 2):
            if not 0 <= position_move <= 100000:
                continue
            if not visited[position_move]:
                queue.append((position_move, time + 1))
                visited[position_move] = True


if __name__ == "__main__":
    n, k = map(int, input().split())
    visited = [False] * 100001

    print(bfs(n, visited))