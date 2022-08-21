import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    n_list = list(map(int, sys.stdin.readline().split()))

    sum_list = [0, n_list[0], n_list[0] + n_list[1]]

    for i in range(2, n):
        sum_list.append(sum_list[i] + n_list[i])

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(sum_list[j] - sum_list[i - 1])