# Definition for a Node.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.node_hash_map = {}

    def get(self, key: int) -> int:
        node = self.node_hash_map.get(key)
        if node:
            self.removeFromLinkedList(node)
            self.addBack(node)
            val = node.value
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        put_node = self.node_hash_map.get(key)
        if put_node is not None:
            put_node.value = value

            self.removeFromLinkedList(put_node)
            self.addBack(put_node)
        else:
            put_node = Node(key, value)
            self.addBack(put_node)
            self.node_hash_map[key] = put_node

        if len(self.node_hash_map) > self.capacity:
            key = self.head.next.key
            self.removeFromLinkedList(self.head.next)
            self.node_hash_map.pop(key)

    def removeFromLinkedList(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def addBack(self, node):
        tail_prev_node = self.tail.prev

        tail_prev_node.next = node
        node.prev = tail_prev_node

        node.next = self.tail
        self.tail.prev = node


if __name__ == "__main__":
    lru_cache = LRUCache(4)
    lru_cache.put(1, 10)
    lru_cache.put(2, 20)
    lru_cache.put(3, 30)
    lru_cache.put(4, 40)
    print(1, lru_cache.get(1))  # key 1 renew

    lru_cache.put(5, 50)
    print(1, lru_cache.get(1))
    print(2, lru_cache.get(2))
    print(3, lru_cache.get(3))
    print(4, lru_cache.get(4))
    print(5, lru_cache.get(5))