from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, num in enumerate(nums):
            match_num = target - num
            match_idx = hash_table.get(match_num)

            if match_idx is not None:
                return [idx, match_idx]

            hash_table[num] = idx