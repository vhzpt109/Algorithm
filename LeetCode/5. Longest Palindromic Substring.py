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
                start = s[row]
                end = s[col]
                prev_count = dp[row + 1][col - 1]
                if start == end and prev_count != 0:
                    dp[row][col] = prev_count + 2
                row += 1
                col += 1

        max_length = 0
        start = 0
        end = 0
        for row in range(str_length):
            for col in range(str_length):
                current_length = dp[row][col]
                if max_length < current_length:
                    max_length = current_length
                    start = row
                    end = col

        sub_str = s[start:end + 1]

        return sub_str


if __name__ == "__main__":
    obj = Solution()
    # s = "aabb"
    s = "baabc"
    print(obj.longestPalindrome(s))