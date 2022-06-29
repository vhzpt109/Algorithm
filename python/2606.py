def dfs(graph, start, visited):
    visited[start] = True
    global count
    count += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

if __name__ == "__main__":
    n_computer = int(input())
    n_connect = int(input())
    graph = [[] for _ in range(n_computer + 1)]
    visited = [False] * (n_computer + 1)

    for _ in range(n_connect):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = -1 # 자기 자신인 1은 빼고
    dfs(graph, 1, visited)
    print(count)