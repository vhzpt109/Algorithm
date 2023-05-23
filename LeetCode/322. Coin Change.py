from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        coins = [coin for coin in coins if coin <= amount]

        for i in range(1, amount + 1):
            min_cost = 2**32 - 1
            for coin in coins:
                if i < coin:
                    continue
                min_cost = min(min_cost, dp[i - coin] + 1)
            if min_cost != 0:
                dp[i] = min_cost

        if dp[amount] == 2**32 - 1:
            return -1
        return dp[amount]


if __name__ == "__main__":
    obj = Solution()
    # coins = [1, 2, 5]
    # coins = [2]
    # amount = 11
    coins = [1]
    amount = 1
    print(obj.coinChange(coins, amount))
