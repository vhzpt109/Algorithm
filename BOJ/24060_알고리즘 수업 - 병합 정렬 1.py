import sys

input = sys.stdin.readline


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            result.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            result.append(right[j])
            j += 1
    while i < len(left):
        temp.append(left[i])
        result.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        result.append(right[j])
        j += 1

    return temp


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    merge_sort(arr)

    if len(result) >= k:
        print(result[k - 1])
    else:
        print(-1)