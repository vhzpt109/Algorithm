import sys
from collections import deque


def bfs(start):
    count = 1
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    return count


input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    result = []
    for i in range(1, n + 1):
        result.append(bfs(i))

    print(*result)