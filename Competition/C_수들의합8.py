if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    prefix_sum_A_list = [0, A[0], A[0] + A[1]]
    prefix_sum_B_list = [0, B[0], B[0] + B[1]]

    for i in range(2, n):
        prefix_sum_A_list.append(prefix_sum_A_list[i] + A[i])
        prefix_sum_B_list.append(prefix_sum_B_list[i] + B[i])

    count = 0
    for end in range(1, n + 1):
        for start in range(1, end + 1):
            if prefix_sum_A_list[end] - prefix_sum_A_list[start - 1] == prefix_sum_B_list[end] - prefix_sum_B_list[start - 1]:
                count += 1
    print(count)