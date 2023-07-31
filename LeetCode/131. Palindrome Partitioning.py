from typing import List


class Solution:
    def __init__(self):
        self.s = None
        self.results = []

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        for i in range(len(s)):
            self.backtracking(0, i, [])

        return self.results

    def backtracking(self, begin, last, letters):
        if not self.isPalindrome(self.s[begin:last + 1]):
            return

        letters.append(self.s[begin:last + 1])

        if len(self.s) == last + 1:
            self.results.append(letters.copy())
            letters.pop()
            return

        for i in range(last + 1, len(self.s)):
            self.backtracking(last + 1, i, letters)

        letters.pop()
        return

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    obj = Solution()
    s = "aabb"
    print(obj.partition(s))