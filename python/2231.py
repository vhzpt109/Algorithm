if __name__ == "__main__":
    n = int(input())
    n_str_list = list(str(n))

    result = 0
    for i in range(n):
        i_str_list = list(str(i))
        sum = i
        for i_str in i_str_list:
            sum += int(i_str)
        if sum == n:
            result = i
            break
    print(result)