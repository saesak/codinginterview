"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #dfs approach
        
        n_list = []
        
        if node == None:
            return None
        
        def check(ele, n_list):
            for n in n_list:
                if n.val == ele.val:
                    return (True, n_list.index(n))
            return (False, None)
        
        def dfs(node):
            
            new  = Node(node.val,None)
            n_list.append(new)
            
            #print(node.val)
            
            if node.neighbors:
                new.neighbors = []
                for ele in node.neighbors:
                    tmp = check(ele, n_list)
                    if tmp[0]:
                        new.neighbors.append(n_list[tmp[1]])
                    else:
                        new.neighbors.append(dfs(ele))
                    
            return new 
        
        res = dfs(node)
        
        
        return res

'''
Better solution:

https://leetcode.com/problems/clone-graph/discuss/1482002/Python-Very-clean-and-easy-DFS-beats-95.-Look-no-further.

using a hashmap instead of a list, mapping original nodes to new nodes so i don't have to
use check function but instead i just need to see if it is inside and if so,
return the dict value 

'''