import sys


def available_number_check_row(board, y):
    global available_number
    no_number_list = []
    for i in range(9):
        no_number_list.append(board[y][i])

    no_number_set = set(no_number_list)
    no_number_set.discard(0)
    no_number_set = set(available_number) - set(no_number_list)

    return no_number_set


def available_number_check_col(board, x):
    global available_number
    no_number_list = []
    for i in range(9):
        no_number_list.append(board[i][x])

    no_number_set = set(no_number_list)
    no_number_set.discard(0)
    no_number_set = set(available_number) - set(no_number_list)

    return no_number_set


def available_number_check_rect(board, x, y):
    global available_number
    no_number_list = []
    position_x = x // 3 * 3
    position_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            no_number_list.append(board[position_y + i][position_x + j])

    no_number_set = set(no_number_list)
    no_number_set.discard(0)
    no_number_set = set(available_number) - set(no_number_list)

    return no_number_set


def sdoku_backtracking(board, zero_coordinate, depth):
    if depth == len(zero_coordinate):
        for row_board in board:
            print(*row_board)
        exit(0)

    for coordinate in zero_coordinate[depth:]:
        a_b_check_row_set = available_number_check_row(board, coordinate[0])
        a_b_check_col_set = available_number_check_col(board, coordinate[1])
        a_b_check_rect_set = available_number_check_rect(board, coordinate[1], coordinate[0])

        and_check_list = list(a_b_check_row_set & a_b_check_col_set & a_b_check_rect_set)
        if len(and_check_list) >= 1:
            for number in and_check_list:
                board[coordinate[0]][coordinate[1]] = number
                sdoku_backtracking(board, zero_coordinate, depth + 1)
                board[coordinate[0]][coordinate[1]] = 0
        return


if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    zero_coordinate = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]
    available_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sdoku_backtracking(board, zero_coordinate, 0)