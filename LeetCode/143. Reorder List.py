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
        pass

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_step_node = head
        two_step_node = head

        while two_step_node:
            if two_step_node.next:
                one_step_node = one_step_node.next
                two_step_node = two_step_node.next.next
            else:
                break

        return one_step_node

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