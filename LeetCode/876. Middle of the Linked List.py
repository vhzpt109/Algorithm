# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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


if __name__ == "__main__":
    obj = Solution()

    Node = ListNode(1)
    Node.next = ListNode(2)
    Node.next.next = ListNode(3)
    Node.next.next.next = ListNode(4)
    Node.next.next.next.next = ListNode(5)

    obj.middleNode(Node)
