def two_cnt(n):
    cnt = 0
    for i in range(1, n):
        if i % 2 == 0:
            cnt += 1
    return cnt

def five_cnt(n):
    cnt = 0
    for i in range(1, n):
        if i % 5 == 0:
            cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())

    n_two = two_cnt(n)
    n_five = five_cnt(n)

    m_two = two_cnt(m)
    m_five = five_cnt(m)

    n_m_two = two_cnt(n - m)
    n_m_five = five_cnt(n - m)

    result = n_two + m