if __name__ == "__main__":
    n, m = map(int, input().split())

    list_nm = []

    for _ in range(n):
        list_nm.append(list(input()))

    min_repaint_cnt = 64
    for row in range(n - 7):
        for col in range(m - 7):
            chess_board = []
            for y in range(row, row + 8):
                chess_board.append(list_nm[y][col:col + 8])

            chess_line_rule1 = list("WBWBWBWB")
            chess_line_rule2 = list("BWBWBWBW")
            sum_repaint_case1 = 0
            sum_repaint_case2 = 0
            for i in range(len(chess_board)):
                if i % 2 == 0:
                    sum_repaint_case1 += 8 - sum([have_chess_board_line == chess_line for have_chess_board_line, chess_line in
                                          zip(chess_board[i], chess_line_rule1)])
                    sum_repaint_case2 += 8 - sum([have_chess_board_line == chess_line for have_chess_board_line, chess_line in
                                          zip(chess_board[i], chess_line_rule2)])
                else:
                    sum_repaint_case1 += 8 - sum([have_chess_board_line == chess_line for have_chess_board_line, chess_line in
                                          zip(chess_board[i], chess_line_rule2)])
                    sum_repaint_case2 += 8 - sum([have_chess_board_line == chess_line for have_chess_board_line, chess_line in
                                          zip(chess_board[i], chess_line_rule1)])

            if min(sum_repaint_case1, sum_repaint_case2) < min_repaint_cnt:
                min_repaint_cnt = min(sum_repaint_case1, sum_repaint_case2)

    print(min_repaint_cnt)