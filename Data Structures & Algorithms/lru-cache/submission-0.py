class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.hashmap = {}

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert_node(self, node):
        right_prev = self.right.prev
        right_prev_nxt = right_prev.next
        right_prev.next = node
        right_prev_nxt.prev = node
        node.next = right_prev_nxt
        node.prev = right_prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove_node(node)
            self.insert_node(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        
        newNode = Node(key, value)
        self.hashmap[key] = newNode
        self.insert_node(newNode)

        if len(self.hashmap) > self.capacity:
            lru_node = self.left.next
            self.remove_node(lru_node)
            del self.hashmap[lru_node.key]
        
