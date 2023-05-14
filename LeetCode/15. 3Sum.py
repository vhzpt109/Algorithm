from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        target = 0
        for idx, num in enumerate(nums):
            sub_target = target - num

            left = idx + 1
            right = len(nums) - 1
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum == sub_target:
                    if [num, nums[left], nums[right]] not in result:
                        result.append([num, nums[left], nums[right]])
                    left += 1
                elif _sum > sub_target:
                    right -= 1
                elif _sum < sub_target:
                    left += 1
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
    print(obj.threeSum([0, 0, 0, 0]))
