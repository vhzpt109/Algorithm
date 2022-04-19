if __name__ == "__main__":
    n, m = map(int, input().split())

    list_nm = []

    for _ in range(n):
        list_nm.append(list(input()))

    cnt = 0
    for i in range(n - 7):
        for j in range(m - 7):
            chess_board = list_nm[0][0:8]

            repaint_black = 0
            repaint_white = 0
            for y in range(8):
                for x in range(8):
                    if chess_board[x][y] == 'W':
                        cnt += 1