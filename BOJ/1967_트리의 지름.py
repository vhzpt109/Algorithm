import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, weight_sum):
    for start_node in graph[x]:
        node, weight = start_node
        if distance[node] == -1:
            distance[node] = weight_sum + weight
            dfs(node, weight_sum + weight)


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        graph[parent].append([child, weight])
        graph[child].append([parent, weight])

    distance = [-1] * (n + 1)
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))
    distance = [-1] * (n + 1)
    distance[start] = 0
    dfs(start, 0)

    print(max(distance))