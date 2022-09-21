if __name__ == "__main__":
    n, m = map(int, input().split())

    s = []
    for _ in range(n):
        s.append(input())
    s.sort()

    m_list = []
    for _ in range(m):
        m_list.append(input())
    m_list.sort()

    count = 0
    for m in m_list:
        if m in s:
            count += 1
    print(count)