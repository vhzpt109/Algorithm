if __name__ == "__main__":
    n_list = []
    for _ in range(9):
        n_list.append(int(input()))

    for i in range(8):
        for j in range(i + 1, 9):
            n_i = n_list[i]
            n_j = n_list[j]
            n_sum = sum(n_list) - n_i - n_j
            if n_sum == 100:
                n_list.remove(n_i)
                n_list.remove(n_j)
                break
        if len(n_list) == 7:
            break

    for n in n_list:
        print(n)