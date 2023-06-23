class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = list(str(x)).copy()
        reverse_string_x = list(str(x)).reverse
        return string_x == string_x.reverse()


if __name__ == "__main__":
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))