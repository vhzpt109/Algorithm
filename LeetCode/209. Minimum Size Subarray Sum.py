from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_end = 0
        min_len = len(nums)
        w_sum = nums[0]

        if sum(nums) < target: return 0
        if nums[-1] >= target: return 1

        for i in range(len(nums) - 1):
            if i > 0:
                w_sum -= nums[i - 1]
            if i > min_end:
                min_end = i

            # find the min subarray
            while min_end < len(nums):
                if w_sum < target:
                    min_end += 1
                    if min_end == len(nums): break
                    w_sum += nums[min_end]
                if w_sum >= target:
                    min_len = min(min_len, min_end - i + 1)
                    break
        return min_len