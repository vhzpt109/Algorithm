if __name__ == "__main__":
    n_melon = int(input())

    direction_length_list = []
    max_width = 0
    max_height = 0
    for _ in range(6):
        direction, length = map(int, input().split())
        direction_length_list.append((direction, length))
        if direction == 1 or direction == 2:
            if max_width < length:
                max_width = length
        elif direction == 3 or direction == 4:
            if max_height < length:
                max_height = length

    square_area = max_width * max_height

    excluded_area = 0
    for i in range(len(direction_length_list) - 1):
        excluded_area += direction_length_list[i][1] * direction_length_list[i + 1][1]
    excluded_area += direction_length_list[-1][1] * direction_length_list[0][1]

    available_area = square_area - (square_area * 3 - excluded_area)
    print(available_area * n_melon)