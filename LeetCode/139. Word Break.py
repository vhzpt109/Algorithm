from typing import List


class Solution:
    def __init__(self):
        self.s = None
        self.word_table = None

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.word_table = dict.fromkeys(wordDict)

        for i in range(len(s)):
            if self.backtracking(0, i):
                return True
        return False

    def backtracking(self, begin, last):
        if not self.word_table.get(self.s[begin:last + 1]):
            return False
        if len(self.s) == last + 1:
            return True

        for i in range(last + 1, len(self.s)):
            if self.backtracking(last + 1, i):
                return True

        return False


if __name__ == "__main__":
    obj = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(obj.wordBreak(s, wordDict))