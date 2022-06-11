if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    x = int(input())

    start = 0
    end = n - 1
    count = 0
    while start < end:
        sum_start_end = n_list[start] + n_list[end]
        if sum_start_end == x:
            count += 1

        if sum_start_end > x:
            end -= 1
            continue
        start += 1
    print(count)