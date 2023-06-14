from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        idx, g = 0, 0
        for i in range(len(gas)):
            if g + gas[i] < cost[i]:
                idx = i + 1
                g = 0
            else:
                g += gas[i] - cost[i]
        return idx


if __name__ == "__main__":
    obj = Solution()
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    # gas = [3, 3, 4]
    # cost = [3, 4, 4]
    # gas = [5, 1, 2, 3, 4]
    # cost = [4, 4, 1, 5, 1]
    gas = [5, 8, 2, 8]
    cost = [6, 5, 6, 6]
    print(obj.canCompleteCircuit(gas, cost))
