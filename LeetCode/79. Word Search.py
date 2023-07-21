from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.word = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == self.word[0]:
                    self.backtracking(x, y, 0)

    def backtracking(self, x, y, word_idx):
        pass


if __name__ == "__main__":
    obj = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(obj.exist(board, word))