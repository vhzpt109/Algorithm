class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(0, len(s) - 1, s, False)

    def isPalindrome(self, left, right, s, isDeleted):
        while left < right:
            if s[left] != s[right]:
                if isDeleted is False:
                    if self.isPalindrome(left + 1, right, s, True) or self.isPalindrome(left, right - 1, s, True):
                        return True
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.validPalindrome("aba"))
    print(obj.validPalindrome("abca"))
    print(obj.validPalindrome("abc"))