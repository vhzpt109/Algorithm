class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isValid(s[left]):
                left += 1
                continue

            if not self.isValid(s[right]):
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def isValid(self, c):
        if c.isdigit():
            return True
        if 97 <= ord(c) <= 122:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    print(obj.isPalindrome("race a car"))
    print(obj.isPalindrome("OP"))