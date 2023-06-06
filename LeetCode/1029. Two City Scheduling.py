from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda value:value[1] - value[0], reverse=True)

        minimum_total_cost = 0
        for i in range(len(costs) // 2):
            minimum_total_cost += costs[i][0]
        for i in range(len(costs) // 2, len(costs)):
            minimum_total_cost += costs[i][1]

        return minimum_total_cost


if __name__ == "__main__":
    obj = Solution()
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(obj.twoCitySchedCost(costs))