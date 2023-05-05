from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        leftSum = 0
        rightSum = _sum

        pastPivotNum = 0
        for i in range(len(nums)):
            pivotNum = nums[i]
            leftSum += pastPivotNum
            rightSum -= pivotNum

            if leftSum == rightSum:
                return i
            pastPivotNum = pivotNum

        return -1