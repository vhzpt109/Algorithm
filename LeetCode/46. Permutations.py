from typing import List


class Solution:
    def __init__(self):
        self.nums = None
        self.result = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.backtracking([], set())
        return self.result

    def backtracking(self, current_list, used_num):
        if len(current_list) == len(self.nums):
            self.result.append(current_list.copy())
            return

        for num in self.nums:
            if num in used_num:
                continue

            current_list.append(num)
            used_num.add(num)
            self.backtracking(current_list, used_num)
            used_num.remove(num)
            current_list.pop()


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3]
    print(obj.permute(nums))