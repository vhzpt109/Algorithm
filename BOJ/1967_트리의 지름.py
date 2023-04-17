import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
