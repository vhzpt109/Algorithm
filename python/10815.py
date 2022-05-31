def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    m = int(input())
    m_list = list(map(int, input().split()))

    for m in m_list:
        print(binary_search(n_list, m, 0, n - 1), end=" ")