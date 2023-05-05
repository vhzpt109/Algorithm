from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1

        return -1