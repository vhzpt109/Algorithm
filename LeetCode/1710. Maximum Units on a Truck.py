from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda value: value[1], reverse=True)

        total_unit = 0
        left_boxes = truckSize
        for box_count, unit in boxTypes:
            if box_count <= left_boxes:
                total_unit += (box_count * unit)
                left_boxes -= box_count
            else:
                total_unit += (unit * left_boxes)
                left_boxes -= left_boxes

            if left_boxes == 0:
                return total_unit

        return total_unit


if __name__ == "__main__":
    obj = Solution()
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    print(obj.maximumUnits(boxTypes, truckSize))