from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True

        target_col = left

        left = 0
        right = len(matrix[0]) - 1
        while left < right:
            mid = (left + right) // 2

            if matrix[target_col][mid] > target:
                right = mid - 1
            elif matrix[target_col][mid] < target:
                left = mid + 1
            else:
                return True

        if matrix[target_col][left] == target:
            return True

        return False


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    # matrix = [[1]]
    # target = 3
    # target = 28
    target = 11
    print(obj.searchMatrix(matrix, target))
