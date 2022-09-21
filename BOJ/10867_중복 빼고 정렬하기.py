if __name__ == "__main__":
    n = int(input())
    n_set = set(map(int, input().split()))
    n_list = list(n_set)
    n_list.sort()

    print(*n_list)