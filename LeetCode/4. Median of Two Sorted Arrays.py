from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        p1, p2 = 0, 0
        result = []
        for i in range(length):
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    result.append(nums1[p1])
                    p1 += 1
                else:
                    result.append(nums2[p2])
                    p2 += 1
            elif p1 < len(nums1):
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        if len(result) % 2 == 1:
            return result[len(result) // 2]
        else:
            return (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMedianSortedArrays([1, 3], [2]))
