from collections import Counter

if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    m = int(input())
    m_list = list(map(int, input().split()))

    n_list_counter = Counter(n_list)
    for m in m_list:
        print(n_list_counter[m], end=" ")