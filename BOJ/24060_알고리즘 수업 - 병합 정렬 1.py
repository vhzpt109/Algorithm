count = 0

def merge_sort(arr):
    global count
    count += 1

    if count == k:
        print(arr)

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


if __name__ == "__main__":
    n, k = map(int, input().split())
    A_list = list(map(int, input().split()))

    merge_sort(A_list)

    if count < k:
        print(-1)