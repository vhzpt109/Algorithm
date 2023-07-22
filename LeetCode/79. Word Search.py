from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.word = None
        self.visited = None

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.backtracking(x, y, 0):
                    return True
        return False

    def backtracking(self, x, y, word_idx):
        if self.board[y][x] == self.word[word_idx]:
            if word_idx == len(self.word) - 1:
                return True
        else:
            return False

        self.visited[y][x] = True

        for i in range(4):
            xx = x + self.dx[i]
            yy = y + self.dy[i]
            w = word_idx + 1

            if xx < 0 or xx >= len(self.board[0]) or yy < 0 or yy >= len(self.board):
                continue
            if self.visited[yy][xx]:
                continue
            if self.word[w] != self.board[yy][xx]:
                continue

            if self.backtracking(xx, yy, w):
                return True

        self.visited[y][x] = False
        return False


if __name__ == "__main__":
    obj = Solution()
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    # word = "SEE"
    # board = [["a"]]
    # word = "b"
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    print(obj.exist(board, word))