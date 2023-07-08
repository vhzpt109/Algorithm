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
        if not head:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        previous, current = None, slow.next
        while current:
            save = current.next
            current.next = previous
            previous = current
            current = save
        slow.next = None

        head2 = previous
        while head2:
            save1 = head.next
            head.next = head2
            head = head2
            head2 = save1