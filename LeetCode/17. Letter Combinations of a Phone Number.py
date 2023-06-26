from typing import List


class Solution:
    def __init__(self):
        self.hash = {'1': [],
                     '2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}

        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        target_depth = len(digits)
        self.backtracking(digits, "", 0, target_depth)

        return self.result

    def backtracking(self, digits: str, result: str, depth: int, target_depth: int):
        if depth == target_depth:
            self.result.append(result[:])
            return

        for digit in self.hash[digits[depth]]:
            self.backtracking(digits, result[:] + digit, depth + 1, target_depth)


if __name__ == "__main__":
    obj = Solution()
    # digits = "23"
    # digits = ""
    digits = "2"
    print(obj.letterCombinations(digits))
