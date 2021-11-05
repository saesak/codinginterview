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

'''
https://leetcode.com/problems/symmetric-tree/
'''