import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    graph_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for y in range(1, n):
        graph_sum[y][1] = graph_sum[y - 1][n] + graph[y - 1][n - 1]
        for x in range(2, n):
            graph_sum[y][x] = graph_sum[y][x] + graph[y][x]

    de = 10
    de = 20