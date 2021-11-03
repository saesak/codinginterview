# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
use dfs to first change tree into a graph

then use bfs to go through the tree starting from target to find ones k distance
from target

total is O(N + N) = O(N) time, you iterate through the entire tree twice

total space used is O(N) for visited and still O(N + N) = O(N) if you count initial tree we
change to graph 
'''

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(root, par = None):
            
            if root != None:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root, None)
        
        visited = {target}
        res = []
        
        def bfs(root, k):
            
            queue = [(root, 0)]
            
            while queue:
                curr = queue.pop(0)
                
                if curr[1] == k:
                    res.append(curr[0].val)
                
                curr_list = [(curr[0].left, curr[1] + 1), 
                             (curr[0].right, curr[1] + 1), 
                             (curr[0].par, curr[1] + 1)]
                for ele in curr_list:
                    if ele[0] not in visited and ele[0] != None:
                        visited.add(ele[0])
                        queue.append(ele)
                        
        bfs(target, k)
        
        return res