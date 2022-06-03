def binary_search(height_list, target, start, end):
    while start <= end:
        left_len = 0
        mid = (start + end) // 2
        for height in height_list:
            temp = height - mid
            if temp > 0:
                left_len += temp
        if left_len < target:
            end = mid - 1
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    n, m = map(int, input().split())
    height_list = list(map(int, input().split()))

    print(binary_search(height_list, m, 1, max(height_list)))