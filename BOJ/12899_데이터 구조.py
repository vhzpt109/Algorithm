import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
RANGE = int(2e6) + 2


def search(start, end, node, kth):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        if kth <= tree[node * 2]:
            return search(start, mid, node * 2, kth)
        else:
            return search(mid + 1, end, node * 2 + 1, kth - tree[node * 2])


def update(start, end, node, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] += value
        return
    else:
        mid = (start + end) // 2
        update(start, mid, node * 2, index, value)
        update(mid + 1, end, node * 2 + 1, index, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


if __name__ == "__main__":
    n = int(input())

    tree = [0 for _ in range(4 * RANGE)]
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            update(1, RANGE, 1, x, 1)
        else:
            kth = search(1, RANGE, 1, x)
            print(kth)
            update(1, RANGE, 1, kth, -1)