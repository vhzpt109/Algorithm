import sys
sys.setrecursionlimit(10**6)


def dfs(a, target, count):
    if a == target:
        return count
    if a > target:
        return sys.maxsize

    return min(dfs(a * 2, target, count + 1), dfs(int(str(a) + "1"), target, count + 1))


if __name__ == "__main__":
    a, b = map(int, input().split())

    count = dfs(a, b, 1)
    if count == sys.maxsize:
        print(-1)
    else:
        print(count)