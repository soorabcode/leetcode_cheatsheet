# Day 113 
# LRU Cache 
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
class DListNode:
    """Node for the Doubly Linked List"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> Node
        
        # Initialize dummy head and tail nodes to simplify edge cases
        self.head = DListNode()
        self.tail = DListNode()
        
        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node: DListNode):
        """Add a node right after the head (most recently used position)"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DListNode):
        """Remove an existing node from the linked list"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node: DListNode):
        """Move an existing node to the front (most recently used)"""
        self._remove_node(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front as it's now most recently used
            self._move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, update value and move to front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # If key doesn't exist, create a new node
            new_node = DListNode(key, value)
            
            # Add to hash map and linked list (front)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            # If capacity exceeded, remove the least recently used item (node before tail)
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)