from typing import List


class Solution:
    def __init__(self):
        self.nums = None
        self.target = None
        self.result = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        self.target = target
        self.result = []
        self.backtracking(0, [], 0)

        return self.result

    def backtracking(self, previous_idx, current_list, list_sum):
        if list_sum == self.target:
            self.result.append(current_list.copy())
            return
        elif list_sum > self.target:
            return

        for idx in range(previous_idx, len(self.nums)):
            current_list.append(self.nums[idx])
            self.backtracking(idx, current_list, list_sum + self.nums[idx])
            current_list.pop()


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 3, 6, 7]
    target = 7
    print(obj.combinationSum(nums, target))