class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.nodes = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0) #helpers nodes that tracks the LRU and MRU
        self.left.next = self.right
        self.right.prev = self.left
        self.left.prev = self.right.next = None

    def remove_node(self, node: Node) -> LRUCache:
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def insert_node(self, node: Node) -> LRUCache:
        prev_to_right = self.right.prev
        node.prev = prev_to_right
        node.next = self.right
        prev_to_right.next = self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove_node(self.nodes[key])
            self.insert_node(self.nodes[key])
            return self.nodes[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove_node(self.nodes[key])
        self.nodes[key] = Node(key, value)
        self.insert_node(self.nodes[key])

        if len(self.nodes) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.nodes[lru.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)