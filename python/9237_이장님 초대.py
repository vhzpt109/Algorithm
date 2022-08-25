if __name__ == "__main__":
    n = int(input())
    t_list = list(map(int, input().split()))
    t_list.sort()

    for i in range(n):
        t_list[i] -= i

    print(max(t_list) + n + 1)