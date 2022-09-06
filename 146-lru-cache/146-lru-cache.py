class Node:
    def __init__(self, val, n=None, p=None):
        self.val = val
        self.next = n
        self.prev = p


class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        
        temp = self.tail.prev
        self.tail.prev = node
        temp.next = node
        node.next = self.tail
        node.prev = temp

    def delete(self, node):
        
        temp = node.prev
        n = node.next
        temp.next = n
        n.prev = temp
        
        node.next = None
        node.prev = None
    
    def get(self, key: int) -> int:
        
        if key in self.lru:
            node = self.lru[key]
            self.delete(node)
            self.insert(node)
            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru:
            self.delete(self.lru[key])
            self.lru[key] = Node((key, value))
            self.insert(self.lru[key])
        else:
            if len(self.lru) == self.capacity:
                self.lru.pop(self.head.next.val[0])
                self.delete(self.head.next)
                
            
            self.lru[key] = Node((key, value))
            self.insert(self.lru[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)