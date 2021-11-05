# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def sym(left, right):
            
            if left == None and right == None:
                return True
            if left == None and right != None:
                return False
            if left != None and right == None:
                return False
            if left.val != right.val:
                return False
            
            return sym(left.left, right.right) and sym(left.right, right.left)
        
        return sym(root.left, root.right)

'''
REVISIT
'''