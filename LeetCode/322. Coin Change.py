from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        idx = [i for i in range(1, amount + 1) if ]

        for coin in coins:
            dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0 or dp[i - coin] == -1:
                    continue
                dp[i] = min(dp[i], dp[i - coin])
            dp[i] += 1

        return dp[amount]


if __name__ == "__main__":
    obj = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(obj.coinChange(coins, amount))
