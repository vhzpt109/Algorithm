from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            pivot = (left + right) // 2
            num = nums[pivot]
            nextNum = nums[pivot + 1]

            if num < nextNum:
                left = pivot + 1
            elif num > nextNum:
                right = pivot

        return left