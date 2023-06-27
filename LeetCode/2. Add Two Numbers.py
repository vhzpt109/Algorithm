# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        round = 0

        while l1 or l2 or round != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            sum = num1 + num2 + round
            val = sum % 10
            round = sum // 10

            newListNode = ListNode(val)
            tail.next = newListNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = head.next
        head.next = None

        return result


if __name__ == "__main__":
    obj = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(4)
    l2.next.next = ListNode(4)

    obj.addTwoNumbers(l1, l2)
