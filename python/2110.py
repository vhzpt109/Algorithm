import sys

input = sys.stdin.readline


def binary_search(x_list, start, end):
    while start <= end:
        mid = (start + end) // 2

        count = 1
        temp = x_list[0]
        for i in range(n):
            if x_list[i] >= temp + mid:
                temp = x_list[i]
                count += 1

        if count >= c:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == "__main__":
    n, c = map(int, input().split())
    x_list = []
    for _ in range(n):
        x_list.append(int(input()))
    x_list.sort()

    print(binary_search(x_list, 1, x_list[-1] - x_list[0]))