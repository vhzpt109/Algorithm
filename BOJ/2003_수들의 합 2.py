if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    prefix_sum_A_list = [0, A[0]]

    for i in range(1, n):
        prefix_sum_A_list.append(prefix_sum_A_list[i] + A[i])

    start, end = 0, 0
    count = 0
    while start <= end and end <= n:
        sum_two_point = prefix_sum_A_list[end] - prefix_sum_A_list[start]
        if sum_two_point == m:
            count += 1
            start += 1
            end += 1
        elif sum_two_point > m:
            start += 1
        else:
            end += 1

    print(count)