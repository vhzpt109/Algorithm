from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        idx0 = 0
        idx2 = len(nums) - 1
        i = 0

        while i <= idx2:
            if nums[i] == 0:
                nums[i], nums[idx0] = nums[idx0], nums[i]
                idx0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[idx2] = nums[idx2], nums[i]
                idx2 -= 1
            else:
                i += 1