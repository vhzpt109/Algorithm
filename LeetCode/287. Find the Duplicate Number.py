from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])

            nums[nums[i]] = -nums[nums[i]]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDuplicate([1, 2, 2]))
