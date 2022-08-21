import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    n = int(input())

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for _ in range(n - 1):
        u, v = map(int, input().split())
        union_parent(parent, u, v)

    for i in range(1, n + 1):
        find_parent(parent, i)

    for i in range(1, n + 1):
        print(parent[i])