# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head  # slow, fast는 head가 가르키는 곳을 참조.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            prev, curr = None, slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next




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