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
        if y1 == y2 and x1 == x2:
            print(sum_list[y2 - 1][x2] - sum_list[y2 - 1][x1 - 1])
        else:
            print(sum_list[y2 - 1][x2] - sum_list[y2 - 1][x1 - 1] + sum_list[y1 - 1][x2] - sum_list[y1 - 1][x1 - 1])