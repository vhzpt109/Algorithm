
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head is None:
            return head

        node_hash_map = {}

        dummy_head = Node(-1)
        deepcopy_node = dummy_head

        current_node = head
        while current_node:
            val = current_node.val
            temp_node = Node(x=val)

            deepcopy_node.next = temp_node
            node_hash_map[current_node] = temp_node

            deepcopy_node = deepcopy_node.next
            current_node = current_node.next

        current_node = head
        while current_node:
            temp_node = node_hash_map[current_node]
            current_node_random = current_node.random
            if current_node_random is not None:
                random_node = node_hash_map[current_node_random]
                temp_node.random = random_node
            else:
                temp_node.random = None
            current_node = current_node.next

        return dummy_head.next
