class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = list(str(x))
        return string_x == string_x[::-1]


if __name__ == "__main__":
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))