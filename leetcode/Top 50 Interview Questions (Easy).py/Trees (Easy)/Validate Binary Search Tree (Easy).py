# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def bsthelper(self, root, min_val, max_val):
        if root == None:
            return True
        if min_val !=None and min_val >= root.val:
            return False
        if max_val !=None and max_val <= root.val:
            return False
        left = self.bsthelper(root.left, min_val, root.val)
        print('left' + str(left))
        print(root.val)
        right = self.bsthelper(root.right, root.val, max_val)
        print('right' + str(right))
        print(root.val)
        return left and right
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.bsthelper(root, None, None)

'''
bad soln, find a better way 
'''