from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval:interval[1])

        last_end = -999999
        count = 1
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start < last_end:
                continue

            if last_end <= end:
                count += 1
                last_end = end

        return len(intervals) - count



if __name__ == "__main__":
    obj = Solution()
    # intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    # intervals = [[1, 2], [1, 2], [1, 2]]
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    print(obj.eraseOverlapIntervals(intervals))
