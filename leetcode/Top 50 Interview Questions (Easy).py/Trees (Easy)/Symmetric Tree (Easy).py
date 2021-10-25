# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    

    
    '''def symhelp(self, root, array, rorl):
        if rorl == 'left':
            if root == None:
                return None
            array.append(root.val)
            array.append(self.symhelp(root.left, array, rorl))
            array.append(self.symhelp(root.right, array, rorl))
        if rorl == 'right':
            if root == None:
                return None
            array.append(root.val)
            array.append(self.symhelp(root.right, array, rorl))
            array.append(self.symhelp(root.left, array, rorl))
        
        
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        
        leftarr = []
        rightarr = []
        
        self.symhelp(root.left, leftarr, 'left')
        self.symhelp(root.right, rightarr, 'right')
        
        print(leftarr)
        print(rightarr)
        
        if len(rightarr) != len(leftarr):
            return False
        
        for idx, ele in enumerate(leftarr):
            if rightarr[idx] != ele:
                return False
        return True'''
    
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSym(root.left, root.right)
        
    def isSym(self, left, right):
        if left == None and right == None:
            return True
        if (left == None and right != None) or (left != None and right == None):
            return False
        '''if left.val == right.val:
            return True'''
        if left.val != right.val:
            return False
        
        
        return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
        