# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        node1 = dummy_node
        for _ in range(n + 1):
            node1 = node1.next

        node2 = dummy_node
        while node1:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next

        return dummy_node.next


if __name__ == "__main__":
    obj = Solution()

    Node = ListNode(1)
    Node.next = ListNode(2)
    Node.next.next = ListNode(3)
    Node.next.next.next = ListNode(4)
    Node.next.next.next.next = ListNode(5)

    obj.removeNthFromEnd(Node, 3)
