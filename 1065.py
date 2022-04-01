def cal_hansu(x):
    hansu_sum = 0
    for i in range(1, x + 1):
        num_str_list = list(map(int, str(i)))
        if i < 100:
            hansu_sum += 1
        else:
            hansu_check = True
            for j in range(len(num_str_list) - 2):
                if (num_str_list[j] - num_str_list[j + 1]) != (num_str_list[j + 1] - num_str_list[j + 2]):
                    hansu_check = False
                    break
            if hansu_check:
                hansu_sum += 1

    return hansu_sum

if __name__ == "__main__":
    x = int(input())

    print(cal_hansu(x))