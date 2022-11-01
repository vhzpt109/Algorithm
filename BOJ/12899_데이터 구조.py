import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
RANGE = int(2e6)


def search(start, end, node, k):
    return


def update(start, end, node, index):
    if index < start or index > end:
        return
    else:
        tree[node] += 1
        if start == end:
            return
        else:
            mid = (start + end) // 2
            update(start, mid, node * 2, index)
            update(mid + 1, end, node * 2 + 1, index)


if __name__ == "__main__":
    n = int(input())

    tree = [[-1] for _ in range(RANGE)]
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            update(0, RANGE, 1, x)
        else:
            print(search(0, RANGE, 1, x))