# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
soln that doesn't use bst structure at all

'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = []
        
        def recurse(root, low, high):
            
            if root:
                recurse(root.left, low, high)
                if root.val >= low and root.val <= high:
                    res.append(root.val)
                recurse(root.right, low, high)
            
        recurse(root, low, high)
        
        return sum(res)