if __name__ == "__main__":
    n, s = map(int, input().split())
    sequence = list(map(int, input().split()))

    sequence_sum_list = [0, sequence[0], sequence[0] + sequence[1]]

    for i in range(2, n):
        sequence_sum_list.append(sequence_sum_list[i] + sequence[i])

    start, end = 0, 1
    shortest_length = 100001
    while start != n:
        if sequence_sum_list[end] - sequence_sum_list[start] >= s:
            shortest_length = min(shortest_length, end - start)

            start += 1
        else:
            if end != n:
                end += 1
            else:
                start += 1

    print(shortest_length if shortest_length != 100001 else 0)