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
        graph[b].append(a)

    max_count = 1
    result = []
    for i in range(1, n + 1):
        count = bfs(i)
        if count > max_count:
            max_count = count
            result.clear()
            result.append(i)
        elif count == max_count:
            result.append(i)

    print(*result)