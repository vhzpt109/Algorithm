if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))

    substract_list = []
    for i in range(1, n):
        substract_list.append(n_list[i] - n_list[i - 1])

    a = b = 0
    count = 0
    for a_temp in range(1, 10):
        for b_temp in range(1, 10):
            for i in range(len(substract_list)):
                if substract_list[i] == n_list[i] * a_temp + b_temp:
                    count += 1
                    a = a_temp
                    b = b_temp

    if count > 1:
        print('A')
    elif count == 0:
        print('A')
    else:
        print(a, b)
