from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n + 1)]

        dp[1] = cost[0]

        for i in range(2, n + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n])


if __name__ == "__main__":
    obj = Solution()
    # cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(obj.minCostClimbingStairs(cost))
