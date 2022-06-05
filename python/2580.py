import sys

def check_row(board, y):
    count = 0
    row_sum = 0
    zero_idx = []

    for i in range(9):
        if board[y][i] == 0:
            count += 1
            zero_idx = (y, i)
        else:
            row_sum += board[y][i]

    if count == 1:
        board[zero_idx[0]][zero_idx[1]] = 45 - row_sum

def check_col(board, x):
    count = 0
    col_sum = 0
    zero_idx = []

    for i in range(9):
        if board[i][x] == 0:
            count += 1
            zero_idx = (i, x)
        else:
            col_sum += board[i][x]

    if count == 1:
        board[zero_idx[0]][zero_idx[1]] = 45 - col_sum


def check_rect(board, x, y):
    count = 0
    rect_sum = 0
    zero_idx = []

    position_x = x // 3 * 3
    position_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[position_y + i][position_x + j] == 0:
                count += 1
                zero_idx = (y, x)
            else:
                rect_sum += board[position_y + i][position_x + j]

    if count == 1:
        board[zero_idx[0]][zero_idx[1]] = 45 - rect_sum


if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    while min(map(min, board)) == 0:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    check_col(board, j)
                    check_row(board, i)
                    check_rect(board, j, i)

    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("")