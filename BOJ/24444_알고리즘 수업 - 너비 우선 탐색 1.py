import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    global visited_sequence
    while queue:
        v = queue.popleft()
        visited_sequence[v] = count
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    visited_sequence = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for g in graph:
        g.sort()

    bfs(graph, r, visited)

    for sequence in visited_sequence[1:]:
        if sequence:
            print(sequence)
        else:
            print(0)