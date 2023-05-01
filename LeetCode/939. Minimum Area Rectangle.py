import sys
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hash_map = {}
        for point in points:
            if point[0] not in hash_map:
                hash_map[point[0]] = set()
            hash_map[point[0]].add(point[1])

        min_area = sys.maxsize
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                point1 = points[i]
                point2 = points[j]

                if point1[0] == point2[0] or point1[0] == point2[1]:
                    continue
                if point1[1] == point2[0] or point1[1] == point2[1]:
                    continue
                if not (point1[0] in hash_map and point2[1] in hash_map[point1[0]]):
                    continue
                if not (point2[0] in hash_map and point1[1] in hash_map[point2[0]]):
                    continue

                rectangle_area = abs((point1[0] - point2[0]) * (point1[1] - point2[1]))

                min_area = min(min_area, rectangle_area)

        if min_area == sys.maxsize:
            return 0
        else:
            return min_area