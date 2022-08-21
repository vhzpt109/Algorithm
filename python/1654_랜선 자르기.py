def binary_search(k_list, target, start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2
        if mid == 0:
            mid = 1
        for k in k_list:
            count += k // mid
        if count < target:
            end = mid - 1
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    k, n = map(int, input().split())
    k_list = list()
    for _ in range(k):
        k_list.append(int(input()))

    print(binary_search(k_list, n, 1, max(k_list) * 2))