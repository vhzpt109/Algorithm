class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        invalid_coordinate = [(x, y) for x in range(9) for y in range(9) if board[x][y] == '.']

        self.sudoku_backtracking(board, invalid_coordinate, 0)

    def sudoku_backtracking(self, board, invalid_coordinate, depth):
        if depth == len(invalid_coordinate):
            return True

        coordinate = invalid_coordinate[depth]

        and_check_list = self.available_number_check(board, coordinate[1], coordinate[0])
        if len(and_check_list) >= 1:
            for number in and_check_list:
                board[coordinate[0]][coordinate[1]] = number
                if self.sudoku_backtracking(board, invalid_coordinate, depth + 1):
                    return True
                board[coordinate[0]][coordinate[1]] = '.'

        return False

    def available_number_check(self, board, x, y):
        available_number_list = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
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


if __name__ == "__main__":
    obj = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    obj.solveSudoku(board)
    print(board)
