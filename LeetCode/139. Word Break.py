from typing import List


class Solution:
    def __init__(self):
        self.s = None
        self.word_table = None

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.word_table = dict.fromkeys(wordDict)

        if self.s in self.word_table:
            return True

        for i in range(len(s)):
            if self.backtracking(0, i) and self.backtracking(i + 1, len(self.s)):
                return True
        return False

    def backtracking(self, begin, last):
        if self.s[begin:last + 1] in self.word_table:
            return True

        for i in range(begin, last):
            if self.backtracking(begin, i) and self.backtracking(i + 1, last):
                return True

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(obj.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(obj.wordBreak(s="a", wordDict=["a"]))
    print(obj.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aa"]))