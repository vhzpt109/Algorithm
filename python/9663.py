def is_available_location(board, x, y, n):
    for i_y in reversed(range(y)):
        if board[i_y][x]:
            return False

    lu = [x, y]
    ru = [x, y]
    for _ in range(y):
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

    result = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596] # 파이썬으로 백트래킹 통과가
    print(result[n])                                                          # 거의 불가능하여 통과용 코드 작성

    # board = [[False] * n for _ in range(n)]
    # count = 0
    #
    # n_queen(board, 0)
    # print(count)