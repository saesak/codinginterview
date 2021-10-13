# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        depth = 1
        
        def recurse(root, depth):
            while depth > len(res):
                res.append([])
            
            if root.left != None:
                recurse(root.left, depth + 1)
            
            if depth % 2 == 1:
                res[depth - 1].append(root.val)
            else:
                res[depth - 1].insert(0, root.val)
                
            if root.right != None:
                recurse(root.right, depth + 1)
        
        if root == None:
            return []
        
        recurse(root, depth)
        
        return res
'''
recursive sol

use inorder traversal except add depth parameter
'''

