import sys

if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    start, end = 0, n - 1
    close_to_zero_value = sys.maxsize
    close_to_zero_start_idx = -1
    close_to_zero_end_idx = -1

    while start < end:
        sum_start_end = n_list[start] + n_list[end]
        if close_to_zero_value > abs(sum_start_end):
            close_to_zero_value = abs(sum_start_end)
            close_to_zero_start_idx = start
            close_to_zero_end_idx = end
            if close_to_zero_value == 0:
                break

        if sum_start_end < 0:
            start += 1
        else:
            end -= 1

    print(n_list[close_to_zero_start_idx], n_list[close_to_zero_end_idx])