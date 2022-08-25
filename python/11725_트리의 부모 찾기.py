import sys
sys.setrecursionlimit(10**6)


input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)


if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    parent = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    print(*parent[2:], sep='\n')