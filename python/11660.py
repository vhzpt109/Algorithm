import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    sum_list = []
    for y in range(n):
        sub_sum_list = [0, graph[y][0]]
        for x in range(1, n):
            sub_sum_list.append(sub_sum_list[x] + graph[y][x])
        sum_list.append(sub_sum_list)

    for _ in range(m):
        y1, x1, y2, x2 = map(int, input().split())
        prefix_sum = 0
        for y in range(y1, y2 + 1):
            prefix_sum += sum_list[y - 1][x2] - sum_list[y - 1][x1 - 1]
        print(prefix_sum)