if __name__ == "__main__":
    n, m, k = map(int, input().split())

    chess_board = []

    for _ in range(n):
        chess_board.append(list(input()))

    rule1_repaint_black_chess_board = [[-1 for _ in range(m)] for _ in range(n)]
    rule1_repaint_white_chess_board = [[-1 for _ in range(m)] for _ in range(n)]
    rule2_repaint_black_chess_board = [[-1 for _ in range(m)] for _ in range(n)]
    rule2_repaint_white_chess_board = [[-1 for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if x % 2 == 0:
                if chess_board[y][x] == 'B':
                    rule1_repaint_black_chess_board[y][x] = 1
                    rule1_repaint_white_chess_board[y][x] = 0
                    rule2_repaint_black_chess_board[y][x] = 0
                    rule2_repaint_white_chess_board[y][x] = 1
                else:
                    rule1_repaint_black_chess_board[y][x] = 0
                    rule1_repaint_white_chess_board[y][x] = 1
                    rule2_repaint_black_chess_board[y][x] = 1
                    rule2_repaint_white_chess_board[y][x] = 0
            else:
                if chess_board[y][x] == 'B':
                    rule1_repaint_black_chess_board[y][x] = 0
                    rule1_repaint_white_chess_board[y][x] = 1
                    rule2_repaint_black_chess_board[y][x] = 1
                    rule2_repaint_white_chess_board[y][x] = 0
                else:
                    rule1_repaint_black_chess_board[y][x] = 1
                    rule1_repaint_white_chess_board[y][x] = 0
                    rule2_repaint_black_chess_board[y][x] = 0
                    rule2_repaint_white_chess_board[y][x] = 1

    rule1_repaint_prefix_sum = []
    rule2_repaint_prefix_sum = []