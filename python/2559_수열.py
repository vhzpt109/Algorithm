if __name__ == "__main__":
    n, k = map(int, input().split())
    n_list = list(map(int, input().split()))

    sum_list = [0, n_list[0], n_list[0] + n_list[1]]

    for i in range(2, n):
        sum_list.append(sum_list[i] + n_list[i])

    subsum_list = []
    for i in range(k, n + 1):
        subsum_list.append(sum_list[i] - sum_list[i - k])
    print(max(subsum_list))