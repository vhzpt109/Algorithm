import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = n_list[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
        return tree[node]


def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, index, diff):
    if index < start or index > end:
        pass
    else:
        tree[node] = diff
        if start == end:
            pass
        else:
            mid = (start + end) // 2
            update(start, mid, node + 2, index, diff)
            update(mid + 1, end, node * 2 + 1, index, diff)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    tree = [[-1] for _ in range(4 * n)]

    n_list = []
    for _ in range(n):
        n_list.append(int(input()))

    init(0, n - 1, 1)

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(0, n - 1, 1, b - 1, c)
        elif a == 2:
            print(sum(0, n - 1, 1, b - 1, c - 1))