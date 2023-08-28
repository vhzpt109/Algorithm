from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert([1, 3, 5, 6], 5))
