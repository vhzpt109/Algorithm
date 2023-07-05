# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower_node = ListNode(-1)
        upper_node = ListNode(-1)
        dummy_node = lower_node

        current_node = head
        while current_node:
            if current_node.val < x:
                lower_node.next = current_node
                lower_node = lower_node.next
            else:
                upper_node.next = current_node
                upper_node = upper_node.next
            current_node = current_node.next
        lower_node.next = upper_node

        return dummy_node.next


if __name__ == "__main__":
    obj = Solution()

    node = ListNode(1)
    node.next = ListNode(4)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(2)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(2)

    result_node = obj.partition(node, 3)
    while result_node:
        print(result_node.val, end=" ")
        result_node = result_node.next
