# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    #left to right  
    def descend(self, root, arr, depth):
        '''while left != None or right != None:
            arr.append([])
            if left != None:
                lleft = 
            if right != None:
                
            depth = depth + 1'''
        if root.left == None and root.right == None:
            depth = depth - 1 
            return root.val
        while len(arr) < depth + 1:
            arr.append([])
        if root.left != None:
            arr[depth].append(self.descend(root.left, arr, depth + 1))
        if root.right != None:
            arr[depth].append(self.descend(root.right, arr, depth + 1))
        return root.val
        
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr = []
        if root == None:
            return arr
        if root.left == None and root.right == None:
            arr.append([root.val])
            return arr
        #arr.append([root.val])
        arr.insert(0,[self.descend(root, arr, 0)])
        
        return arr