# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        addedListNode = self.addTwoNumbersEntity(l1, l2)

        reversedAddedListNode = self.reverseList(addedListNode)

        return reversedAddedListNode

    def addTwoNumbersEntity(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        round = 0

        while l1 or l2 or round != 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + round
            val = sum % 10
            round = sum // 10

            newListNode = ListNode(val)
            tail.next = newListNode
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = head.next

        return result

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

    l1 = ListNode(4)
    l1.next = ListNode(8)

    l2 = ListNode(7)
    l2.next = ListNode(9)

    obj.addTwoNumbers(l1, l2)
