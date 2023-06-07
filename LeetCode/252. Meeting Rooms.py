import heapq
from typing import List


class Solution():
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda interval: interval[0])

        lasts = []  # min heap
        heapq.heappush(lasts, intervals[0][1])

        room_count = 1

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            last_end = lasts[0]

            if last_end <= start:
                heapq.heappop(lasts)
                heapq.heappush(lasts, end)
            else:
                heapq.heappush(lasts, end)
                room_count += 1

        return room_count


if __name__ == "__main__":
    obj = Solution()
    intervals = [[9, 11], [9, 12], [10, 14], [12, 16], [13, 16], [15, 17]]
    print(obj.minMeetingRooms(intervals))