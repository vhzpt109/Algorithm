def SieveOfEratosthenes():
    list = [0] * 10000
    for i in range(1, len(list)):
        list[i] = i + 1

    for i in range(len(list)):
        if list[i] == 0:
            continue
        for j in range(i + 1, len(list)):
            if list[j] % (i + 1) == 0:
                list[j] = 0
    return list


if __name__ == "__main__":
    m = int(input())
    n = int(input())

    list = SieveOfEratosthenes()
    list_m_n = list[m - 1:n]
    while 0 in list_m_n:
        list_m_n.remove(0)

    if not list_m_n:
        print(-1)
    else:
        list_sum = sum(list_m_n)
        list_min = min(list_m_n)
        print(list_sum)
        print(list_min)