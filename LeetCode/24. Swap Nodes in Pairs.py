from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        previous = None
        current = head
        result = head.next
        while current and current.next:
            adj = current.next
            if previous: previous.next = adj

            current.next, adj.next = adj.next, current
            previous, current = current, current.next

        return result or head


if __name__ == "__main__":
    obj = Solution()

    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next = ListNode(4)

    print(obj.swapPairs(head))
