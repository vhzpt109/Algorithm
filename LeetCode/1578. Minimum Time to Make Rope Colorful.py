from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost_sum = 0
        current_color = colors[0]
        max_cost = neededTime[0]
        for i in range(1, len(colors)):
            if current_color != colors[i]:
                current_color = colors[i]
                max_cost = neededTime[i]

            elif max_cost < neededTime[i]:
                cost_sum += max_cost
                max_cost = neededTime[i]
            else:
                cost_sum += neededTime[i]

        return cost_sum


if __name__ == "__main__":
    obj = Solution()
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    print(obj.minCost(colors, neededTime))