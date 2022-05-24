def two_cnt(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt

def five_cnt(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())

    n_two = two_cnt(n) - two_cnt(m) - two_cnt(n - m)
    n_five = five_cnt(n) - five_cnt(m) - five_cnt(n - m)

    print(min(n_two, n_five))