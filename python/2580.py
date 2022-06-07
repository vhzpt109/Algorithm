import sys


def available_number_check(board, x, y):
    available_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if board[i][x] in available_number_list:
            available_number_list.remove(board[i][x])
        if board[y][i] in available_number_list:
            available_number_list.remove(board[y][i])

    position_x = x // 3 * 3
    position_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[position_y + i][position_x + j] in available_number_list:
                available_number_list.remove(board[position_y + i][position_x + j])

    return available_number_list


def sdoku_backtracking(board, zero_coordinate, depth):
    if depth == len(zero_coordinate):
        for row_board in board:
            print(*row_board)
        exit(0)

    coordinate = zero_coordinate[depth]

    and_check_list = available_number_check(board, coordinate[1], coordinate[0])
    if len(and_check_list) >= 1:
        for number in and_check_list:
            board[coordinate[0]][coordinate[1]] = number
            sdoku_backtracking(board, zero_coordinate, depth + 1)
            board[coordinate[0]][coordinate[1]] = 0


if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    zero_coordinate = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]

    sdoku_backtracking(board, zero_coordinate, 0)