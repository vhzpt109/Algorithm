import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n, x = map(int, input().split())
    visitor = list(map(int, input().split()))

    prefix_sum_list = [0, visitor[0]]
    for i in range(1, n):
        prefix_sum_list.append(prefix_sum_list[i] + visitor[i])

    max_visitor = 0
    num_max_visitor = 1
    for i in range(x, len(prefix_sum_list)):
        period_visitor = prefix_sum_list[i] - prefix_sum_list[i - x]
        if max_visitor < period_visitor:
            max_visitor = period_visitor
            num_max_visitor = 1
        elif max_visitor == period_visitor:
            num_max_visitor += 1

    if max_visitor == 0:
        print("SAD")
    else:
        print(max_visitor)
        print(num_max_visitor)