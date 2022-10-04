if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))

    if n == 1:
        print('A')
    elif n == 2:
        if n_list[0] == n_list[1]:
            print(n_list[0])
        else:
            print('A')
    else:
        if n_list[1] - n_list[0] == 0:
            a = 0
            b = n_list[1]
        else:
            a = (n_list[2] - n_list[1]) // (n_list[1] - n_list[0])
            b = n_list[1] - n_list[0] * a

    print(n_list[n - 1] * a + b)