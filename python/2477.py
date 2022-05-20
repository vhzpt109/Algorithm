if __name__ == "__main__":
    k = int(input())

    excluded_area = 0
    direction_length_list = []
    for _ in range(6):
        direction, length = map(int, input().split())
        direction_length_list.append((direction, length))

    for i in range(len(direction_length_list) - 1):
        excluded_area += direction_length_list[i][1] * direction_length_list[i + 1][1]
    excluded_area += direction_length_list[-1][1] * direction_length_list[0][1]
    print(excluded_area)

    square_area = 0
    info_max_d_l_list = max(direction_length_list, key=lambda x:x[1])
    if info_max_d_l_list[0] > 0:
        if direction_length_list[info_max_d_l_list[0] - 1] > direction_length_list[info_max_d_l_list[0] + 1]:
            square_area = info_max_d_l_list[1] * direction_length_list[info_max_d_l_list[0] - 1][1]
        else:
            square_area = info_max_d_l_list[1] * direction_length_list[info_max_d_l_list[0] + 1][1]
        square_area = square_area * 3

    print(square_area)
