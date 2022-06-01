if __name__ == "__main__":
    n, m = map(int, input().split())

    n_set = set()
    for _ in range(n):
        n_set.add(input())

    m_set = set()
    for _ in range(m):
        m_set.add(input())

    n_m_intersection = n_set.intersection(m_set)
    n_m_intersection = list(n_m_intersection)
    n_m_intersection.sort()

    print(len(n_m_intersection))
    for intersection in n_m_intersection:
        print(intersection)