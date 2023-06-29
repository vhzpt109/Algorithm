from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head

        while list1 or list2:
            num1 = list1.val if list1 else 101
            num2 = list2.val if list2 else 101

            if num1 < num2:
                tail.next = list1
                tail = tail.next
                list1 = list1.next if list1 else None

            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next if list2 else None

        result = head.next

        return result


if __name__ == "__main__":
    obj = Solution()

    l1 = ListNode(4)
    l1.next = ListNode(8)

    l2 = ListNode(7)
    l2.next = ListNode(9)

    node = obj.mergeTwoLists(l1, l2)
    while node.next:
        print(node.val, end=" ")
        node = node.next
    print(node.val)