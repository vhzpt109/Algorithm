from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        clone_graph = {node.val: Node(node.val, [])}

        while queue:
            current_node = queue.popleft()
            current_clone = clone_graph[current_node.val]

            for connected_node in current_node.neighbors:
                if connected_node.val not in clone_graph:
                    clone_graph[connected_node.val] = Node(connected_node.val, [])
                    queue.append(connected_node)

                current_clone.neighbors.append(clone_graph[connected_node.val])

        return clone_graph[node.val]