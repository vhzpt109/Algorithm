from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        self.backtracking(board, 0)

        return self.result

    def is_available_location(self, board, x, y, n):
        for i_y in reversed(range(y)):
            if board[i_y][x] == 'Q':
                return False

        lu = [x, y]
        ru = [x, y]
        for _ in range(y):
            if 0 < lu[0] and 0 < lu[1]:
                lu[0] -= 1
                lu[1] -= 1
                if board[lu[1]][lu[0]] == 'Q':
                    return False
            if ru[0] < n - 1 and 0 < ru[1]:
                ru[0] += 1
                ru[1] -= 1
                if board[ru[1]][ru[0]] == 'Q':
                    return False
        return True

    def backtracking(self, board, y):
        for x in range(len(board[y])):
            if self.is_available_location(board, x, y, len(board)):
                board[y][x] = 'Q'
                if y == len(board) - 1:
                    self.result.append([''.join(row) for row in board])
                    board[y][x] = '.'
                    return
                else:
                    self.backtracking(board, y + 1)
                    board[y][x] = '.'


if __name__ == "__main__":
    obj = Solution()
    n = 4
    print(obj.solveNQueens(n))