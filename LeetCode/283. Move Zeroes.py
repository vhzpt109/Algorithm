from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeroIndex], nums[i] = nums[i], nums[zeroIndex]
                zeroIndex += 1