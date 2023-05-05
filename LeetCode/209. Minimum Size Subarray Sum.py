import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cml_sums = [0]
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            cml_sums.append(tmp_sum)

        minSubLen = sys.maxsize
        left = 0
        right = 1

        while left <= right <= len(nums) and left <= len(nums):
            if cml_sums[right] - cml_sums[left] >= target:
                minSubLen = min(minSubLen, right - left)
                left += 1
                right += 1
            elif cml_sums[right] - cml_sums[left] < target:
                right += 1

        if minSubLen == sys.maxsize:
            return -1
        else:
            return minSubLen