# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one_step_node = head
        two_step_node = head

        while two_step_node:
            if two_step_node.next:
                one_step_node = one_step_node.next
                two_step_node = two_step_node.next.next
            else:
                break

            if one_step_node == two_step_node:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    Node = ListNode(1)
    Node.next = ListNode(2)
    Node.next.next = ListNode(3)
    Node.next.next.next = ListNode(4)
    Node.next.next.next.next = ListNode(5)

    obj.hasCycle(Node)
