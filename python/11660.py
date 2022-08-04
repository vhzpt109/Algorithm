import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    graph_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for y in range(1, n):
        for x in range(1, n):
            graph_sum[y][x] = graph_sum[y - 1][x] + graph_sum[y][x - 1] + graph[y][x]