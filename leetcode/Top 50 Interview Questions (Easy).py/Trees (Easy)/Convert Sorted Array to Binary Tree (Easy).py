# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        
        
        #root = TreeNode(nums[middle])
        def inputval(array, start, end):
            middle = int(round((start + end) / 2))
            if (end < start):
                return None
            node = TreeNode(array[middle])
            node.left = inputval(array, start, middle - 1)
            node.right = inputval(array, middle + 1, end)
            #root.left = inputval(array[start:middle - 1], start, middle - 1, root)
            #root.right = inputval(array[middle + 1: end], middle + 1, end, root)
            return node
        
        final = inputval(nums, 0, len(nums) - 1)
        
        return final