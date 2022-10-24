if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))

    max_value = -1
    max_col = -1
    max_row = -1
    for y in range(9):
        for x in range(9):
            if board[y][x] > max_value:
                max_value = board[y][x]
                max_col = x + 1
                max_row = y + 1

    print(max_value)
    print(max_row, max_col)