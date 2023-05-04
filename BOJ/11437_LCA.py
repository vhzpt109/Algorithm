import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(node, d):
    visited[node] = True
    depth[node] = d

    for leaf in tree[node]:
        if visited[leaf]:
            continue
        parent[leaf] = node
        dfs(leaf, d + 1)


def findLCA(node1, node2):
    while depth[node1] != depth[node2]:
        if depth[node1] > depth[node2]:
            node1 = parent[node1]
        else:
            node2 = parent[node2]

    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]

    return node1


if __name__ == "__main__":
    n = int(input())

    tree = [[] for _ in range(n + 1)]
    parent = [0 for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for _ in range(n - 1):
        node1, node2 = map(int, input().split())
        tree[node1].append(node2)
        tree[node2].append(node1)

    dfs(1, 0)

    m = int(input())
    for _ in range(m):
        node1, node2 = map(int, input().split())

        print(findLCA(node1, node2))