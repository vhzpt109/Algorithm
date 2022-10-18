import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
DIV = 1000000007


def init(start, end, node):
    if start == end:
        tree[node] = n_list[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1) % DIV
        return tree[node]


def multiply(start, end, node, left, right):
    if left > end or right < start:
        return
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return multiply(start, mid, node * 2, left, right) * multiply(mid + 1, end, node * 2 + 1, left, right) % DIV


def update(start, end, node, index, diff):
    if index < start or index > end:
        pass
    else:
        tree[node] /= diff
        if start == end:
            pass
        else:
            mid = (start + end) // 2
            update(start, mid, node * 2, index, diff)
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
            diff = n_list[b - 1]
            n_list[b - 1] = c
            update(0, n - 1, 1, b - 1, diff)
        elif a == 2:
            print(multiply(0, n - 1, 1, b - 1, c - 1))