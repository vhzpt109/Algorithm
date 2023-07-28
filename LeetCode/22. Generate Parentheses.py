from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        open_count = n
        close_count = n

        self.backtracking(open_count, close_count, '')

        return self.result

    def backtracking(self, open_count: int, close_count: int, letters: str):
        if open_count == 0 and close_count == 0:
            self.result.append(letters)
            return

        # open whenever we have open
        if 0 < open_count:
            self.backtracking(open_count - 1, close_count, letters + '(')

        # close when we cannot open
        if open_count < close_count:
            self.backtracking(open_count, close_count - 1, letters + ')')


if __name__ == "__main__":
    obj = Solution()
    n = 4
    print(obj.generateParenthesis(n))