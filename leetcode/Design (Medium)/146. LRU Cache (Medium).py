'''
super bad implementation but it works

dictionary containing list 

beats 9% in terms of runtime
beats 67% in terms of memory 
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.cache['cap'] = capacity
        self.cache['track'] = []
        
    def get(self, key: int) -> int:
        if key in self.cache:
            tmp = self.cache['track']
            tmp.pop(tmp.index(key))
            tmp.append(key)
            self.cache['track'] = tmp
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            tmp = self.cache['track']
            tmp.pop(tmp.index(key))
            tmp.append(key)
            self.cache['track'] = tmp
        else:
            tmp = self.cache['track']
            if len(tmp) == self.cache['cap']:
                val = tmp.pop(0)
                self.cache.pop(val)
                tmp.append(key)
                self.cache[key] = value
                self.cache['track'] = tmp
            else:
                tmp.append(key)
                self.cache[key] = value
                self.cache['track'] = tmp

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
REVISIT
'''


'''
Better approach using doubly linked list and dictionary, replacing above's 
dictionary but instead putting linked lists inside

O(1) time for get and put
'''

class DLL:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = DLL(0,0) #dummy pointers to reference head and tail make this whole thing a lot easier.
        self.tail = DLL(0,0)
        
        self.cap = capacity
        self.cache = dict()
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def rem(self, node):  #removes from doubly linked list no matter where it is
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def add(self, node): #adds to head of doubly linked list so head is recent, tail is least recent.
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.rem(self.cache[key])
            self.add(self.cache[key])            
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.rem(node)
            self.add(node)
        else:
            node = DLL(key, value)
            self.add(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.cap:
                ret_node = self.rem(self.tail.prev)
                self.cache.pop(ret_node.key)
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)