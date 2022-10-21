import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = n_list[start], n_list[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        left = init(start, mid, node * 2)
        right = init(mid + 1, end, node * 2 + 1)
        tree[node] = min(left[0], right[0]), max(left[1], right[1])
        return tree[node]


def get_min_max(start, end, node, a, b):
    if a > end or b < start:
        return 10**9+1, -1
    elif a <= start and end <= b:
        return tree[node]
    else:
        mid = (start + end) // 2
        left = get_min_max(start, mid, node * 2, a, b)
        right = get_min_max(mid + 1, end, node * 2 + 1, a, b)

        return min(left[0], right[0]), max(left[1], right[1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    tree = [-1 for _ in range(4 * n)]

    n_list = []
    for _ in range(n):
        n_list.append(int(input()))

    init(0, n - 1, 1)

    for _ in range(m):
        a, b = map(int, input().split())
        print(*get_min_max(0, n - 1, 1, a - 1, b - 1))