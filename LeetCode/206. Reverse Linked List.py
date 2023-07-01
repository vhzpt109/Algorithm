# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        elif head.next is None:
            return head

        current_node = head.next
        previous_node = head
        head.next = None

        while current_node:
            tmp_next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = tmp_next_node

        return previous_node


if __name__ == "__main__":
    obj = Solution()

    Node = ListNode(1)
    Node.next = ListNode(2)
    Node.next.next = ListNode(3)
    Node.next.next.next = ListNode(4)
    Node.next.next.next.next = ListNode(5)

    obj.reverseList(Node)