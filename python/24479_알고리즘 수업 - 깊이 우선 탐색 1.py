import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    global count
    global visited_sequence
    visited_sequence[v] = count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    visited_sequence = [[] for _ in range(n + 1)]
    count = 1

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for g in graph:
        g.sort()

    dfs(graph, r, visited)

    for sequence in visited_sequence[1:]:
        if sequence:
            print(sequence)
        else:
            print(0)