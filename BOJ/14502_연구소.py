from collections import deque


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
    n, m = map(int, input().split())
    _map = []
    for _ in range(n):
        _map.append(list(map(int, input().split())))

    print(_map[0].index(2))