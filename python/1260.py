import sys
from collections import deque

input = sys.stdin.readline


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for g in graph:
        g.sort()

    visited = [False] * (n + 1)
    dfs(graph, r, visited)
    print()
    visited = [False] * (n + 1)
    bfs(graph, r, visited)