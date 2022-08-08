import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    graph_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for y in range(1, n + 1):
        # graph_sum[y][0] = graph_sum[y - 1][n]
        graph_sum[y][1] = graph_sum[y - 1][n] + graph[y - 1][0]
        for x in range(2, n + 1):
            graph_sum[y][x] = graph_sum[y][x - 1] + graph[y - 1][x - 1]

    for _ in range(m):
        y1, x1, y2, x2 = map(int, input().split())
        prefix_sum = graph_sum[y2][x2] - graph_sum[y1][x1 - 1]
        # print(prefix_sum)
        print(graph_sum[x2][y2] - graph_sum[x2][y1 - 1] - graph_sum[x1 - 1][y2] + graph_sum[x1 - 1][y1 - 1])