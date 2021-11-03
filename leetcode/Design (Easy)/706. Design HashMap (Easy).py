'''
hashing using modulo

key point: 

using key % 2069 so that we can use numbers above 2069 as keys
otherwise fails with bigger numbers

2069 is used because it is a big prime number

another key point:
used buckets (aka arrays) to store in hashmap
so every element in the hashmap is an array that you have to iterate
through if it is of some size to find the key you want. so it is 
o(1) lookup time, approximately, but with enough collisions, this gets screwed, no longer at o(1)


a really messy and kind of hacky implementation, would advise replacing. 

REVISIT
'''

class MyHashMap:

    def __init__(self):
        self.hmap = [[] for x in range(2069)]
        

    def put(self, key: int, value: int) -> None:
        
        if key != 0:
            h = key % 2069
        else:
            h = 0
        
        if self.hmap[h] == []:
            self.hmap[h].append([key,value])
        elif len(self.hmap[h]) > 0:
            found = False
            for ind, ele in enumerate(self.hmap[h]):
                if ele[0] == key:
                    ele[1] = value
                    found = True
                    break
                
            if not found:
                self.hmap[h].append([key, value])

    def get(self, key: int) -> int:
        if key != 0:
            h = key % 2069
        else:
            h = 0
        
        if self.hmap[h] == []:
            return -1
        elif len(self.hmap[h]) > 0:
            for ele in self.hmap[h]:
                if ele[0] == key:
                    return ele[1]
        return -1 #in case not found

    def remove(self, key: int) -> None:
        if key != 0:
            h = key % 2069
        else:
            h = 0
        
        if len(self.hmap[h]) > 0:
            for ind, ele in enumerate(self.hmap[h]):
                if ele[0] == key:
                    self.hmap[h].pop(ind)
                    break
                    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)