class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] >= '1' else 0

        for i in range(2, len(s) + 1):
            if s[i - 1] >= '1':
                dp[i] += dp[i - 1]
            if int(s[i - 2: i]) >= 10 and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


if __name__ == "__main__":
    obj = Solution()
    s = "123"
    print(obj.numDecodings(s))