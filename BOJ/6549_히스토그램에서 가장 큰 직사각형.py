if __name__ == "__main__":
    while True:
        h_list = list(map(int, input().split()))
        n = h_list.pop(0)

        if n == 0:
            break

        max_value = 0
        for i in range(len(h_list)):
            for j in range(i + 1, len(h_list)):
                if h_list[i] <= h_list[j]:
                    max_value = max(max_value, h_list[i] * (j - i + 1))
                else:
                    break
        print(max_value)