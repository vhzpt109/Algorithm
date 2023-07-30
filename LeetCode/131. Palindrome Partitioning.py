from typing import List


class Solution:
    def __init__(self):
        self.results = []

    def partition(self, s: str) -> List[List[str]]:
        for i in range(len(s)):
            self.backtracking(s[i:i + 1], [])
            self.backtracking(s[i + 1:], [])

        return self.results

    def backtracking(self, s, result):
        if self.isPalindrome(s):
            result.append(s.copy())
        else:
            return

        for i in range(len(s)):
            self.backtracking(s[i: i + 1], result)
            self.backtracking(s[i + 1:], result)

    def isPalindrome(self, s):
        return s == s[-1::]


if __name__ == "__mian__":
    obj = Solution()
    s = "aabb"
    print(obj.partition(s))