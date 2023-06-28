# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return self.removeElementIterator(head, val)

    def removeElementIterator(self, node: ListNode, target_val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = node

        current_node = node
        previous_node = dummy_head
        while current_node:
            if current_node.val == target_val:
                previous_node.next = current_node.next
                current_node = current_node.next
            else:
                current_node = current_node.next
                previous_node = previous_node.next
        return dummy_head.next


if __name__ == "__main__":
    obj = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(6)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(4)
    node.next.next.next.next.next = ListNode(5)
    node.next.next.next.next.next.next = ListNode(6)

    obj.removeElements(node, 6)


