from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        gas.extend(gas[:])
        cost.extend(cost[:])

        idx = 0
        while idx < length:
            g = gas[idx]
            pass_flag = True
            for i in range(1, length + 1):
                g -= cost[idx + i]
                if g < 0:
                    idx = idx + i
                    pass_flag = False
                    break
                g += gas[idx + i]
            if pass_flag:
                return idx + 1
            idx += 1

        return -1


if __name__ == "__main__":
    obj = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    # gas = [3, 3, 4]
    # cost = [3, 4, 4]
    print(obj.canCompleteCircuit(gas, cost))