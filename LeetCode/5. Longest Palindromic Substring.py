class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        dp = [[0] * str_length for _ in range(str_length)]

        for i in range(str_length):
            dp[i][i] = 1

        for i in range(str_length - 1):
            start = s[i]
            end = s[i + 1]
            if start == end:
                dp[i][i + 1] = dp[i][i] + 1

        for i in range(1, str_length):
            row = 0
            col = i
            while col < str_length:
                


if __name__ == "__main__":
    obj = Solution()
    s = "aabb"
    print(obj.longestPalindrome(s))