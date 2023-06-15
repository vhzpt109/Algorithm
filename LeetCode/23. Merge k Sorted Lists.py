import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = []
        heap = []

        for nth_list in lists:
            if len(nth_list) == 0:
                continue

            # heap push ( num, idx, list)
            heapq.heappush(heap, (nth_list[0], 0, nth_list))

        while heap:
            num, idx, nth_list = heapq.heappop(heap)
            merged_list.append(num)
            idx += 1
            if idx < len(nth_list):
                heapq.heappush(heap, (nth_list[idx], idx, nth_list))

        return merged_list


if __name__ == "__main__":
    obj = Solution()
    lists = [[1, 5, 7, 9], [2, 6, 8], [3, 4, 10]]
    print(obj.mergeKLists(lists))