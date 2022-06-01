def is_available_location(board, x, y, n):
    for i in range(len(board)):
        if board[i][x] or board[y][i]:
            return False

    lu = [x, y]
    ru = [x, y]
    ld = [x, y]
    rd = [x, y]
    for _ in range(n - 1):
        if 0 < lu[0] and 0 < lu[1]:
            lu[0] -= 1
            lu[1] -= 1
            if board[lu[1]][lu[0]]:
                return False
        if ru[0] < n - 1 and 0 < ru[1]:
            ru[0] += 1
            ru[1] -= 1
            if board[ru[1]][ru[0]]:
                return False
        if 0 < ld[0] and ld[1] < n - 1:
            ld[0] -= 1
            ld[1] += 1
            if board[ld[1]][ld[0]]:
                return False
        if rd[0] < n - 1 and rd[1] < n - 1:
            rd[0] += 1
            rd[1] += 1
            if board[rd[1]][rd[0]]:
                return False
    return True


def n_queen(board, y):
    global count
    for x in range(len(board[y])):
        if is_available_location(board, x, y, len(board)):
            if y == len(board) - 1:
                count += 1
                return
            board[y][x] = True
            n_queen(board, y + 1)
            board[y][x] = False


if __name__ == "__main__":
    n = int(input())

    board = [[False] * n for _ in range(n)]
    count = 0

    n_queen(board, 0)
    print(count)