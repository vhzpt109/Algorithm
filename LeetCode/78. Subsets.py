from typing import List


class Solution:
    def __init__(self):
        self.sets = []
        self.numbers = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.numbers = nums
        self.backtracking([], 0, len(nums))

        return self.sets

    def backtracking(self, nums, depth, target_depth):
        if depth == target_depth:
            self.sets.append(nums.copy())
            return

        self.backtracking(nums, depth + 1, target_depth)

        nums.append(self.numbers[depth])
        self.backtracking(nums, depth + 1, target_depth)
        nums.pop()


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3]
    print(obj.subsets(nums))