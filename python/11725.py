def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return x


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
        node1, node2 = map(int, input().split())
        union_parent(parent, node1, node2)

    for i in range(2, n + 1):
        # print(find_parent(parent, i))
        print(parent[i])
